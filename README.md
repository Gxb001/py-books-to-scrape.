# Books to Scrape - Projet de Web Scraping

## Aperçu

Ce projet est une application de web scraping développée en Python pour extraire des données de livres du
site [Books to Scrape](http://books.toscrape.com/). Il comprend quatre étapes principales et deux bonus, comme spécifié
dans les exigences du projet :

1. **Étape 1** : Scraper les données d'un seul livre et les sauvegarder dans un fichier Excel.
2. **Étape 2** : Scraper tous les livres de la catégorie "Travel" et les sauvegarder dans un fichier CSV.
3. **Étape 3** : Scraper tous les livres du site (catégorie "Books") et les sauvegarder dans un fichier CSV.
4. **Étape 4** : Télécharger les images de couverture de tous les livres scrapés à l'étape 3.
5. **Bonus 1** : Générer un fichier CSV récapitulatif (`books_details_by_category.csv`) avec des statistiques par
   catégorie et créer un diagramme circulaire montrant la répartition des livres pour les 20 premières catégories.
6. **Bonus 2** : Créer un histogramme montrant les prix moyens des livres par catégorie.

Le script est optimisé pour la performance grâce à des requêtes HTTP asynchrones (`aiohttp`) et inclut une mesure du
temps d'exécution pour évaluer les performances.

## Fonctionnalités

- **Scraping asynchrone** : Utilise `aiohttp` pour des requêtes HTTP non bloquantes, réduisant le temps d'exécution à ~
  2-4 minutes pour ~1000 livres et images.
- **Extraction de données** : Collecte des informations détaillées sur les livres, incluant l'URL, l'UPC, le titre, les
  prix, la disponibilité, la description, la catégorie, la note et l'URL de l'image.
- **Sorties de fichiers** :
    - Fichier Excel pour un livre unique (Étape 1).
    - Fichiers CSV pour les données par catégorie et site entier (Étapes 2 et 3).
    - Fichier CSV récapitulatif par catégorie (Bonus 1).
    - Images des couvertures de livres (Étape 4).
    - Visualisations (diagramme circulaire et histogramme) sous forme de fichiers PNG (Bonus 1 et 2).
- **Gestion robuste des URL** : Utilise `urljoin` pour résoudre correctement les URL relatives dans différentes
  structures de catégories.
- **Visualisation des données** : Génère un diagramme circulaire (20 premières catégories par nombre de livres) et un
  histogramme (prix moyens par catégorie) avec `matplotlib`.
- **Gestion des erreurs** : Inclut une gestion complète des erreurs pour les requêtes HTTP, le parsing et les opérations
  sur les fichiers.
- **Suivi du temps** : Mesure et affiche le temps d'exécution total dans un format lisible.

## Prérequis

- **Python** : Version 3.7 ou supérieure.
- **Dépendances** : Installer les bibliothèques Python requises via `pip` (voir Installation ci-dessous).
- **Connexion Internet** : Nécessaire pour scraper le site Books to Scrape.
- **Environnement graphique** (optionnel) : Requis pour afficher les graphiques Matplotlib de manière interactive. Si
  exécuté sur un serveur, commenter les appels à `plt.show()`.

## Installation

1. **Cloner ou télécharger le projet** :
    - Téléchargez le script (`scrape_book_category.py`) ou clonez le dépôt si applicable.

2. **Installer les dépendances** :
   Exécutez la commande suivante pour installer les bibliothèques requises :
   ```bash
   pip install requests beautifulsoup4 openpyxl aiohttp pandas matplotlib
   ```

3. **Vérifier la configuration** :
   Assurez-vous que Python est installé et accessible :
   ```bash
   python --version
   ```

## Utilisation

1. **Exécuter le script** :
   Lancez le script depuis la ligne de commande :
   ```bash
   python scrape_book_category.py
   ```

2. **Exécution attendue** :
    - Le script traitera les étapes 1 à 4 et les bonus 1 et 2 séquentiellement.
    - Des messages de progression seront affichés pour chaque étape (par exemple, "Livre scrapé : A Light in the
      Attic", "Image téléchargée : poetry_rgp6kl3n.png").
    - Le temps d'exécution total sera affiché à la fin (par exemple, "Temps d'exécution total : 2 minutes et 54
      secondes").

3. **Fichiers générés** :
    - **Étape 1** : `A_Light_in_the_Attic.xlsx` (fichier Excel avec les données d'un livre, en-têtes colorés).
    - **Étape 2** : `Travel.csv` (fichier CSV avec ~11 livres de la catégorie "Travel").
    - **Étape 3** : `All_Books.csv` (fichier CSV avec ~1000 livres du site entier).
    - **Étape 4** : Répertoire `/images` contenant ~1000 images de couvertures (par exemple, `poetry_rgp6kl3n.png`).
    - **Bonus 1** :
        - `books_details_by_category.csv` (CSV avec colonnes : `category`, `books_count`, `average_price` pour ~50
          catégories).
        - `books_by_category_pie_chart.png` (diagramme circulaire montrant la répartition des livres pour les 20
          premières catégories).
    - **Bonus 2** : `average_price_by_category_histogram.png` (histogramme montrant les prix moyens par catégorie).

4. **Remarques** :
    - Si vous exécutez dans un environnement non graphique (par exemple, un serveur), commentez `plt.show()` dans
      `plot_pie_chart` et `plot_price_histogram` pour éviter des erreurs d'affichage.
    - Le script utilise un sémaphore pour limiter les requêtes HTTP à 20 connexions simultanées afin de ne pas
      surcharger le serveur.

## Structure du projet

- **Script principal** : `scrape_book_category.py`
    - Contient toutes les fonctions pour le scraping, la génération de fichiers et la visualisation.
    - Organisé en fonctions modulaires pour chaque tâche (par exemple, `fetch_page`, `scrape_category`,
      `plot_pie_chart`).
- **Fonctions clés** :
    - `fetch_page` / `async_fetch_page` : Récupèrent le contenu HTML (synchrone pour l'étape 1, asynchrone pour les
      autres).
    - `extract_book_info` : Analyse les détails des livres à partir du HTML.
    - `save_to_csv` / `save_to_excel` : Sauvegardent les données dans des fichiers CSV/Excel.
    - `get_book_urls_from_category` : Collecte les URL des livres avec gestion de la pagination.
    - `scrape_category` : Scrape les données des livres pour une catégorie.
    - `async_download_book_images` : Télécharge les images de couverture des livres.
    - `generate_category_summary_csv` : Crée le CSV récapitulatif par catégorie.
    - `plot_pie_chart` : Génère le diagramme circulaire pour les 20 premières catégories (Bonus 1).
    - `plot_price_histogram` : Génère l'histogramme des prix moyens (Bonus 2).
    - `main` : Orchestre toutes les étapes et mesure le temps d'exécution.

## Sorties

### Étape 1 : Livre unique

- **Fichier** : `A_Light_in_the_Attic.xlsx`
- **Contenu** : Données d'un livre (URL, UPC, titre, prix, disponibilité, description, catégorie, note, URL de l'image)
  dans un fichier Excel avec en-têtes colorés.

### Étape 2 : Catégorie Travel

- **Fichier** : `Travel.csv`
- **Contenu** : ~11 livres de la catégorie "Travel", avec les mêmes champs que l'étape 1, sauvegardés au format CSV (
  délimiteur : `;`).

### Étape 3 : Tous les livres

- **Fichier** : `All_Books.csv`
- **Contenu** : ~1000 livres du site entier, avec les mêmes champs, sauvegardés au format CSV (délimiteur : `;`).

### Étape 4 : Images des livres

- **Répertoire** : `/images`
- **Contenu** : ~1000 images PNG nommées par catégorie et chaîne aléatoire (par exemple, `poetry_rgp6kl3n.png`).

### Bonus 1 : Récapitulatif par catégorie et diagramme circulaire

- **Fichier** : `books_details_by_category.csv`
    - Colonnes : `category`, `books_count`, `average_price` (basé sur `price_including_tax`).
    - Exemple :
      ```csv
      category;books_count;average_price
      Fiction;65;35.28
      Poetry;19;45.12
      Travel;11;38.75
      ...
      ```
- **Fichier** : `books_by_category_pie_chart.png`
    - Diagramme circulaire montrant la répartition des livres pour les 20 premières catégories, avec des pourcentages (
      par exemple, "Fiction : 6.5%").

### Bonus 2 : Histogramme des prix

- **Fichier** : `average_price_by_category_histogram.png`
    - Diagramme en barres montrant les prix moyens des livres pour ~50 catégories, triés par prix.
    - Axe X : Catégories (étiquettes inclinées à 45° pour la lisibilité).
    - Axe Y : Prix moyen (£).

## Performances

- **Temps d'exécution** : ~2-4 minutes pour toutes les étapes, grâce aux requêtes HTTP asynchrones (`aiohttp`) avec une
  limite de 20 connexions simultanées.
- **Optimisation** :
    - Le scraping et le téléchargement asynchrones réduisent le temps d'exécution de ~17 minutes (synchrone) à ~2-4
      minutes.
    - La limite du sémaphore empêche la surcharge du serveur.
- **Suivi du temps** : Le temps d'exécution total est affiché à la fin (par exemple, "Temps d'exécution total : 2
  minutes et 54 secondes (174.23 secondes)").

## Remarques

- **Gestion des erreurs** : Le script inclut une gestion robuste des erreurs pour les échecs HTTP, les problèmes de
  parsing et les opérations sur les fichiers. Les erreurs sont consignées dans la console sans arrêter l'exécution.
- **Charge du serveur** : La limite du sémaphore (20 requêtes simultanées) évite de surcharger le serveur Books to
  Scrape. En cas d'erreurs comme HTTP 429, réduisez la limite du sémaphore (par exemple, à 10) dans
  `get_book_urls_from_category`, `scrape_category` et `async_download_book_images`.
- **Environnement graphique** : Commentez `plt.show()` dans `plot_pie_chart` et `plot_price_histogram` pour les
  environnements non graphiques (par exemple, serveurs) afin d'éviter des erreurs d'affichage.
- **Personnalisation** :
    - Pour modifier le nombre de catégories dans le diagramme circulaire, ajustez `.head(20)` dans `plot_pie_chart`.
    - Pour limiter les catégories dans l'histogramme, ajoutez `.head(n)` dans `plot_price_histogram`.
    - Pour utiliser `price_excluding_tax` au lieu de `price_including_tax`, mettez à jour
      `generate_category_summary_csv` et `plot_price_histogram`.
- **Extensibilité** : Des visualisations supplémentaires (par exemple, boîtes à moustaches, nuages de points) ou des
  statistiques peuvent être ajoutées en étendant les fonctions des bonus.

## Résolution des problèmes

- **Erreurs HTTP (par exemple, 429 Trop de requêtes)** :
    - Réduisez la limite du sémaphore dans `get_book_urls_from_category`, `scrape_category` et
      `async_download_book_images` (par exemple, de 20 à 10).
    - Ajoutez un délai (par exemple, `await asyncio.sleep(0.1)`) dans `async_fetch_page`.
- **Erreurs d'affichage Matplotlib** :
    - Si exécuté sur un serveur, commentez `plt.show()` dans `plot_pie_chart` et `plot_price_histogram`.
- **Données manquantes** :
    - Assurez-vous que `all_books_data` est rempli (Étape 3). Vérifiez les erreurs HTTP ou de parsing dans la sortie de
      la console.
- **Problèmes d'encodage des fichiers** :
    - Tous les fichiers CSV utilisent l'encodage UTF-8 et le délimiteur `;` pour la compatibilité.
