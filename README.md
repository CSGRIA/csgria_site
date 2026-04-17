# CSGR-IA Website Project

## Overview
This project is a professional web platform developed for CSGR-IA. The website is designed to present the organization's missions, history, and governance through a dynamic and manageable interface. It features a comprehensive administration system that allows for real-time updates of the landing page content, organizational timeline, and team profiles.

## Technologies
The project is built using the following stack:
- **Core Framework**: Django 5.2
- **Database**: SQLite3
- **Media Handling**: Pillow (for image processing)
- **Frontend**: HTML5, Vanilla CSS3 (utilizing CSS variables for theme management), and JavaScript
- **Fonts**: Poppins (via Google Fonts)

## Codebase Structure
The project follows a standard modular Django architecture:

- **csgria_site/**: Contains project-level configurations, settings, and main URL routing.
- **core/**: The primary application managing the site's core features.
    - **models.py**: Definitions for Carousels, Missions, About Us sections, Events (Timeline), Profiles (Governance), and Contact Information.
    - **views.py**: View logic for the Home, About, and Contact pages.
    - **context_processors.py**: Global context provider for site-wide contact information.
- **actualite/**: A placeholder application for future news and blog features.
- **account/**: A placeholder application for future user authentication and profile management.
- **templates/**: Centralized directory for HTML templates using Django Template Language (DTL).
- **static/** & **media/**: Directories for managing static assets and user-uploaded content.

## Installation and Setup

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### Environment Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On Linux/macOS: `source venv/bin/activate`

### Dependency Installation
Install the required packages using the requirements file:
```bash
pip install -r requirements.txt
```

### Database Initialization
Run the migrations to create the database schema:
```bash
python manage.py migrate
```

### Administrative Access
Create a superuser to access the Django Administration panel:
```bash
python manage.py createsuperuser
```

## Running the Project
To start the local development server:
```bash
python manage.py runserver
```
Once the server is running, the website will be accessible at http://127.0.0.1:8000/ and the administration panel at http://127.0.0.1:8000/admin/.

---

# Projet Site Web CSGR-IA (Version Française)

## Présentation
Ce projet est une plateforme web professionnelle développée pour CSGR-IA. Le site est conçu pour présenter les missions, l'histoire et la gouvernance de l'organisation via une interface dynamique et administrable. Il dispose d'un système d'administration complet permettant la mise à jour en temps réel des contenus de la page d'accueil, de la chronologie organisationnelle et des profils de l'équipe.

## Technologies
Le projet utilise la pile technique suivante :
- **Framework Principal** : Django 5.2
- **Base de Données** : SQLite3
- **Gestion des Médias** : Pillow (pour le traitement des images)
- **Frontend** : HTML5, Vanilla CSS3 (utilisation de variables CSS pour la gestion du thème) et JavaScript
- **Typographie** : Poppins (via Google Fonts)

## Structure des Fichiers
Le projet suit une architecture Django modulaire standard :

- **csgria_site/** : Contient les configurations au niveau du projet, les paramètres et le routage principal des URLs.
- **core/** : L'application principale gérant les fonctionnalités clés du site.
    - **models.py** : Définitions pour les Carrousels, Missions, sections À Propos, Événements (Chronologie), Profils (Gouvernance) et Informations de Contact.
    - **views.py** : Logique des vues pour les pages Accueil, À Propos et Contact.
    - **context_processors.py** : Fournisseur de contexte global pour les informations de contact sur l'ensemble du site.
- **actualite/** : Une application factice prévue pour les futures fonctionnalités de blog et d'actualités.
- **account/** : Une application factice prévue pour la future gestion des comptes utilisateurs et profils.
- **templates/** : Répertoire centralisé pour les modèles HTML utilisant le langage de gabarit Django (DTL).
- **static/** & **media/** : Répertoires pour la gestion des ressources statiques et des contenus téléchargés par les utilisateurs.

## Installation et Configuration

### Prérequis
- Python 3.12 ou supérieur
- pip (gestionnaire de paquets Python)

### Configuration de l'Environnement
1. Créer un environnement virtuel :
   ```bash
   python -m venv venv
   ```
2. Activer l'environnement virtuel :
   - Sur Windows : `.\venv\Scripts\activate`
   - Sur Linux/macOS : `source venv/bin/activate`

### Installation des Dépendances
Installez les paquets requis en utilisant le fichier requirements :
```bash
pip install -r requirements.txt
```

### Initialisation de la Base de Données
Lancez les migrations pour créer le schéma de la base de données :
```bash
python manage.py migrate
```

### Accès Administrateur
Créez un super-utilisateur pour accéder au panneau d'administration Django :
```bash
python manage.py createsuperuser
```

## Lancement du Projet
Pour démarrer le serveur de développement local :
```bash
python manage.py runserver
```
Une fois le serveur démarré, le site sera accessible sur http://127.0.0.1:8000/ et le panneau d'administration sur http://127.0.0.1:8000/admin/.

CSGR IA
