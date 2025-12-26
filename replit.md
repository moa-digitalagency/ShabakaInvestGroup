# Shabaka Invest Group - Site Web

## Overview
Site web complet pour Shabaka Invest Group, une société de domiciliation, création et gestion d'entreprises basée à Marrakech. Accompagne les entrepreneurs, investisseurs et dirigeants au Maroc.

## Tech Stack
- **Backend**: Python Flask
- **Database**: PostgreSQL
- **Frontend**: HTML, Tailwind CSS (via CDN), JavaScript
- **Authentication**: Flask-Login

## Project Structure
```
├── main.py                # Point d'entrée Flask
├── templates/            # Templates HTML (public, admin)
├── static/               # Fichiers statiques (uploads, etc)
├── modeles/              # Modèles SQLAlchemy
├── routes/               # Blueprints (public, admin)
├── services/             # Logique métier
├── security/             # Authentification
└── utils/                # Utilitaires
```

## Features
1. **Pages publiques**: Accueil, Services, À Propos, Contact
2. **Admin Panel** (`/admin`): Gestion complète du contenu
   - Services (CRUD)
   - Témoignages
   - Messages de contact
   - SEO par page

## Design & Couleurs
- **Couleur primaire**: Bleu nuit (#0d1a5e à #5a6cff)
- **Design**: Responsive avec Tailwind CSS
- **Thème**: Moderne et professionnel
- **Police**: Poppins

## Navigation
- Accueil
- Services
- À Propos
- Contact

## Services Proposés
1. Domiciliation d'Entreprise
2. Création & Gestion d'Entreprises
3. Conseil Stratégique & Business Development
4. Communication & Image Professionnelle

## Projets Accompagnés
1. Syndic Shabaka (syndic.shabaka.site)
2. Villa à Vendre Marrakech (villaavendremarrakech.com)
3. Capsule Shabaka (capsule.shabaka.site)
4. AdScreen Shabaka (www.adscreen.shabaka.site)
5. Bellari Propreté Services (www.bellaripropreteservices.com)
6. Bellari Concept (bellariconcept.com)

## Sections de la Page d'Accueil
1. **Hero** - 2 colonnes avec texte à gauche et image à droite + 3 statistiques
2. **À Propos** - Présentation et checklist
3. **Services** - 2 colonnes pour 4 services
4. **Notre Processus** - 4 étapes (Consultation, Analyse, Exécution, Suivi)
5. **Pourquoi nous choisir** - 3 avantages (Support 24/7, Rapidité, Sécurité)
6. **Nos Projets** - 6 projets accompagnés avec liens externes
7. **Témoignages** - Avis clients
8. **Appel à l'action** - Section CTA bleu nuit
9. **Contact** - Formulaire de contact
10. **Blog** - Articles et ressources

## Recent Changes (26 Dec 2025)
- Refonte complète du design avec style moderne
- Hero redesigné avec 2 colonnes (texte + image) et 3 stats
- Section Services changée en 2 colonnes avec descriptions
- Ajout section "Notre Processus" avec 4 étapes numérotées
- Ajout section "Pourquoi nous choisir" (Support, Rapidité, Sécurité)
- Section projets avec 6 URLs réelles
- Traits inclinés, badges de section, cartes avec bordures
- Tous les boutons en style pill (arrondi complet)
