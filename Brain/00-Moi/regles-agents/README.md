---
description: "Comment marchent les carnets des agents : chaque correction = 1 règle dans le carnet de l'agent. À lire avant d'écrire dans un carnet."
type: index
statut: actif
sujets: [ia]
---
# Carnets d'apprentissage des agents

Un carnet par agent. Chaque correction que tu fais devient une règle définitive : l'agent ne refait jamais deux fois la même erreur.

## Comment ça tourne
1. Chaque agent lit son carnet AVANT de travailler. Le carnet passe avant le reste de ses consignes.
2. Tu corriges, notes ou refuses un travail (même en passant, dans n'importe quel chat) → Claude ajoute UNE ligne dans le carnet de l'agent ou du skill concerné : `JJ/MM/AAAA · d'où ça vient · ce qui n'allait pas → règle`.

## Qui est qui
| Fichier | Nom | Rôle |
|---|---|---|
| stratege.md | Le Stratège | agent n°1 : calendrier, positionnement, offre, analyse |
| scripteur.md | Le Scripteur | agent n°2 : scripts, copywriting, ta façon de parler |
| supermonteur.md | Le Monteur | agent n°3 : montage et variantes |
| carrousel.md | Le Carrousel | agent n°4 : carrousels |
| publieur.md | Le Publieur | agent n°5 : descriptions, heure, publication |
| stratege-contenu.md | Stratège contenu | skill du Stratège : chiffres et sujets |
| audit-insta.md | L'Auditeur Insta | skill du Stratège : analyse d'un compte |
| positionneur.md | Le Positionneur | skill du Stratège : fiche de positionnement |
| offre.md | Le Créateur d'offres | skill du Stratège : offre notée sur 10 |
| copywriter.md | Le Copywriter | skill du Scripteur : pages, DM, emails, légendes |
| anti-ia.md | Le Gommeur | skill du Scripteur et du Publieur : retire le ton IA |
| ma-marque.md | Ma marque | ta voix, ta cible, tes couleurs |
| slides.md | Le Projectionniste | bonus : slides, retours sur les carrousels |
