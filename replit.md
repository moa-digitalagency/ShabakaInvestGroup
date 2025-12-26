# Shabaka Invest Group - Site Web

## Overview
Site web complet pour Shabaka Invest Group, une société de domiciliation et conseils d'entreprise basée à Marrakech.

## Tech Stack
- **Backend**: Python Flask
- **Database**: PostgreSQL
- **Frontend**: HTML, Tailwind CSS (via CDN), JavaScript
- **Authentication**: Flask-Login

## Project Structure
```
├── main.py                 # Point d'entrée Flask
├── templates/             # Templates HTML (public, admin)
├── static/                # Fichiers statiques (uploads, etc)
└── src/
    ├── modeles/           # Modèles SQLAlchemy
    ├── routes/            # Blueprints (public, admin)
    ├── services/          # Logique métier
    ├── security/          # Authentification
    └── utils/             # Utilitaires
```

## Features
1. **Pages publiques**: Accueil, Services, Domiciliation, Conseils, À Propos, Témoignages, Contact
2. **Admin Panel** (`/admin`): Gestion complète du contenu
   - Services (CRUD)
   - Témoignages
   - Messages de contact
   - SEO par page
   - Bibliothèque médias
   - Paramètres du site

## Couleurs & Design
- **Couleur primaire**: Bleu nuit (#0d1a5e à #5a6cff)
- **Design**: Responsive avec Tailwind CSS
- **Thème**: Moderne et professionnel

## Admin Access
- **URL**: `/admin`
- **Email**: admin@shabakainvest.com
- **Password**: admin123

## Services Proposés
- Domiciliation d'Entreprise
- Conseils aux Entreprises
- Gestion de Projet

## Recent Changes
- Suppression du service "Nettoyage de Chantier" de la base de données
- Changement des couleurs de orange vers bleu nuit
- Déplacement de templates/ et static/ à la racine
- src/ contient uniquement la logique applicative
