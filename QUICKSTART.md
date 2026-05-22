# Quick Start Guide - Deploy in 10 Minutes

## Prerequisites
- GitHub account (for code storage)
- PythonAnywhere account (free tier)
- Gmail account with 2FA enabled

---

## Step 1: Prepare Your Code (2 minutes)

### 1.1 Update Personal Info
Edit `templates/base.html`:
- Change `Jarvis` to your name
- Update social media URLs (LinkedIn, GitHub, Twitter)

Edit `templates/contact.html`:
- Update email and phone number

### 1.2 Add Your Assets
- Save profile photo → `static/images/profile.jpg`
- Save CV → `static/cv.pdf`

### 1.3 Add Your Projects
Visit `/admin` locally (password: test) and add 3-5 projects OR edit `static/projects.json`

---

## Step 2: Generate Secure Keys (1 minute)

Run these commands in terminal:

```bash
# Generate SECRET_KEY
python3 -c "import secrets; print(secrets.token_hex(32))"
# Copy the output!

# Generate ADMIN_PASSWORD
# Just come up with something like: MyPortfolio2024!@#
```

---

## Step 3: Get Gmail App Password (2 minutes)

1. Go to https://myaccount.google.com/security
2. Enable 2-Step Verification (if not already enabled)
3. Go to https://myaccount.google.com/apppasswords
4. Select Mail + your device
5. Copy the 16-character password

---

## Step 4: Push to GitHub (1 minute)

```bash
cd portfolio
git init
git add .
git commit -m "Initial portfolio"
git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
git push -u origin main
```

---

## Step 5: Deploy to PythonAnywhere (3 minutes)

### 5.1 Sign Up
- Go to https://www.pythonanywhere.com
- Sign up (free tier is fine)
- Log in to dashboard

### 5.2 Clone Your Repo
In PythonAnywhere console (click "Bash console"):

```bash
cd /home/YOUR_USERNAME
git clone https://github.com/YOUR_USERNAME/portfolio.git mysite
cd mysite
```

### 5.3 Create Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 mysite
workon mysite
pip install -r requirements.txt
```

### 5.4 Configure Web App

1. Click "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select "Python 3.10"

### 5.5 Update WSGI File

1. In Web tab, find WSGI configuration file
2. Click to edit `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`
3. Replace entire content:

```python
import os
import sys

# Set environment variables
os.environ['FLASK_ENV'] = 'production'
os.environ['SECRET_KEY'] = 'PASTE_YOUR_SECRET_KEY_HERE'
os.environ['ADMIN_PASSWORD'] = 'PASTE_YOUR_ADMIN_PASSWORD'
os.environ['GMAIL_EMAIL'] = 'your_email@gmail.com'
os.environ['GMAIL_APP_PASSWORD'] = 'PASTE_YOUR_16_CHAR_APP_PASSWORD'

# Add path
path = '/home/YOUR_USERNAME/mysite'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

Replace all caps values with YOUR values from Step 2 & 3.

### 5.6 Add Static Files

1. Still in Web tab
2. Scroll to "Static files"
3. Click "Add a new static files mapping"
4. URL: `/static/`
5. Directory: `/home/YOUR_USERNAME/mysite/static`
6. Save

### 5.7 Reload

1. Click green "Reload" button
2. Wait 10 seconds
3. Visit: `https://YOUR_USERNAME.pythonanywhere.com`

✅ **Done!** Your portfolio is live!

---

## Step 6: Update After First Deploy

Every time you make changes:

```bash
# Local
git add .
git commit -m "Update: description of changes"
git push origin main

# PythonAnywhere console
cd /home/YOUR_USERNAME/mysite
git pull origin main
touch /var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py
```

---

## Testing Your Site

Visit `https://YOUR_USERNAME.pythonanywhere.com` and test:

- [ ] Home page loads with your name
- [ ] Projects display correctly
- [ ] Contact form appears
- [ ] Admin login works (at `/admin`)
- [ ] Dark/light theme toggle works
- [ ] Mobile view looks good

---

## Troubleshooting

### 404 Error?
- Check WSGI file is correctly configured
- Verify file path in WSGI is correct

### 500 Error?
Check error log:
```bash
# PythonAnywhere console
tail -20 /var/log/YOUR_USERNAME.pythonanywhere.com.error.log
```

### Contact form not working?
- Verify `GMAIL_APP_PASSWORD` is correct (use app password, not main password)
- Check Gmail 2FA is enabled
- Check error log

### Static files not loading?
- Verify static files mapping is correct
- Check URL is `/static/` (with trailing slash)

---

## Next Steps

1. **Custom Domain** (Paid plan required):
   - Register domain
   - Point to PythonAnywhere
   - Update settings in Web tab

2. **Add More Projects**:
   - Visit `/admin`
   - Login with your admin password
   - Add projects

3. **Monitor Performance**:
   - Check CPU usage in dashboard
   - Upgrade to paid if needed

---

## Important Reminders

✅ **Do:**
- Keep SECRET_KEY secure
- Use Gmail App Password (not main password)
- Update code via Git
- Test locally before deploying
- Backup projects.json regularly

❌ **Don't:**
- Commit `.env` files
- Use weak passwords
- Share SECRET_KEY
- Modify WSGI file directly on PythonAnywhere (edit locally, push to Git)

---

## Full Documentation

For more detailed info, see:
- [README.md](README.md) - Overview and features
- [CONFIGURATION.md](CONFIGURATION.md) - Detailed configuration
- [PYTHONANYWHERE_GUIDE.md](PYTHONANYWHERE_GUIDE.md) - Deployment deep dive
- [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) - Complete checklist

---

**Congratulations!** Your Flask portfolio is now live on PythonAnywhere! 🚀
