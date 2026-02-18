![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg) ![Framework](https://img.shields.io/badge/flask-3.0+-green.svg) ![Database](https://img.shields.io/badge/database-SQLAlchemy-orange.svg) ![Status](https://img.shields.io/badge/status-Private%2FInternal-red.svg) ![License](https://img.shields.io/badge/license-Proprietary-black.svg) ![Owner](https://img.shields.io/badge/owner-MOA%20Digital%20Agency-purple.svg)

[ 🇫🇷 Français ](README.md) | [ 🇬🇧 English ](README_en.md)

# Shabaka Invest Group - Domiciliation & Services Platform

> **PRIVATE & PROPRIETARY PROJECT** - MOA Digital Agency (myoneart.com)
> Author: Aisance KALONJI.
> Strictly internal use only. Distribution prohibited.

## Description
**Shabaka Invest Group** is a custom-built CMS platform developed to manage business domiciliation and creation activities in Morocco. It features a public interface (Front-Office) optimized for conversion and SEO, and a comprehensive administration interface (Back-Office) for content and lead management.

## Technical Architecture

```mermaid
graph TD
    Client[Client Browser] -->|HTTP/HTTPS| Flask[Flask App]

    subgraph "Backend (Flask)"
        Flask -->|Route| Blueprints{Blueprints}
        Blueprints -->|/admin| AdminBP[Admin Blueprint]
        Blueprints -->|/| PublicBP[Public Blueprint]

        AdminBP -->|Logic| Services[Business Services]
        PublicBP -->|Logic| Services

        Services -->|ORM| Models[SQLAlchemy Models]
    end

    Models -->|SQL| DB[(Database)]

    subgraph "Frontend"
        Templates[Jinja2 Templates]
        Tailwind[Tailwind CSS (CDN)]
    end

    PublicBP --> Templates
    AdminBP --> Templates
    Templates -.-> Client
```

## Table of Contents
1.  [Key Features](#key-features)
2.  [Installation & Startup](#installation--startup)
3.  [Detailed Documentation](#detailed-documentation)

## Key Features
*   **Dynamic CMS:** Full management of services, testimonials, and projects.
*   **Automated SEO:** Generation of sitemap.xml, robots.txt, and configurable meta-data per page.
*   **Light CRM:** Centralization of contact requests and tracking (read/unread).
*   **Media Library:** Centralized management of uploads (images/documents).
*   **Security:** Strong authentication, CSRF protection, input sanitization.

## Installation & Startup

### Prerequisites
*   Python 3.11 or higher
*   pip (Package Manager)

### Installation
1.  Clone the repository (restricted access).
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure environment variables (see `config.py`).

### Startup
1.  Initialize the database:
    ```bash
    python init_db.py
    ```
2.  Launch the development server:
    ```bash
    python main.py
    ```
    The application will be accessible at `http://localhost:5000`.

## Detailed Documentation
All technical and functional documentation is located in the `docs/` folder.

*   📂 **[Features Bible](docs/ShabakaInvest_features_full_list_en.md)**: Exhaustive list of all features.
*   🛠 **[Technical Specifications](docs/ShabakaInvest_technical_specs_en.md)**: Stack, Architecture, Security.
*   📖 **[User Guide](docs/ShabakaInvest_user_guide_en.md)**: Manual for site administration.

---
Copyright © 2024 MOA Digital Agency. All rights reserved.
