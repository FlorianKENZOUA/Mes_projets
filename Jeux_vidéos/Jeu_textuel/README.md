# 🏝️ Tropical Mystery – Jeu textuel

**Tropical Mystery** est un jeu vidéo textuel de type *escape game* à monde ouvert.  
Développé en Python dans un cadre scolaire, ce projet propose une aventure immersive sur une île mystérieuse où réflexion, exploration et interactions sont la clé pour s’échapper.

🎥 [Voir la démonstration du jeu sur YouTube](https://www.youtube.com/watch?v=2EAcJZU1Igs)

---

## 🎮 Concept du jeu

Vous incarnez un explorateur échoué sur une île paradisiaque.  
Votre mission : retrouver **un code secret** détenu par plusieurs habitants de l’île. Chaque habitant porte une bague comportant un chiffre du code.  
Une seule tentative vous est accordée pour déverrouiller le coffre et vous échapper... sinon, vous resterez piégé pour toujours.

---

## 🧭 Commandes disponibles

Voici la liste des commandes que vous pouvez utiliser pendant la partie :

- `help` : affiche les commandes disponibles.
- `go` : se déplacer dans une direction.
- `back` : revenir à la pièce précédente.
- `look` : observer l’environnement.
- `history` : consulter l’historique des lieux visités.
- `take` : ramasser un objet.
- `drop` : se débarrasser d’un objet.
- `check` : voir le contenu de son inventaire.
- `talk` : discuter avec un PNJ.
- `quit` : quitter la partie (progression non sauvegardée).

---

## 🧱 Structure du code (UML simplifiée)

Le jeu repose sur plusieurs classes orientées objet :

- `Game` : gestion globale de la partie.
- `Player` : gestion du joueur, de son inventaire et ses déplacements.
- `Room` : chaque lieu du jeu avec ses objets et personnages.
- `Item` : objets ramassables dans l’environnement.
- `Character` : PNJ avec lesquels interagir.
- `Command` : structure des commandes disponibles.
- `Actions` : ensemble des fonctions liées aux commandes.

---

## 🛠️ Perspectives d’évolution

- Création d’une **interface graphique** pour améliorer l’expérience utilisateur.
- **Système de dialogues à choix multiples** pour enrichir les interactions avec les PNJ.
- Ajout de **paramètres de survie** (faim, soif…) et de **quêtes secondaires** pour complexifier le gameplay.

---

## 👥 Développeurs

- **Amine Muskud** – ESIEE Paris, filière E3S  
- **Florian Kenzoua** – ESIEE Paris, filière E3FD

---
