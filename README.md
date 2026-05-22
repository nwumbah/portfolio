# Flask Portfolio Website

A modern, responsive portfolio website built with Python Flask, designed for easy deployment to PythonAnywhere.

## Features

✨ **Modern Design**
- Responsive layout that works on all devices
- Dark/Light theme toggle
- Smooth animations and transitions
- Professional styling with CSS Grid and Flexbox

🎯 **Core Pages**
- **Home**: Hero section with profile photo, about, skills, and featured projects
- **Projects**: Detailed project showcase with modal popups
- **Contact**: Contact form with email integration
- **Admin Dashboard**: Add, edit, and delete projects without code changes

📧 **Email Integration**
- Contact form sends emails via Gmail
- Uses App Password for security
- Error handling and user feedback

🔐 **Admin Features**
- Password-protected admin panel
- Add projects dynamically
- Manage portfolio content from web interface
- Session-based authentication

---

## Project Structure

```
portfolio/
├── app.py                      # Main Flask application
├── wsgi.py                     # WSGI entry point for PythonAnywhere
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── PYTHONANYWHERE_GUIDE.md     # Complete deployment guide
├── DEPLOYMENT_CHECKLIST.md     # Pre-deployment checklist
├── README.md                   # This file
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with nav & footer
│   ├── index.html             # Home page
│   ├── projects.html          # Projects showcase
│   ├── contact.html           # Contact form page
│   ├── admin_login.html       # Admin login page
│   └── admin_dashboard.html   # Project management dashboard
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   ├── js/
│   │   ├── main.js            # Main JavaScript
│   │   └── theme.js           # Dark/Light theme toggle
│   ├── projects.json          # Projects data (auto-managed)
│   ├── images/
│   │   └── profile.jpg        # Your profile photo
│   ├── cv.pdf                 # Your CV (optional)
│   └── icons/                 # Optional: Custom icons
│
└── venv/                       # Virtual environment (created locally)
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Gmail account with 2-factor authentication

### Local Setup

1. **Clone or download the project**
   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file** (for local development)
   ```env
   ADMIN_PASSWORD=your_test_password
   SECRET_KEY=your_secret_key_here
   GMAIL_EMAIL=your_email@gmail.com
   GMAIL_APP_PASSWORD=your_16_char_app_password
   FLASK_ENV=development
   ```

5. **Run the application**
   ```bash
   python app.py
   ```
   
   Visit: `http://localhost:5000`

---

## Configuration

### Environment Variables

Set these environment variables (locally in `.env` or on PythonAnywhere):

| Variable | Description | Example |
|----------|-------------|---------|
| `ADMIN_PASSWORD` | Password for admin panel | `MySecurePass123!` |
| `SECRET_KEY` | Flask session secret key | Use `secrets.token_hex(32)` |
| `GMAIL_EMAIL` | Your Gmail address | `your_email@gmail.com` |
| `GMAIL_APP_PASSWORD` | Gmail App Password (16 chars) | From Google Account settings |
| `FLASK_ENV` | Environment mode | `development` or `production` |

### Customization

1. **Profile Information** - Edit `templates/base.html`:
   - Name and title
   - Social media links
   - Contact information

2. **Projects** - Either:
   - Edit `static/projects.json` directly, OR
   - Use the admin dashboard at `/admin`

3. **Styling** - Modify `static/css/style.css`:
   - Colors in `:root` CSS variables
   - Layout and typography
   - Responsive breakpoints

---

## Usage

### Adding Projects

**Method 1: Admin Dashboard**
1. Navigate to `/admin`
2. Enter your admin password
3. Fill in project details
4. Click "Add Project"

**Method 2: Direct JSON Edit**
1. Edit `static/projects.json`
2. Add project object:
   ```json
   {
       "title": "Project Name",
       "description": "Short description",
       "technologies": "Tech1, Tech2, Tech3",
       "details": "Longer details (optional)"
   }
   ```

### Contact Form

The contact form at `/contact` sends emails to your configured Gmail address. Requires:
- Gmail 2FA enabled
- App Password generated and set as environment variable

### Admin Panel

- **URL**: `/admin`
- **Features**: Add/delete projects, view all projects
- **Password**: Set via `ADMIN_PASSWORD` environment variable
- **Security**: Session-based, password protected

---

## Deployment to PythonAnywhere

### Quick Deploy (5 minutes)

1. **Sign up** at https://www.pythonanywhere.com (free tier available)

2. **In PythonAnywhere console**, run:
   ```bash
   cd /home/yourusername
   git clone https://github.com/yourusername/portfolio.git mysite
   cd mysite
   mkvirtualenv --python=/usr/bin/python3.10 mysite
   pip install -r requirements.txt
   ```

3. **Go to Web tab** and:
   - Add new web app → Manual configuration → Python 3.10
   - Point to WSGI file: `/var/www/yourusername_pythonanywhere_com_wsgi.py`
   - Update WSGI file content to import from your project

4. **Add static files mapping**:
   - URL: `/static/` → Directory: `/home/yourusername/mysite/static/`

5. **Reload** and visit your site!

**See [PYTHONANYWHERE_GUIDE.md](PYTHONANYWHERE_GUIDE.md) for detailed steps.**

---

## Troubleshooting

### Contact form not sending emails
- Verify Gmail App Password (not regular password)
- Confirm 2FA is enabled on Google account
- Check PythonAnywhere error log: `/var/log/yourusername.pythonanywhere.com.error.log`

### Static files not loading
- Verify static files mapping in PythonAnywhere Web settings
- Check file permissions: `chmod 755 static/`

### Admin panel not working
- Verify environment variables are set
- Check browser cookies are enabled
- Clear browser cache and try again

### "ModuleNotFoundError: No module named 'flask'"
- Activate virtual environment: `workon mysite`
- Reinstall: `pip install -r requirements.txt`
- Check virtualenv is selected in Web app settings

---

## Security Best Practices

✅ **Do This:**
- Use strong, unique admin password
- Generate secure SECRET_KEY using `secrets` module
- Use Gmail App Password (not main password)
- Enable 2FA on Gmail
- Keep dependencies updated
- Use HTTPS (automatic on PythonAnywhere)
- Don't commit `.env` files to Git

❌ **Don't Do This:**
- Hardcode passwords in code
- Use weak admin passwords
- Share SECRET_KEY or credentials
- Disable form validation
- Use old/unmaintained dependencies

---

## Performance Tips

1. **Optimize images**: Compress profile.jpg before uploading
2. **Cache static files**: Browser caches CSS/JS automatically
3. **Minimize JSON**: Keep projects.json size small
4. **Upgrade when needed**: Free tier may be slow with many visitors

---

## Upgrading to Paid Tier (Optional)

Benefits:
- More disk space (100GB vs 100MB)
- Custom domain support
- Higher CPU quotas
- Priority support

---

## Support & Resources

- 📚 **Flask Docs**: https://flask.palletsprojects.com
- 🚀 **PythonAnywhere**: https://help.pythonanywhere.com
- 🔧 **Python**: https://python.org
- 💬 **Issues**: Create an issue in your repository

---

## License

Feel free to use this template for your portfolio. Customize it as needed!

---

## Author

**IKU JARVIS NWUMBAH**
- System & Network Administrator
- Location: Limbe, Cameroon
- Email: jnwumbah@gmail.com

---

**Last Updated**: May 2026  
**Version**: 1.0
