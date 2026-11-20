#!/usr/bin/env python3
"""Creator Cards : tire les cartes ou retrouve celles qu'on a tirées.

  python3 tirer.py                 tire 5 cartes au hasard (1 par famille)
  python3 tirer.py build           tire un Build au hasard
  python3 tirer.py B01             les 5 cartes du Build B01
  python3 tirer.py H06 F01 ...     retrouve des cartes par code ou par nom
  python3 tirer.py liste           toutes les cartes
Affiche les codes et les noms. Le détail de chaque carte est dans cartes.md.
"""
import json, random, sys, unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent
D = json.loads((ICI / "cartes.json").read_text())
FAM = D["familles"]
ORDRE = list(FAM.keys())


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    for x in "’'-.":
        s = s.replace(x, " ")
    return " ".join(w for w in s.split() if w not in {"l", "le", "la", "les", "de", "du"})


TOUTES = {c["code"].upper(): (f, c["nom"]) for f in ORDRE for c in FAM[f]}
BUILDS = {b["code"].upper(): b for b in D["builds"]}


def montre(code):
    f, nom = TOUTES[code]
    print(f"{f:8} {code:6} {nom}")


def cherche(mot):
    m = mot.upper()
    if m in TOUTES or m in BUILDS:
        return m
    n = norm(mot)
    for code, (_, nom) in TOUTES.items():
        if norm(nom) == n:
            return code
    for b in BUILDS.values():
        if norm(b["nom"]) == n:
            return b["code"].upper()
    hits = [c for c, (_, nom) in TOUTES.items() if n and n in norm(nom)]
    return hits[0] if len(hits) == 1 else None


def build(code):
    b = BUILDS[code]
    print(f"BUILD    {b['code']:6} {b['nom']}")
    for code_carte in b["cartes"].values():
        if code_carte and code_carte.upper() in TOUTES:
            montre(code_carte.upper())


a = sys.argv[1:]
if not a:
    for f in ORDRE:
        if f.upper() != "BUILD":
            montre(random.choice(FAM[f])["code"].upper())
elif a[0].lower() == "build":
    build(random.choice(list(BUILDS)))
elif a[0].lower() == "liste":
    for f in ORDRE:
        for c in FAM[f]:
            montre(c["code"].upper())
    for code in BUILDS:
        print(f"BUILD    {code:6} {BUILDS[code]['nom']}")
else:
    for mot in (a if len(a) > 1 else [a[0]]):
        code = cherche(mot)
        if code is None:
            print(f"?        {mot}  (introuvable : regarde « liste »)")
        elif code in BUILDS:
            build(code)
        else:
            montre(code)
