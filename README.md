# Shabaka Invest Group - Plateforme Digitale

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-orange.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)]()

> **Shabaka Invest Group** est une plateforme moderne de gestion de services d'investissement et de domiciliation d'entreprises à Marrakech. Ce projet combine une vitrine commerciale haut de gamme avec un CMS complet pour une autonomie totale des équipes.

---

## 📖 Table des Matières
- [Aperçu](#-aperçu)
- [Fonctionnalités Clés](#-fonctionnalités-clés)
- [Stack Technique](#-stack-technique)
- [Démarrage Rapide](#-démarrage-rapide)
- [Documentation Complète](#-documentation-complète)
- [Structure du Projet](#-structure-du-projet)

---

## 🚀 Aperçu

Cette application web sur mesure permet à **Shabaka Invest Group** de présenter ses services (domiciliation, création d'entreprise, conseil) et de capter des leads qualifiés via des formulaires intelligents et une intégration WhatsApp directe. L'interface d'administration offre un contrôle total sur le contenu sans nécessiter d'intervention technique.

---

## ✨ Fonctionnalités Clés

*   **Interface Publique Dynamique :** Hero section configurable, catalogue de services, témoignages clients.
*   **CMS Intégré (Admin Panel) :**
    *   Gestion complète des Services, Projets et Témoignages.
    *   Upload et gestion des Médias (Images/Docs).
    *   Configuration SEO avancée par page (Meta tags, Open Graph).
*   **Lead Generation :**
    *   Formulaire de contact avec notification admin.
    *   Génération de liens WhatsApp pré-remplis pour les devis.
*   **Performance & SEO :**
    *   Génération automatique de Sitemap XML et Robots.txt.
    *   Architecture optimisée pour le chargement rapide.

> 👉 **[Voir la liste exhaustive des fonctionnalités](docs/ShabakaInvest_features_full_list.md)**

---

## 🛠 Stack Technique

Ce projet repose sur une architecture robuste et maintenable :

| Composant | Technologie |
|---|---|
| **Backend** | Python 3, Flask, SQLAlchemy |
| **Frontend** | Jinja2, Tailwind CSS (CDN), AlpineJS/Vanilla JS |
| **Base de Données** | PostgreSQL (Prod) / SQLite (Dev) |
| **Sécurité** | Flask-Login, CSRF Protection, Password Hashing |
| **Déploiement** | Gunicorn, Nginx, Docker Ready |

> 👉 **[Voir l'architecture technique détaillée](docs/ShabakaInvest_technical_architecture.md)**

---

## ⚡ Démarrage Rapide

### Prérequis
*   Python 3.10+
*   pip / venv

### Installation

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/votre-org/shabaka-invest.git
    cd shabaka-invest
    ```

2.  **Configurer l'environnement virtuel :**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialiser la base de données :**
    ```bash
    python init_db.py
    ```

5.  **Lancer le serveur de développement :**
    ```bash
    python main.py
    ```
    Accédez au site sur `http://localhost:5000`

> 👉 **[Guide de déploiement complet](docs/ShabakaInvest_deployment.md)**

---

## 📚 Documentation Complète

Toute la documentation technique et utilisateur se trouve dans le dossier [`docs/`](docs/).

*   📄 **[Bible des Fonctionnalités](docs/ShabakaInvest_features_full_list.md)** : Détail exhaustif de chaque feature.
*   🏗 **[Architecture Technique](docs/ShabakaInvest_technical_architecture.md)** : Modèles de données, sécurité, structure.
*   📘 **[Guide Utilisateur (Admin)](docs/ShabakaInvest_user_guide.md)** : Manuel pour les gestionnaires de contenu.
*   🚀 **[Guide de Déploiement](docs/ShabakaInvest_deployment.md)** : Installation serveur et configuration env.

---

## 📂 Structure du Projet

```bash
/
├── docs/                # Documentation (markdown)
├── modeles/             # Modèles de base de données (SQLAlchemy)
├── routes/              # Contrôleurs (Admin & Public)
├── services/            # Logique métier
├── static/              # Assets (CSS, JS, Uploads)
├── templates/           # Vues HTML (Jinja2)
├── main.py              # Point d'entrée Flask
└── requirements.txt     # Dépendances
```

---

© 2025 Shabaka Invest Group. Tous droits réservés.
