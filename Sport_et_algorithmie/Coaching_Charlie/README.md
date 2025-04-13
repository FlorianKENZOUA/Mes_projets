# 🏃‍♂️ Algorithme de coaching basé sur les données GPS et résultats de course

Ce projet a été développé en Python sous Visual Studio Code.  
Il permet d'analyser les performances d'un coureur (Charlie) sur deux éditions successives d'une course, à partir de données GPS et de résultats officiels, afin de produire un bilan complet et personnalisé.

---

## 📁 Contenu du dossier

Le dossier contient tous les fichiers nécessaires au bon fonctionnement du programme :

### 📦 Données
- `ecorun_2022_copie.gpx` : fichier GPS de la course de Charlie en 2022.
- `ecorun_2023_copie.gpx` : fichier GPS de la course de Charlie en 2023.
- `ecorun_2022_scrape.xlsx` : résultats officiels de l'édition 2022 (issus de scraping).
- `Résultats_2023_scrape.xlsx` : résultats officiels de l'édition 2023 (issus de scraping).

### 🧠 Code
- `ecorun_2022.py` : analyse des données de 2022.
- `ecorun_2023.py` : analyse des données de 2023.
- `cotation.py` : module d’algorithme de cotation utilisé pour l’évaluation des performances.
- `bilan_2022_2023.py` : comparaison et synthèse des deux éditions.
- `main.py` : point d’entrée du programme (à exécuter).

---

## ▶️ Comment exécuter le programme

1. Ouvrir le fichier `main.py` dans VS Code ou un autre éditeur Python.
2. Agrandir la fenêtre du terminal pour un affichage optimal.
3. Lancer le script et suivre les instructions affichées dans le terminal.

---

## 🧩 À propos

Ce projet s'inscrit dans une démarche de **coaching basé sur les données**.  
Il exploite des fichiers `.gpx` (montre GPS) et des classements pour fournir un retour quantifié, objectif et accessible à l’athlète.

---

## 🔧 Technologies utilisées

- Python
- Visual Studio Code
- Pandas, Matplotlib, GPXPy, etc.

---
