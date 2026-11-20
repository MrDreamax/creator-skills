# Creator Skills : 5 agents IA qui font ton contenu

Une équipe de 5 agents IA, dans ton app Claude, sur ton Mac :

1. **Le Stratège** : analyse ton contenu, fait ton calendrier, pose ton positionnement, crée ton offre.
2. **Le Scripteur** : écrit tes scripts de vidéos virales et tes textes de vente, avec TA façon de parler.
3. **Le Monteur** : monte tes vidéos en reels prêts à poster, et te fait des variantes à tester.
4. **Le Carrousel** : fait tes carrousels Instagram avec tes vraies photos.
5. **Le Publieur** : écrit la description et choisit l'heure, pour chaque réseau. Rien ne part sans ton OK.

Bonus : le jeu Creator Cards. Tire 5 cartes (Hook, Format, Concept, Émotion, CTA), Le Scripteur écrit le script qui les suit.

Tu parles à Claude dans le chat. Aucune appli à ouvrir.

## Avant de commencer
1. **Claude (obligatoire)** : l'app sur claude.ai/download, abonnement Pro ou plus (le gratuit n'ouvre pas l'onglet Code).
2. **ElevenLabs (obligatoire pour monter et transcrire)** : compte sur elevenlabs.io, formule Starter (environ 5 €/mois, suffit largement ; Creator si un jour il en manque). Crée une clé API. Après l'installation : copie-la, puis dis à Claude « Range ma clé ElevenLabs ».
3. **Blotato (obligatoire pour publier)** : compte sur blotato.com (~29 $/mois), branche tes réseaux. Puis dans Claude : Réglages > Connecteurs > Blotato. Il publie tes reels et envoie tes cadeaux en message privé quand on commente ton mot-clé.
4. **Les 100 musiques (obligatoire pour les montages)** : télécharge le fichier des musiques (lien envoyé à part). Pendant l'installation, Claude te le demande et le range tout seul.
5. **Google Chrome (obligatoire pour les carrousels et les PDF)** : google.com/chrome.
6. **Node et ffmpeg (obligatoires pour monter)** : les deux moteurs du Monteur. Après l'installation, dis « Installe mes logiciels » : Claude les installe ou te guide.
7. **Apify (optionnel, payant)** : seulement si tu veux que Le Stratège analyse un compte Instagram tout seul. Sans Apify, tu lui donnes des captures.
8. **Conseillés** : Wispr Flow (wisprflow.ai, tu dictes au lieu d'écrire), Obsidian (obsidian.md, pour lire ta mémoire), Fathom (fathom.video, tes appels transcrits).

## Installer (5 minutes)
1. Ouvre l'app Claude sur ton Mac, onglet **Code**.
2. Colle cette phrase :

   > Installe Creator Skills qui est ici : https://github.com/MrDreamax/creator-skills

3. Clique « Autoriser » quand Claude le demande. À la fin, Claude lance « Bienvenue » (3 minutes de questions) et ouvre ton guide.

Ton guide pas à pas : `Documents/Brain/GUIDE.html`. À tout moment : « Montre-moi le guide ».

Règle de base : Claude prépare, toi tu décides. Rien n'est envoyé, publié ou payé sans ton OK. **Publication en mode essai** tant que tu ne l'actives pas toi-même.

## Pour Claude (installation)
1. `git clone https://github.com/MrDreamax/creator-skills ~/Documents/creator-skills` (ou `git -C ~/Documents/creator-skills pull` s'il existe déjà).
2. `bash ~/Documents/creator-skills/install.sh` (relançable : c'est aussi la mise à jour ; le profil du master prompt, le Brain perso, les réglages, la DA, les reels et les carrousels de la personne ne sont jamais écrasés, rien n'est supprimé chez elle, l'ancienne version est sauvegardée dans `~/.claude/backups/`).
3. Demande son prénom (bouton) et écris-le dans `~/Documents/SuperApps/config.json` → `"nom"`.
4. Le Monteur appelle Claude tout seul : vérifie `claude auth status`. Pas connecté = double-clic sur `~/Documents/SuperApps/superda/connecter-claude.command`.
5. Lance le skill `bienvenue` (~/.claude/skills/bienvenue/SKILL.md) : il remplit le profil et ouvre le guide à la fin.
6. Ne mets jamais `"mode_essai": false` toi-même : c'est à la personne de le faire.
7. Musiques : si install.sh affiche `MUSIQUES_MANQUANTES`, Bienvenue (étape 6 ter) demande le fichier et lance `bash ~/Documents/creator-skills/ranger-musiques.command`. À tout moment : « Range mes musiques ».
8. « Range ma clé ElevenLabs » : la clé est dans son presse-papier, lance `bash ~/Documents/creator-skills/ranger-cle-elevenlabs.command` (jamais la clé dans le chat).

Ce qui est installé : `~/.claude/CLAUDE.md` (master prompt), `~/.claude/skills/` (les 5 agents + leurs skills), les moteurs du Monteur et du Carrousel dans `~/Documents/SuperApps/`, le Brain (mémoire + fiches d'experts) dans `~/Documents/Brain/`.

Fiches des 7 conseillers (`Brain/08-Conseillers/`) : d'après roast-room de Nate Herk (licence MIT).
