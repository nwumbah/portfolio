# Flask Portfolio Website - Deployment Checklist

## Before Deployment

### 1. Security Configuration
- [ ] Update `ADMIN_PASSWORD` in environment variables to a strong password
  ```bash
  export ADMIN_PASSWORD="your_strong_secure_password_here"
  ```
- [ ] Generate and set `SECRET_KEY`:
  ```bash
  python3 -c "import secrets; print(secrets.token_hex(32))"
  export SECRET_KEY="<output_from_above>"
  ```
- [ ] Configure Gmail credentials:
  - [ ] Enable 2-factor authentication on Gmail
  - [ ] Generate App Password at https://myaccount.google.com/apppasswords
  - [ ] Set environment variables:
    ```bash
    export GMAIL_EMAIL="your_email@gmail.com"
    export GMAIL_APP_PASSWORD="16_character_password_here"
    ```

### 2. Content Setup
- [ ] Add professional profile photo to `static/images/profile.jpg`
- [ ] Add CV PDF to `static/cv.pdf`
- [ ] Update contact email and phone in `templates/base.html` and `templates/contact.html`
- [ ] Update social media links (LinkedIn, GitHub, Twitter) in `templates/base.html`
- [ ] Populate `static/projects.json` with your projects OR use admin dashboard to add them

### 3. File Structure Verification
- [ ] Ensure all files are in correct structure:
  ```
  ✓ app.py
  ✓ wsgi.py (required for PythonAnywhere)
  ✓ requirements.txt
  ✓ .gitignore
  ✓ templates/ folder with all HTML files
  ✓ static/css/style.css
  ✓ static/js/main.js
  ✓ static/js/theme.js (if exists)
  ✓ static/projects.json
  ✓ static/images/profile.jpg
  ✓ static/cv.pdf
  ```

### 4. Local Testing
- [ ] Create virtual environment: `python3 -m venv venv`
- [ ] Activate it: `source venv/bin/activate`
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Set environment variables locally (create `.env` file):
  ```
  ADMIN_PASSWORD=test_password
  SECRET_KEY=your_test_key
  GMAIL_EMAIL=your_email@gmail.com
  GMAIL_APP_PASSWORD=your_app_password
  FLASK_ENV=development
  ```
- [ ] Run locally: `python3 app.py`
- [ ] Test all pages:
  - [ ] Home page loads correctly
  - [ ] Projects display properly
  - [ ] Contact form works (or shows error if email not configured)
  - [ ] Admin login accessible at `/admin`
  - [ ] Admin can add/delete projects
- [ ] Test theme toggle (dark/light mode)
- [ ] Test responsive design on mobile

### 5. Git Setup
- [ ] Initialize git repository: `git init`
- [ ] Create `.gitignore` (already provided)
- [ ] Add files: `git add .`
- [ ] Create initial commit: `git commit -m "Initial portfolio commit"`
- [ ] Create GitHub repository
- [ ] Push to GitHub: `git remote add origin <your_repo_url>` → `git push -u origin main`

---

## PythonAnywhere Deployment Steps

### Step 1: Create Account
- [ ] Sign up at https://www.pythonanywhere.com (free tier)

### Step 2: Upload Code
**Option A: Using Git (Recommended)**
```bash
# In PythonAnywhere console
cd /home/yourusername
git clone https://github.com/yourusername/your-portfolio.git mysite
cd mysite
```

**Option B: Using Files Interface**
- [ ] Upload files via web interface

### Step 3: Setup Virtual Environment
```bash
# In PythonAnywhere console
mkvirtualenv --python=/usr/bin/python3.10 mysite
workon mysite
pip install -r requirements.txt
```

### Step 4: Configure Web App
- [ ] Go to Web tab → Add a new web app
- [ ] Choose "Manual configuration"
- [ ] Select Python 3.10 (or appropriate version)
- [ ] Update WSGI configuration file:
  - Path: `/var/www/yourusername_pythonanywhere_com_wsgi.py`
  - Content should point to `app.py` in your project directory

### Step 5: Set Environment Variables
Add to top of WSGI file or use PythonAnywhere environment settings:
```python
import os
os.environ['ADMIN_PASSWORD'] = 'your_password'
os.environ['SECRET_KEY'] = 'your_secret_key'
os.environ['GMAIL_EMAIL'] = 'your_email@gmail.com'
os.environ['GMAIL_APP_PASSWORD'] = 'your_app_password'
```

### Step 6: Configure Static Files
- [ ] Go to Web → Static files
- [ ] Add mapping:
  - URL: `/static/`
  - Directory: `/home/yourusername/mysite/static/`

### Step 7: Reload & Test
- [ ] Click "Reload" button
- [ ] Visit `https://yourusername.pythonanywhere.com`
- [ ] Test all functionality

---

## Post-Deployment

### Monitoring
- [ ] Check access logs: `tail -f /var/log/yourusername.pythonanywhere.com.access.log`
- [ ] Check error logs: `tail -f /var/log/yourusername.pythonanywhere.com.error.log`
- [ ] Monitor CPU usage in PythonAnywhere dashboard

### Maintenance
- [ ] Set up daily backups (download projects.json periodically)
- [ ] Monitor disk space usage
- [ ] Keep dependencies updated
- [ ] Review and test updates before deployment

### Domain Setup (Optional - Paid Only)
- [ ] Register custom domain
- [ ] Point domain to PythonAnywhere
- [ ] Configure HTTPS certificate

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 404 Not Found | Check WSGI file path and syntax in Web settings |
| 500 Internal Error | Check error log, verify environment variables |
| Static files not loading | Verify static files mapping in Web settings |
| Contact form not sending | Verify Gmail credentials and 2FA/App Password |
| "Permission denied" | Check file permissions, ensure proper ownership |
| Slow loading | Upgrade to paid tier or optimize code |

---

## Quick Update Procedure

After making changes locally:
```bash
# Push changes to GitHub
git add .
git commit -m "Update: description"
git push origin main

# In PythonAnywhere console
cd /home/yourusername/mysite
git pull origin main
touch /var/www/yourusername_pythonanywhere_com_wsgi.py
```

---

## Support Resources

- **PythonAnywhere Help**: https://help.pythonanywhere.com
- **Flask Documentation**: https://flask.palletsprojects.com
- **Werkzeug (Flask server)**: https://werkzeug.palletsprojects.com
- **Gmail App Passwords**: https://myaccount.google.com/apppasswords
