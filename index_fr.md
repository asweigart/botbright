# Botbright

[🇬🇧 English](index.md) · [🇪🇸 Español](index_es.md) · **🇫🇷 Français** · [🇩🇪 Deutsch](index_de.md) · [🇮🇹 Italiano](index_it.md) · [🇵🇹 Português](index_pt.md) · [🇷🇺 Русский](index_ru.md) · [🇨🇳 中文](index_zh.md) · [🇯🇵 日本語](index_ja.md) · [🇰🇷 한국어](index_ko.md) · [🇮🇳 हिन्दी](index_hi.md) · [🇧🇩 বাংলা](index_bn.md) · [🇻🇳 Tiếng Việt](index_vi.md) · [🇸🇦 العربية](index_ar.md) · [🇹🇭 ไทย](index_th.md) · [🇵🇭 Tagalog](index_tl.md) · [🇳🇴 Norsk](index_no.md) · [🇳🇱 Nederlands](index_nl.md) · [🇸🇪 Svenska](index_sv.md) · [🇹🇷 Türkçe](index_tr.md) · [🇰🇪 Kiswahili](index_sw.md) · [🇮🇩 Bahasa Indonesia](index_id.md) · [🇵🇱 Polski](index_pl.md) · [🇬🇷 Ελληνικά](index_el.md) · [🇮🇱 עברית](index_he.md) · [🇵🇭 Filipino](index_fil.md) · [🇨🇿 Čeština](index_cs.md) · [🇩🇰 Dansk](index_da.md) · [🇫🇮 Suomi](index_fi.md) · [🇷🇴 Română](index_ro.md) · [🇭🇺 Magyar](index_hu.md) · [🇭🇷 Hrvatski](index_hr.md)

---

Botbright est un clone en JavaScript dans un seul fichier du jeu de réflexion Flash *Lightbot*. Programme un robot isométrique pour qu'il parcoure une grille de tuiles 3D et illumine les tuiles bleues à atteindre. Glisse des tuiles d'instruction dans la mémoire du robot, appuie sur **Lancer** et regarde ton programme s'exécuter.

Tout le jeu tient dans un seul fichier HTML (`botbright.html`) avec CSS et JavaScript intégrés — pas de build, pas de dépendances externes, pas d'appels réseau. Ouvre le fichier dans n'importe quel navigateur récent et joue. Enregistre-le sur ton disque dur et il continuera à fonctionner hors ligne pour toujours.

Tu peux aussi changer la palette de couleurs et faire porter différents chapeaux à ton robot. Un éditeur de niveaux est intégré, et les niveaux et chapeaux peuvent être importés ou exportés au format JSON.

## Jouer

Double-clique sur le fichier botbright.html ou ouvre-le dans ton navigateur. Le jeu fonctionne hors ligne.

Version en ligne : [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

## Comment ça marche

Le robot dispose de trois zones de mémoire :

- **Mémoire principale** — 12 emplacements d'instructions, s'exécute quand tu appuies sur Lancer
- **Mémoire F1** — 8 emplacements d'instructions, une fonction appelable
- **Mémoire F2** — 8 emplacements d'instructions, une seconde fonction appelable

Glisse les tuiles d'instruction depuis la palette vers la mémoire. Réorganise en les faisant glisser entre les emplacements. Sors une tuile d'un emplacement pour la supprimer.

| Instruction | Effet |
|-------------|------------|
| Avancer | Avance d'une tuile vers l'avant, si elle est à la même hauteur |
| Tourner à gauche | Tourne de 90° dans le sens antihoraire |
| Tourner à droite | Tourne de 90° dans le sens horaire |
| Sauter | Monte d'un niveau, ou descend de plusieurs niveaux |
| Allumer | Bascule la tuile cible sous le robot |
| Appeler F1 / F2 | Empile cette fonction sur la pile d'appels (récursion autorisée, avec limites) |

Un niveau est terminé lorsque chaque tuile cible est allumée en jaune.

Les programmes trop longs sont interrompus : 1000 instructions au total maximum, 100 cadres dans la pile maximum.

## Contrôles

**Caméra** — WASD ou flèches pour déplacer, Q/E ou PageHaut/PageBas pour tourner de 90°, +/− ou molette pour zoomer. Appuie sur 0 pour réinitialiser la vue. Fais glisser la zone de jeu pour la déplacer, pince pour zoomer, fais pivoter avec deux doigts pour tourner. Maintiens les boutons caméra à l'écran pour un mouvement continu et fluide.

**Largeur du panneau latéral** — fais glisser la séparation entre la zone de jeu et le panneau.

**Vitesse** — curseur dans le panneau : lent / normal / rapide. Ajustable pendant l'exécution.

## Éditeur de niveaux

Un éditeur complet est livré avec le jeu. Ajoute/duplique/supprime des niveaux, redimensionne la grille (1–32 dans chaque dimension), peins des hauteurs de 0 à 9, marque les tuiles cibles, définis la position et l'orientation de départ, et teste le niveau sans quitter l'éditeur.

Le jeu de niveaux complet s'exporte au format JSON et s'importe de la même manière, pour partager des niveaux ou sauvegarder tes modifications.

## Éditeur de chapeaux

Le robot peut porter des chapeaux. Dix-neuf options sont incluses : Aucun, Chapeau haut-de-forme, Chapeau de sorcier, Couronne, Bonnet, Casquette, Chapeau de cowboy, Chapeau de fête, Chapeau melon, Auréole, Cornes de diable, Sombrero, Chapeau de sorcière, Fez, Bois, Oreilles de lapin, Oreilles de chat, Casque de plongée et Casque viking. Chaque chapeau est défini par quatre sprites SVG — un par orientation à l'écran — pour qu'il suive la direction du robot à toutes les rotations de caméra (la visière de la casquette, la boucle du chapeau de sorcière, le hublot du casque de plongée et les oreilles de lapin/chat se déplacent en conséquence). Un aperçu en direct fait tourner le robot une fois par seconde pour voir le chapeau sous tous les angles. Les chapeaux s'exportent et s'importent également au format JSON pour des designs personnalisés.

## Palettes de couleurs

Un panneau **Couleurs** dans la barre latérale expose la palette : couleur des tuiles, couleur des bords, couleur des cibles, couleur des cibles allumées, fond et corps du robot. Tu peux utiliser un thème intégré ou les modifier toi-même.

## Langues

Traductions de l'interface en 23 langues : anglais, espagnol, français, allemand, italien, portugais, russe, chinois, japonais, coréen, hindi, bengali, vietnamien, arabe (avec mise en page de droite à gauche), thaï, tagalog, norvégien, néerlandais, suédois, turc, swahili, indonésien et polonais. La langue par défaut suit la propriété `navigator.language` du navigateur ; le sélecteur de langue de l'écran d'accueil la remplace pour la session. Les noms et descriptions des niveaux intégrés, ainsi que les noms des chapeaux intégrés, sont traduits dans toutes les langues prises en charge. L'éditeur de niveaux n'écrit que dans la langue actuellement sélectionnée lorsque tu modifies un nom ou une description, sans toucher aux autres traductions.

## Mode clair / sombre

Suit la préférence `prefers-color-scheme` du navigateur pour l'interface. Sélectionner le thème **Par défaut** dans le panneau Couleurs applique la palette correspondant au mode actuel du navigateur, et reste synchronisée si tu changes de mode. Tout autre thème intégré — ou une palette personnalisée — remplace ce comportement.

## Crédits

Créé par Al Sweigart — [https://inventwithpython.com/botbright/](https://inventwithpython.com/botbright/)

Inspiré de *Lightbot* de Daniel Yaroslavski.
