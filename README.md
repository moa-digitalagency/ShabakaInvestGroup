![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg) ![Framework](https://img.shields.io/badge/flask-3.0+-green.svg) ![Database](https://img.shields.io/badge/database-SQLAlchemy-orange.svg) ![Status](https://img.shields.io/badge/status-Private%2FInternal-red.svg) ![License](https://img.shields.io/badge/license-Proprietary-black.svg) ![Owner](https://img.shields.io/badge/owner-MOA%20Digital%20Agency-purple.svg)

[ 🇫🇷 Français ](README.md) | [ 🇬🇧 English ](README_en.md)

# Shabaka Invest Group - Plateforme de Domiciliation & Services

> **PROJET PRIVÉ & PROPRIÉTAIRE** - MOA Digital Agency (myoneart.com)
> Auteur : Aisance KALONJI.
> Usage strictement interne. Toute distribution interdite.

## Description
**Shabaka Invest Group** est une plateforme CMS sur-mesure développée pour gérer l'activité de domiciliation et de création d'entreprises au Maroc. Elle dispose d'une interface publique (Front-Office) optimisée pour la conversion et le SEO, et d'une interface d'administration (Back-Office) complète pour la gestion des contenus et des prospects.

## Architecture Technique

```mermaid
graph TD
    Client[Navigateur Client] -->|HTTP/HTTPS| Flask[App Flask]

    subgraph "Backend (Flask)"
        Flask -->|Route| Blueprints{Blueprints}
        Blueprints -->|/admin| AdminBP[Admin Blueprint]
        Blueprints -->|/| PublicBP[Public Blueprint]

        AdminBP -->|Logique| Services[Services Métier]
        PublicBP -->|Logique| Services

        Services -->|ORM| Models[Modèles SQLAlchemy]
    end

    Models -->|SQL| DB[(Base de Données)]

    subgraph "Frontend"
        Templates[Templates Jinja2]
        Tailwind[Tailwind CSS (CDN)]
    end

    PublicBP --> Templates
    AdminBP --> Templates
    Templates -.-> Client
```

## Table des Matières
1.  [Fonctionnalités Clés](#fonctionnalités-clés)
2.  [Installation & Démarrage](#installation--démarrage)
3.  [Documentation Détaillée](#documentation-détaillée)

## Fonctionnalités Clés
*   **CMS Dynamique :** Gestion complète des services, témoignages et projets.
*   **SEO Automatisé :** Génération de sitemap.xml, robots.txt et méta-données configurables par page.
*   **CRM Léger :** Centralisation des demandes de contact et suivi (lu/non lu).
*   **Médiathèque :** Gestion centralisée des uploads (images/documents).
*   **Sécurité :** Authentification forte, CSRF protection, assainissement des entrées.

## Installation & Démarrage

### Prérequis
*   Python 3.11 ou supérieur
*   pip (Gestionnaire de paquets)

### Installation
1.  Cloner le dépôt (accès restreint).
2.  Installer les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
3.  Configurer les variables d'environnement (voir `config.py`).

### Démarrage
1.  Initialiser la base de données :
    ```bash
    python init_db.py
    ```
2.  Lancer le serveur de développement :
    ```bash
    python main.py
    ```
    L'application sera accessible sur `http://localhost:5000`.

## Documentation Détaillée
Toute la documentation technique et fonctionnelle se trouve dans le dossier `docs/`.

*   📂 **[Bible des Fonctionnalités](docs/ShabakaInvest_features_full_list.md)** : Liste exhaustive de toutes les features.
*   🛠 **[Spécifications Techniques](docs/ShabakaInvest_technical_specs.md)** : Stack, Architecture, Sécurité.
*   📖 **[Guide Utilisateur](docs/ShabakaInvest_user_guide.md)** : Manuel pour l'administration du site.

---
Copyright © 2024 MOA Digital Agency. Tous droits réservés.
