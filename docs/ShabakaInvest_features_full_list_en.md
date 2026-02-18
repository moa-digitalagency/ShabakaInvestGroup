[ 🇫🇷 Français ](ShabakaInvest_features_full_list.md) | [ 🇬🇧 English ](ShabakaInvest_features_full_list_en.md)

# Features Bible - Shabaka Invest Group

This document exhaustively lists all technical and business features implemented in the **Shabaka Invest Group** project. It serves as the absolute reference for developers and project managers.

---

## 1. Administration & Back-Office
The administration interface is secured and accessible via `/admin`.

### A. Dashboard (`/admin/`)
- **Real-time Statistics:** Number of services, testimonials, total and unread contacts.
- **Recent Activity:** Display of the last 5 contact messages received.
- **Side Navigation:** Quick access to all management modules.

### B. Service Management (CRUD)
- **List:** Tabular view with sorting capability (drag & drop via `order` field).
- **Create/Edit:**
  - Service Name.
  - Automatically generated slug (editable).
  - Short description (for cards) and long description (HTML allowed).
  - Icon (FontAwesome).
  - Cover Image (Upload with path management).
  - Feature list (bullet points).
  - Status: Active/Inactive, Featured.
- **Delete:** Irreversible action with confirmation.

### C. Testimonial Management
- **Fields:** Author Name, Company, Position, Photo, Content, Rating (1-5 stars).
- **Options:** Highlight on the homepage.

### D. Contact Management (Light CRM)
- **Reception:** Database storage of all form submissions.
- **Tracking:** Automatic "Read/Unread" marking upon opening.
- **Details:** Full view of the message, contact information, and service of interest.

### E. Global Configuration (`/admin/settings`)
- **Site Identity:** Name, Logo, Favicon.
- **Contact Info:** Email, Phone, Address, WhatsApp (support).
- **Social Networks:** Facebook, LinkedIn, Instagram, Twitter, YouTube links.
- **Third-party Scripts:** Injection of code into `<head>` and `<footer>` (Google Analytics, Pixel).

### F. Media Library
- **Upload:** Uploading of image/PDF files.
- **Organization:** Automatic categorization (services, testimonials, general).
- **Management:** Deletion of physical files and database entries.

### G. Advanced SEO Management (`/admin/seo`)
- **Per Page:** Configuration of meta-title, description, keywords for each page type (Home, Services, Contact, etc.).
- **Open Graph:** Title, Description, and Image for social sharing.
- **Robots & Canonical:** Fine-grained configuration per page.

---

## 2. Front-Office (Public)

### A. Dynamic Homepage
- **Hero Section:** Configurable title, subtitle, CTA, and background image.
- **Featured Services:** Automatic display of services marked as "Featured".
- **Testimonials:** Carousel of validated client reviews.
- **Metrics:** Display of key figures (Clients, Years, Satisfaction).

### B. Content Pages
- **Services:** Complete list and detail pages (`/services/<slug>`).
- **Static Pages:** About, Legal Notice.
- **Special Landing Pages:** Domiciliation, Consulting (with dedicated templates).

### C. Contact Form
- **Validation:** Mandatory fields (Name, Email, Message).
- **Feedback:** Flash messages (Success/Error).
- **Security:** Integrated CSRF protection.

### D. Technical Optimization (SEO)
- **XML Sitemap:** Dynamic generation at `/sitemap.xml` including all active service pages.
- **Robots.txt:** Dynamic generation at `/robots.txt` excluding admin and uploads.
- **Metadata:** Dynamic injection of titles/descriptions from the DB.

---

## 3. Security & Infrastructure

### A. Authentication
- **Framework:** Flask-Login.
- **User Model:** Management of administrators with secure password hashing.
- **Route Protection:** `@login_required` and `@admin_required` decorators on the entire back-office.

### B. Data Protection
- **CSRF:** Global protection via `Flask-WTF` on all POST forms.
- **Uploads:** Secure file renaming (UUID/Timestamp) to avoid collisions and malicious executions.
- **HTTP Headers:** Strict Cache-Control to prevent caching of admin pages.

### C. Database
- **ORM:** SQLAlchemy.
- **Migrations:** `init_db.py` script with introspection for schema updates without data loss.
- **Initialization:** Automatic seeding of default data if the database is empty.
