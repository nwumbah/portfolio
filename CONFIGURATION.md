# Configuration Guide for Flask Portfolio

## Quick Configuration Reference

### 1. Generate SECRET_KEY

Run this command to generate a secure key:

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and use it for `SECRET_KEY`.

### 2. Gmail Setup (for Contact Form)

**Step 1: Enable 2-Factor Authentication**
1. Go to https://myaccount.google.com/security
2. Find "2-Step Verification"
3. Follow the setup wizard

**Step 2: Generate App Password**
1. Go to https://myaccount.google.com/apppasswords
2. Select Mail and your device type
3. Copy the 16-character password
4. This is your `GMAIL_APP_PASSWORD`

**Step 3: Set Environment Variables**
```bash
export GMAIL_EMAIL="your_email@gmail.com"
export GMAIL_APP_PASSWORD="1234567890123456"  # 16 characters
```

### 3. Admin Password

Choose a strong password for your admin panel:
- Mix uppercase, lowercase, numbers, symbols
- At least 12 characters long
- Something memorable but not easily guessed

```bash
export ADMIN_PASSWORD="MySecurePass123!@#"
```

### 4. Local Development Setup

Create a `.env` file in your project root:

```bash
cp .env.example .env
# Edit .env with your actual values
```

Load environment variables before running:

```bash
source .env
python3 app.py
```

### 5. PythonAnywhere Configuration

In PythonAnywhere, set environment variables in your WSGI file:

```python
import os

# At the top of wsgi.py
os.environ['FLASK_ENV'] = 'production'
os.environ['SECRET_KEY'] = 'your_secret_key_here'
os.environ['ADMIN_PASSWORD'] = 'your_admin_password_here'
os.environ['GMAIL_EMAIL'] = 'your_email@gmail.com'
os.environ['GMAIL_APP_PASSWORD'] = 'your_16_char_app_password'

import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

---

## CSS Customization

Edit `static/css/style.css` to customize colors:

```css
:root {
    --bg: #f8fafc;              /* Light mode background */
    --text: #1e2937;            /* Light mode text */
    --card: #ffffff;            /* Light mode card background */
    --accent: #2563eb;          /* Primary color (blue) */
}

[data-theme="dark"] {
    --bg: #0f172a;              /* Dark mode background */
    --text: #e2e8f0;            /* Dark mode text */
    --card: #1e2937;            /* Dark mode card background */
    --accent: #60a5fa;          /* Primary color (light blue) */
}
```

### Common Color Changes

1. **Change primary color** (blue to purple):
   - Light: `--accent: #a855f7;`
   - Dark: `--accent: #d8b4fe;`

2. **Change background** (lighter/darker):
   - Light: `--bg: #f5f7fa;` (lighter)
   - Dark: `--bg: #0a0f1f;` (darker)

---

## Content Customization

### Update Personal Information

Edit `templates/base.html`:

```html
<!-- Change the name in nav -->
<h2>Jarvis<span>.</span></h2>

<!-- Update social links -->
<a href="https://linkedin.com/in/YOUR_LINKEDIN" target="_blank">LinkedIn</a>
<a href="https://github.com/YOUR_GITHUB" target="_blank">GitHub</a>
<a href="https://twitter.com/YOUR_TWITTER" target="_blank">Twitter</a>

<!-- Update footer -->
<p>&copy; 2026 YOUR NAME. All Rights Reserved.</p>
```

Edit `templates/contact.html`:

```html
<!-- Update contact info -->
<p><i class="fas fa-envelope"></i> YOUR_EMAIL@gmail.com</p>
<p><i class="fas fa-phone"></i> +237 XXX XXX XXX</p>
<p><i class="fas fa-map-marker-alt"></i> YOUR_CITY, YOUR_COUNTRY</p>
```

### Add Your Profile Photo

1. Prepare a professional photo (square, 500x500px recommended)
2. Save as `static/images/profile.jpg`
3. The app will display it on the home page

### Add Your CV

1. Export your CV as PDF
2. Save as `static/cv.pdf`
3. Users can download it from the home page button

### Update Projects

**Option 1: Edit JSON directly**

Edit `static/projects.json`:

```json
[
    {
        "title": "Project Title",
        "description": "Brief 1-2 line description",
        "technologies": "Python, Flask, Linux",
        "details": "Longer description of what you did and your role"
    },
    {
        "title": "Another Project",
        "description": "What this project is about",
        "technologies": "JavaScript, React, Node.js",
        "details": "More details here"
    }
]
```

**Option 2: Use Admin Dashboard**

1. Visit `/admin`
2. Enter your admin password
3. Use the form to add/delete projects
4. Projects are saved to `projects.json` automatically

---

## Deployment Variables Checklist

Before deploying to PythonAnywhere, verify you have set:

- [ ] `FLASK_ENV` = `production`
- [ ] `SECRET_KEY` = generated secure key (32+ characters)
- [ ] `ADMIN_PASSWORD` = strong password (12+ characters)
- [ ] `GMAIL_EMAIL` = your email address
- [ ] `GMAIL_APP_PASSWORD` = 16-character app password from Google
- [ ] Static files mapped: `/static/` → `static/`
- [ ] WSGI file updated with correct paths
- [ ] All files uploaded to PythonAnywhere

---

## Testing Configuration

### Local Testing

1. Create `.env` with test values
2. Run: `python3 app.py`
3. Visit `http://localhost:5000`
4. Test all pages:
   - [ ] Home page displays
   - [ ] Projects load
   - [ ] Contact form appears
   - [ ] Theme toggle works
   - [ ] Admin login works with password
   - [ ] Admin can add/delete projects

### PythonAnywhere Testing

After deployment:
1. Visit your PythonAnywhere URL
2. Test all same pages as above
3. Try contact form (watch error log if it fails)
4. Login to admin and test project management

---

## Troubleshooting Configuration

| Issue | Solution |
|-------|----------|
| Contact form returns error | Check GMAIL_EMAIL and GMAIL_APP_PASSWORD are correct |
| Admin login rejects password | Verify ADMIN_PASSWORD environment variable |
| Static files not loading | Check static files mapping in PythonAnywhere |
| "KeyError" or "NoneType" error | Missing required environment variable |
| Theme toggle not working | Clear browser cache, check browser console |

---

## Security Checklist

- [ ] `ADMIN_PASSWORD` is strong (12+ chars, mixed case, numbers, symbols)
- [ ] `SECRET_KEY` is generated with `secrets` module
- [ ] `.env` file is in `.gitignore` (never commit credentials)
- [ ] `.env.example` shows structure but not real values
- [ ] Gmail 2FA is enabled
- [ ] Gmail App Password is used (not main password)
- [ ] HTTPS is enabled (automatic on PythonAnywhere)

---

## Support

If you encounter issues:

1. Check error logs: `tail /var/log/yourusername.pythonanywhere.com.error.log`
2. Review this configuration guide
3. See [PYTHONANYWHERE_GUIDE.md](PYTHONANYWHERE_GUIDE.md) for deployment help
4. Check [README.md](README.md) for general info
