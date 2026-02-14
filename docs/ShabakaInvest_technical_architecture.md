# Shabaka Invest Group - Technical Architecture

Ce document décrit l'architecture technique, la stack technologique, le schéma de base de données et les mesures de sécurité mises en place pour la plateforme Shabaka Invest Group.

## 1. Stack Technologique

Le projet repose sur une architecture MVC (Modèle-Vue-Contrôleur) classique utilisant le framework Flask.

### Backend
*   **Langage :** Python 3.10+
*   **Framework Web :** Flask 2.x
*   **ORM :** SQLAlchemy (via `Flask-SQLAlchemy`)
*   **Authentification :** `Flask-Login` (gestion des sessions utilisateur)
*   **Formulaires & Sécurité :** `Flask-WTF` (protection CSRF)
*   **Hachage de Mots de Passe :** `werkzeug.security` (Argon2 / PBKDF2)
*   **Serveur WSGI :** Gunicorn (recommandé pour la production)

### Frontend
*   **Moteur de Template :** Jinja2 (intégré à Flask)
*   **Framework CSS :** Tailwind CSS (v3 via CDN)
*   **Icônes :** FontAwesome 6 (CDN)
*   **Polices :** Google Fonts (Poppins)
*   **Scripts :** Vanilla JavaScript (pas de framework lourd type React/Vue)

### Base de Données
*   **Développement :** SQLite (`instance/site.db`)
*   **Production :** PostgreSQL (via `DATABASE_URL`)

---

## 2. Structure du Projet

L'application est structurée de manière modulaire avec des Blueprints pour séparer la logique publique de l'administration.

```
/
├── modeles/                 # Définitions des modèles de base de données (SQLAlchemy)
│   ├── __init__.py          # Initialisation de db et des modèles (User, Service, etc.)
├── routes/                  # Contrôleurs (Blueprints)
│   ├── admin.py             # Routes de l'interface d'administration (/admin/*)
│   ├── public.py            # Routes du site public (/, /services, /contact)
├── services/                # Logique métier (Service Layer)
│   ├── __init__.py          # Services encapsulés (ContactService, SettingsService...)
├── static/                  # Fichiers statiques
│   ├── uploads/             # Fichiers uploadés par l'utilisateur (images, docs)
│   ├── css/                 # Styles personnalisés (si nécessaire)
│   ├── js/                  # Scripts JS (si nécessaire)
├── templates/               # Vues (Templates Jinja2)
│   ├── admin/               # Templates de l'interface admin
│   ├── public/              # Templates du site public
│   ├── base.html            # Layout principal public
│   ├── base_admin.html      # Layout principal admin
├── utils/                   # Fonctions utilitaires
│   ├── __init__.py          # Helpers (slugify, save_uploaded_file)
├── main.py                  # Point d'entrée de l'application (création de l'app Flask)
├── init_db.py               # Script de migration/initialisation de la BDD
├── requirements.txt         # Dépendances Python
└── README.md                # Documentation racine
```

---

## 3. Schéma de Base de Données (Modèles)

Les modèles sont définis dans `modeles/__init__.py`.

### Utilisateurs (`User`)
Table : `users`
| Champ | Type | Description |
|---|---|---|
| `id` | Integer (PK) | Identifiant unique |
| `email` | String(120) | Email de connexion (Unique) |
| `password_hash` | String(256) | Mot de passe haché |
| `name` | String(100) | Nom de l'administrateur |
| `role` | String(20) | Rôle (défaut: 'admin') |
| `last_login` | DateTime | Dernière connexion |

### Contenu : Services (`Service`)
Table : `services`
| Champ | Type | Description |
|---|---|---|
| `id` | Integer (PK) | Identifiant unique |
| `name` | String(150) | Nom du service |
| `slug` | String(100) | URL friendly (Unique) |
| `short_description` | String(300)| Résumé pour les cartes |
| `description` | Text | Contenu riche |
| `icon` | String(50) | Classe FontAwesome |
| `image` | String(500) | Chemin de l'image |
| `features` | Text | Liste de fonctionnalités (JSON/Texte) |
| `is_featured` | Boolean | Afficher sur l'accueil |
| `order` | Integer | Ordre d'affichage |
| `is_active` | Boolean | Publié ou brouillon |

### Contenu : Pages & SEO (`Page`, `SEOSettings`)
Table : `pages`, `seo_settings`
Relation One-to-One. Permet de stocker le contenu des pages statiques et leurs métadonnées SEO.

### Contenu : Témoignages (`Testimonial`)
Table : `testimonials`
Stocke les avis clients avec note, auteur, entreprise et statut de publication.

### CRM : Contacts (`ContactSubmission`)
Table : `contact_submissions`
| Champ | Type | Description |
|---|---|---|
| `id` | Integer (PK) | Identifiant unique |
| `name` | String(100) | Nom du prospect |
| `email` | String(120) | Email de contact |
| `message` | Text | Contenu du message |
| `is_read` | Boolean | Statut de lecture (Lu/Non lu) |
| `created_at` | DateTime | Date de réception |

### Configuration : Paramètres (`SiteSettings`, `HeroSettings`)
Table : `site_settings`, `hero_settings`
Ces tables "Singleton" (une seule ligne attendue) stockent la configuration globale du site (logo, réseaux sociaux, titre du Hero, etc.) pour éviter de coder en dur.

---

## 4. Sécurité

L'application implémente plusieurs couches de sécurité standard.

### 4.1 Authentification
*   Utilisation de `Flask-Login` pour la gestion de la session utilisateur.
*   Protection des routes `/admin` via le décorateur `@login_required` et `@admin_required`.
*   Les mots de passe ne sont **jamais** stockés en clair.

### 4.2 Protection CSRF (Cross-Site Request Forgery)
*   `Flask-WTF` génère un jeton CSRF unique pour chaque session.
*   Ce jeton est injecté dans tous les formulaires (`<input type="hidden" name="csrf_token" ...>`).
*   Toute requête POST sans jeton valide est rejetée (400 Bad Request).

### 4.3 Upload de Fichiers
*   Les noms de fichiers uploadés sont "nettoyés" via `werkzeug.utils.secure_filename` pour empêcher l'exécution de code malveillant ou la traversée de répertoire.
*   Les fichiers sont stockés dans un répertoire statique public, mais ne sont pas exécutables par le serveur web.

### 4.4 En-têtes HTTP
*   Les réponses incluent des en-têtes de sécurité de base.
*   `Cache-Control` est configuré pour éviter la mise en cache des pages d'administration sensibles.

---

## 5. Déploiement & Environnement

L'application est conçue pour être "Cloud Native" (12-Factor App).
*   **Configuration :** Toutes les données sensibles (clés secrètes, credentials BDD) sont injectées via des variables d'environnement.
*   **Persistance :** Les uploads doivent être stockés sur un volume persistant ou un service S3 en production (actuellement sur système de fichiers local).
*   **Base de Données :** Compatible avec toute base de données supportée par SQLAlchemy (PostgreSQL recommandé en prod).
