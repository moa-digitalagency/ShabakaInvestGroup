[ 🇫🇷 Français ](ShabakaInvest_technical_specs.md) | [ 🇬🇧 English ](ShabakaInvest_technical_specs_en.md)

# Technical Specifications - Shabaka Invest Group

This document details the technical architecture, database structure, and security protocols of the **Shabaka Invest Group** project.

---

## 1. Global Architecture
The project follows an **MVC (Model-View-Controller)** architecture implemented via the Flask framework.
The application is modular, using **Blueprints** to separate responsibilities:
- `routes/public.py`: Front-office management (showcase pages, forms).
- `routes/admin.py`: Back-office management (CRUD, settings).
- `routes/errors.py`: Centralized error management (404, 500).

## 2. Tech Stack

### Backend
- **Language:** Python 3.11+
- **Framework:** Flask 3.0+
- **ORM:** SQLAlchemy 2.0+ (with Flask-SQLAlchemy)
- **Authentication:** Flask-Login
- **Forms:** Flask-WTF

### Frontend
- **Template Engine:** Jinja2 (Server-side rendering)
- **CSS Framework:** Tailwind CSS (via CDN for speed and simplicity)
- **Icons:** FontAwesome (via CDN)
- **JavaScript:** Vanilla JS (no heavy framework like React/Vue).

### Database
- **DBMS:** Compatible with SQLite (Dev) and PostgreSQL (Prod via `DATABASE_URL`).
- **Migrations:** `init_db.py` script using `sqlalchemy.inspect` for schema change detection.

---

## 3. Database Schema (Models)

Models are defined in `modeles/__init__.py`.

| Model | SQL Table | Description |
| :--- | :--- | :--- |
| **User** | `users` | Administrators (email, password_hash, role). |
| **Service** | `services` | Offered services (name, slug, description, image, features). |
| **Testimonial** | `testimonials` | Client reviews (author, content, rating, photo). |
| **ContactSubmission** | `contact_submissions` | Messages received via the contact form. |
| **SiteSettings** | `site_settings` | Global configuration (logo, email, social networks). |
| **SEOSettings** | `seo_settings` | Meta-data per page type (title, description, OG). |
| **MediaAsset** | `media_assets` | Uploaded files (images, documents). |
| **HeroSettings** | `hero_settings` | Hero section configuration (Home). |
| **Project** | `projects` | Portfolio / Achievements. |

---

## 4. Security

### Authentication & Session
- Use of `Flask-Login` for secure session management.
- Passwords hashed with `Werkzeug.security` (PBKDF2/SHA256).
- Admin route protection via `@login_required` decorator and role verification.

### CSRF Protection
- `Flask-WTF` automatically injects a CSRF token into all forms.
- Strict server-side validation before any POST data processing.

### File Management (Uploads)
- Filenames are sanitized via `werkzeug.utils.secure_filename`.
- Storage in `static/uploads/` with subfolders per category.
- Verification of allowed extensions (images, pdf).

### HTTP Headers
- Configuration of `Cache-Control: no-store` for admin pages to prevent browser caching.

---

## 5. Deployment & Environment

The project requires the following environment variables in `.env` or system configuration:

```bash
DATABASE_URL=sqlite:///instance/shabaka.db  # Or PostgreSQL URL
SESSION_SECRET=your_long_secret_key
ADMIN_USERNAME=admin
ADMIN_MAIL=admin@shabakainvest.com
ADMIN_PASSWORD=securepassword
```

### Startup Script
The `main.py` file initializes the application, the database, and launches the development server.
In production, use a WSGI server like **Gunicorn**.
