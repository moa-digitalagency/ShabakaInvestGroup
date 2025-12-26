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
├── static/               # Fichiers statiques
├── modeles/              # Modèles SQLAlchemy
├── routes/               # Blueprints
├── services/             # Logique métier
├── security/             # Authentification
└── utils/                # Utilitaires
```

## Features
1. **Pages publiques**: Accueil, Services, À Propos, Contact
2. **Admin Panel** (`/admin`): Gestion complète

## Design
- **Couleur primaire**: Bleu nuit (#0d1a5e à #5a6cff)
- **Design**: Responsive Tailwind CSS
- **Police**: Poppins

## Sections Page d'Accueil
1. **Hero** - Full screen avec overlays multi-couches, centré
2. **À Propos** - Présentation avec checklist
3. **Solutions complètes** - 2 colonnes services
4. **Notre Processus** - 4 étapes
5. **Pourquoi nous choisir** - 3 avantages
6. **Nos Projets** - 6 projets avec URLs
7. **Témoignages** - Avis clients
8. **CTA** - Section contact
9. **Contact** - Formulaire

## Hero Section - Final Design
- **Hauteur**: 100% de l'écran (min-h-screen)
- **Layout**: Complètement centré en flex column
- **Concept**: Design épuré et premium
- **Éléments visibles**:
  - Badge "Transformez votre vision"
  - Titre 8xl centré avec gradient
  - Sous-titre clair et impactant
  - 3 stats horizontales (Entreprises, Expérience, Satisfaction)
  - 2 boutons d'action "Démarrer" et "Contacter"
  - Scroll indicator en bas
- **Overlays**: 5 couches (dégradés + effets radiaux + grain)
- **Animations**: Fade-in-up staggered + shimmer + bounce
- **Responsivité**: Complète mobile à desktop
