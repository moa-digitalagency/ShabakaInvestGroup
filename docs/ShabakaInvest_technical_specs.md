[ 🇫🇷 Français ](ShabakaInvest_technical_specs.md) | [ 🇬🇧 English ](ShabakaInvest_technical_specs_en.md)

# Spécifications Techniques - Shabaka Invest Group

Ce document détaille l'architecture technique, la structure de la base de données et les protocoles de sécurité du projet **Shabaka Invest Group**.

---

## 1. Architecture Globale
Le projet suit une architecture **MVC (Modèle-Vue-Contrôleur)** implémentée via le framework Flask.
L'application est modulaire, utilisant des **Blueprints** pour séparer les responsabilités :
- `routes/public.py` : Gestion du front-office (pages vitrines, formulaires).
- `routes/admin.py` : Gestion du back-office (CRUD, settings).
- `routes/errors.py` : Gestion centralisée des erreurs (404, 500).

## 2. Stack Technique

### Backend
- **Langage :** Python 3.11+
- **Framework :** Flask 3.0+
- **ORM :** SQLAlchemy 2.0+ (avec Flask-SQLAlchemy)
- **Authentification :** Flask-Login
- **Formulaires :** Flask-WTF

### Frontend
- **Moteur de Template :** Jinja2 (Rendu côté serveur)
- **CSS Framework :** Tailwind CSS (via CDN pour rapidité et simplicité)
- **Icônes :** FontAwesome (via CDN)
- **JavaScript :** Vanilla JS (pas de framework lourd type React/Vue).

### Base de Données
- **SGBD :** Compatible SQLite (Dév) et PostgreSQL (Prod via `DATABASE_URL`).
- **Migrations :** Script `init_db.py` utilisant `sqlalchemy.inspect` pour la détection de changements de schéma.

---

## 3. Schéma de Base de Données (Modèles)

Les modèles sont définis dans `modeles/__init__.py`.

| Modèle | Table SQL | Description |
| :--- | :--- | :--- |
| **User** | `users` | Administrateurs (email, password_hash, role). |
| **Service** | `services` | Services offerts (nom, slug, description, image, features). |
| **Testimonial** | `testimonials` | Avis clients (auteur, contenu, note, photo). |
| **ContactSubmission** | `contact_submissions` | Messages reçus via le formulaire de contact. |
| **SiteSettings** | `site_settings` | Configuration globale (logo, email, réseaux sociaux). |
| **SEOSettings** | `seo_settings` | Méta-données par type de page (titre, description, OG). |
| **MediaAsset** | `media_assets` | Fichiers uploadés (images, documents). |
| **HeroSettings** | `hero_settings` | Configuration de la section Hero (Home). |
| **Project** | `projects` | Portfolio / Réalisations. |

---

## 4. Sécurité

### Authentification & Session
- Utilisation de `Flask-Login` pour la gestion de session sécurisée.
- Mots de passe hashés avec `Werkzeug.security` (PBKDF2/SHA256).
- Protection des routes admin via le décorateur `@login_required` et vérification de rôle.

### Protection CSRF
- `Flask-WTF` injecte automatiquement un token CSRF dans tous les formulaires.
- Validation stricte côté serveur avant tout traitement de données POST.

### Gestion des Fichiers (Uploads)
- Les noms de fichiers sont assainis via `werkzeug.utils.secure_filename`.
- Stockage dans `static/uploads/` avec sous-dossiers par catégorie.
- Vérification des extensions autorisées (images, pdf).

### En-têtes HTTP
- Configuration de `Cache-Control: no-store` pour les pages admin afin d'éviter la mise en cache par les navigateurs.

---

## 5. Déploiement & Environnement

Le projet nécessite les variables d'environnement suivantes dans `.env` ou la configuration système :

```bash
DATABASE_URL=sqlite:///instance/shabaka.db  # Ou URL PostgreSQL
SESSION_SECRET=votre_cle_secrete_longue
ADMIN_USERNAME=admin
ADMIN_MAIL=admin@shabakainvest.com
ADMIN_PASSWORD=motdepassesecurise
```

### Script de Démarrage
Le fichier `main.py` initialise l'application, la base de données, et lance le serveur de développement.
En production, utiliser un serveur WSGI comme **Gunicorn**.
