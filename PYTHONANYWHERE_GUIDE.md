# PythonAnywhere Deployment Guide for Flask Portfolio

## Quick Start: Deploying to PythonAnywhere

### Step 1: Create PythonAnywhere Account
1. Go to https://www.pythonanywhere.com and sign up for a free account
2. Free tier includes: 100MB disk space, 1 web app, CPU quota

### Step 2: Upload Your Code
1. Log in to PythonAnywhere dashboard
2. Go to "Files" section
3. Create a directory structure like: `/home/yourusername/mysite/`
4. Upload all files from your portfolio to that directory

**Alternative (Recommended): Use Git**
```bash
# In PythonAnywhere console ($ prompt):
cd /home/yourusername
git clone https://github.com/yourusername/your-portfolio.git mysite
cd mysite
```

### Step 3: Create Virtual Environment
1. Go to "Web" section → "Add a new web app"
2. Select "Manual configuration" → Python version (3.10+)
3. In PythonAnywhere console:
```bash
mkvirtualenv --python=/usr/bin/python3.10 mysite
workon mysite
pip install -r requirements.txt
```

### Step 4: Configure WSGI File
1. In "Web" app settings, find "WSGI configuration file"
2. Edit it and replace the content with:

```python
import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

### Step 5: Set Environment Variables
1. Go to "Web" → "Your web app" → Scroll to "WSGI configuration file"
2. At the top of wsgi.py, add environment variables OR
3. Create `.env` file in your project and load it in app.py:

```python
# app.py - add this near the top after imports
from dotenv import load_dotenv
load_dotenv()
```

Then set these in PythonAnywhere console:
```bash
export ADMIN_PASSWORD="your_strong_password"
export SECRET_KEY="your_secret_key_here"
export GMAIL_EMAIL="your_email@gmail.com"
export GMAIL_APP_PASSWORD="your_16_char_app_password"
```

### Step 6: Configure Web App
1. In PythonAnywhere "Web" section:
   - Source code: `/home/yourusername/mysite`
   - WSGI file: `/home/yourusername/mysite/wsgi.py`
   - Virtualenv: `/home/yourusername/.virtualenvs/mysite`

### Step 7: Reload Web App
1. Click the green "Reload" button to restart the app
2. Visit your URL: `https://yourusername.pythonanywhere.com`

### Step 8: Configure Gmail (for Contact Form)
1. Use Gmail App Password (NOT your regular password)
2. Steps to create App Password:
   - Enable 2-factor authentication on your Google account
   - Go to https://myaccount.google.com/apppasswords
   - Select Mail and Windows Computer (or your device)
   - Copy the 16-character password
   - Set as `GMAIL_APP_PASSWORD` environment variable

---

## File Structure Required for PythonAnywhere

```
/home/yourusername/mysite/
├── wsgi.py                 # ← REQUIRED for PythonAnywhere
├── app.py
├── requirements.txt
├── .gitignore
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── main.js
│   │   └── theme.js
│   ├── images/
│   │   └── profile.jpg
│   ├── projects.json
│   └── cv.pdf
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── projects.html
│   ├── contact.html
│   ├── admin_login.html
│   └── admin_dashboard.html
└── venv/                   # Virtual environment (created on PythonAnywhere)
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure you:
1. Activated the virtual environment: `workon mysite`
2. Installed requirements: `pip install -r requirements.txt`
3. Selected correct virtualenv in Web app settings

### Issue: "400 Bad Request" or "500 Internal Server Error"
**Solution:** Check error logs:
```bash
# PythonAnywhere console
tail -20 /var/log/yourusername.pythonanywhere.com.error.log
tail -20 /var/log/yourusername.pythonanywhere.com.access.log
```

### Issue: Contact form not sending emails
**Solution:**
1. Verify Gmail credentials are correct
2. Check that 2FA is enabled and App Password is generated
3. Verify environment variables are set in the WSGI file
4. Check error log for email errors

### Issue: Static files not loading
**Solution:** In Web app settings, add Static files mapping:
- URL: `/static/`
- Directory: `/home/yourusername/mysite/static/`

---

## Security Checklist
- [ ] Change `ADMIN_PASSWORD` to something strong
- [ ] Set unique `SECRET_KEY` using `python -c "import secrets; print(secrets.token_hex(32))"`
- [ ] Use Gmail App Password, NOT your main Google password
- [ ] Enable HTTPS (automatic on PythonAnywhere)
- [ ] Keep requirements.txt updated
- [ ] Don't commit sensitive credentials to Git

---

## Free Tier Limitations
- 100MB disk space
- CPU quota (usually sufficient for light usage)
- 1 web app
- No direct SSH access (use console instead)

**Upgrade for:**
- More disk space (100GB on paid plans)
- Multiple web apps
- Custom domain (e.g., yourname.com instead of username.pythonanywhere.com)
- Premium support

---

## Updating Your Code
After making changes locally:

```bash
# Push to GitHub
git add .
git commit -m "Update: description of changes"
git push origin main

# In PythonAnywhere console
cd /home/yourusername/mysite
git pull origin main
workon mysite
pip install -r requirements.txt
touch /var/www/yourusername_pythonanywhere_com_wsgi.py  # Trigger reload
```

---

**Need Help?**
- PythonAnywhere Documentation: https://help.pythonanywhere.com
- Flask Documentation: https://flask.palletsprojects.com
- GitHub Issues: Create an issue in your repository
