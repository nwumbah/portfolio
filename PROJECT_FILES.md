# Project File Structure & Guide

## 📁 Complete Project Structure

```
portfolio/
│
├── 📄 Core Application Files
│   ├── app.py                      # Main Flask application with all routes
│   ├── wsgi.py                     # WSGI entry point for PythonAnywhere ⭐ REQUIRED
│   └── requirements.txt            # Python dependencies (Flask, gunicorn)
│
├── 📚 Documentation Files (Start Here!)
│   ├── README.md                   # Project overview and features
│   ├── QUICKSTART.md               # Deploy in 10 minutes! ⭐ START HERE
│   ├── PYTHONANYWHERE_GUIDE.md    # Detailed deployment guide
│   ├── DEPLOYMENT_CHECKLIST.md    # Pre-deployment checklist
│   ├── CONFIGURATION.md            # Configuration reference
│   └── PROJECT_FILES.md            # This file - overview of all files
│
├── ⚙️ Configuration Files
│   ├── .gitignore                  # Git ignore rules (keep secrets safe!)
│   └── .env.example                # Template for environment variables
│
├── 🎨 Templates (HTML Pages)
│   ├── templates/
│   │   ├── base.html               # Base template (nav, footer, layout)
│   │   ├── index.html              # Home page (hero, about, skills, projects)
│   │   ├── projects.html           # Projects showcase page
│   │   ├── contact.html            # Contact form page
│   │   ├── admin_login.html        # Admin login page
│   │   └── admin_dashboard.html    # Project management dashboard
│
├── 🎯 Static Assets
│   └── static/
│       ├── projects.json           # Projects data (auto-managed)
│       ├── css/
│       │   └── style.css           # Main stylesheet (colors, layout)
│       ├── js/
│       │   ├── main.js             # Main JavaScript (modals, interactions)
│       │   └── theme.js            # Dark/Light theme toggle ⭐ NEW
│       ├── images/                 # Image files
│       │   └── profile.jpg         # Your profile photo (add manually)
│       ├── cv.pdf                  # Your CV/Resume (add manually)
│       └── icons/                  # Optional custom icons
│
└── 🔧 Virtual Environment (Local Only)
    └── venv/                       # Created by: python3 -m venv venv
```

---

## 📖 File Descriptions & Purposes

### Core Application Files

#### `app.py`
- **Purpose**: Main Flask application
- **Contains**: All routes (home, projects, contact, admin)
- **Key Functions**:
  - `home()` - Displays home page with projects
  - `projects_page()` - Shows all projects
  - `contact()` - Handles contact form submissions
  - `admin()` - Admin login page
  - `admin_dashboard()` - Project management interface
- **Configuration**: Database-like file access using `projects.json`

#### `wsgi.py`
- **Purpose**: WSGI entry point for PythonAnywhere
- **Why Needed**: PythonAnywhere requires this file to run the app
- **Do Not Edit**: Directly on PythonAnywhere (edit locally, then push)
- **Critical**: Must be configured correctly in PythonAnywhere Web settings

#### `requirements.txt`
- **Purpose**: Lists Python dependencies
- **Current**: Flask, gunicorn, Werkzeug
- **Update When**: Adding new packages (`pip freeze > requirements.txt`)

---

### Documentation Files (READ THESE!)

| File | When to Read | Key Info |
|------|---|---|
| **QUICKSTART.md** | First-time deployer | Deploy in 10 minutes |
| **README.md** | Want overview | Features, structure, local setup |
| **PYTHONANYWHERE_GUIDE.md** | Need deployment help | Step-by-step with screenshots |
| **DEPLOYMENT_CHECKLIST.md** | Before going live | Security, content, testing |
| **CONFIGURATION.md** | Setting up credentials | Gmail, admin, SSL keys |
| **PROJECT_FILES.md** | Understanding structure | This file - what everything does |

---

### Configuration Files

#### `.gitignore`
- **Purpose**: Tells Git what files NOT to commit
- **Protects**: Virtual environment, sensitive .env files
- **Important**: Keeps `venv/` out of Git (too large)

#### `.env.example`
- **Purpose**: Template showing required variables
- **For You**: Copy to `.env` and fill in your values
- **Never Commit**: `.env` files to Git (it's in .gitignore)
- **Local Development**: Use `source .env` to load variables

---

### HTML Templates

#### `base.html` - Base Template
- **Extends**: None (root template)
- **Contains**: Navigation, footer, flash messages
- **Edit For**: Your name, social links, contact info
- **Blocks**: Content, theme toggle button

#### `index.html` - Home Page
- **Extends**: base.html
- **Sections**: Hero, about, skills, featured projects
- **Features**: Profile photo, CTA buttons, CV download
- **Edit For**: Personal information, bio, skills list

#### `projects.html` - Projects Page
- **Extends**: base.html
- **Display**: All projects in grid layout
- **Features**: Click to view details in modal
- **Auto-Updates**: When you add projects in admin

#### `contact.html` - Contact Form
- **Extends**: base.html
- **Features**: Form submission with email
- **Requires**: GMAIL_EMAIL and GMAIL_APP_PASSWORD configured
- **Edit For**: Contact information display

#### `admin_login.html` - Admin Login
- **Extends**: base.html
- **Purpose**: Password-protected admin access
- **Security**: Session-based authentication
- **Password**: Set via ADMIN_PASSWORD variable

#### `admin_dashboard.html` - Project Manager
- **Extends**: base.html
- **Features**: Add, view, delete projects
- **Protected**: Only accessible after correct login
- **Database**: Updates `static/projects.json` automatically

---

### Static Assets

#### `css/style.css` - Styling
- **Purpose**: All visual styling (colors, layout, responsive)
- **Theme Variables**: Root CSS variables for light/dark mode
- **Customizable**: Colors, fonts, spacing
- **Responsive**: Mobile, tablet, desktop breakpoints

#### `js/main.js` - Main JavaScript
- **Features**:
  - Project modal popups (click project to view details)
  - CV download counter (localStorage)
  - Event listeners for interactions
- **Edit For**: Custom interactions, tracking

#### `js/theme.js` - Theme Toggle ⭐ NEW
- **Features**:
  - Dark/Light mode toggle
  - Persists preference in localStorage
  - Updates icon (sun/moon)
- **No Edit Needed**: Works automatically

#### `projects.json` - Projects Database
- **Purpose**: Stores all projects (replaces traditional database)
- **Format**: JSON array of project objects
- **Update Via**: Admin dashboard OR direct edit
- **Auto-Saved**: When using admin panel

#### `images/profile.jpg` - Your Photo
- **Purpose**: Profile photo on home page
- **Required**: Yes, but will work without it (shows broken image)
- **Size**: 180x180px (circular), recommended 500x500px original
- **Add**: Download/screenshot your photo, save to this location

#### `cv.pdf` - Your Resume
- **Purpose**: Downloadable via "Download CV" button
- **Optional**: Will show 404 if not added
- **Add**: Export your CV as PDF to this location

---

## 🔄 Project Data Flow

```
User Access → Flask App (app.py)
    ↓
    ├─→ Route Handler (e.g., @app.route('/'))
    │   ↓
    │   └─→ Load Data (projects.json)
    │       ↓
    │       └─→ Render Template (HTML)
    │           ↓
    │           └─→ Browser Display (CSS + JS)
    │
    └─→ User Interaction
        ├─→ Click Project → Modal (main.js)
        ├─→ Theme Toggle → Dark/Light (theme.js)
        ├─→ Submit Contact → Email (app.py)
        └─→ Admin Login → Manage Projects (admin_dashboard.html)
```

---

## 🚀 Development Workflow

### Local Development
```
1. Create/edit files
2. python3 app.py  (Flask runs locally)
3. Visit http://localhost:5000
4. Test changes
5. git commit & git push
```

### PythonAnywhere Deployment
```
1. Changes pushed to GitHub
2. PythonAnywhere console: git pull origin main
3. touch wsgi.py  (trigger reload)
4. Visit https://yourusername.pythonanywhere.com
5. Changes live!
```

---

## 📝 What To Edit (In Order)

### First Deploy
1. **templates/base.html** - Update your name, social links
2. **templates/contact.html** - Update contact info
3. **static/images/profile.jpg** - Add your photo
4. **static/cv.pdf** - Add your resume
5. **static/projects.json** - Add your projects
6. **.env** (create from .env.example) - Add credentials
7. Deploy to PythonAnywhere

### After First Deploy
- Add projects via `/admin` dashboard instead of editing JSON
- Update content as needed (all changes can go via Git)
- Keep dependencies updated in requirements.txt

---

## 🔐 Security Files & Handling

### 🔴 SENSITIVE (Don't Commit)
- `.env` - Contains passwords and API keys
- `venv/` - Virtual environment (too large, Python specific)
- `*.pyc` - Compiled Python (auto-generated)
- `.vscode/`, `.idea/` - IDE settings

### 🟢 SAFE TO COMMIT
- `app.py` - No secrets in code
- `templates/` - HTML files
- `static/css/`, `static/js/` - Styling & scripts
- `.gitignore` - Tells Git what not to commit
- `README.md`, `QUICKSTART.md` - Documentation

### ⚠️ SPECIAL HANDLING
- `.env.example` - Commit this (shows structure)
- `projects.json` - Can commit (no secrets), but auto-updated on PythonAnywhere
- `requirements.txt` - Always commit (shows dependencies)

---

## 📊 File Size Expectations

| File | Size | Note |
|------|------|------|
| app.py | ~4 KB | Main application |
| requirements.txt | <1 KB | Just packages |
| static/css/style.css | ~10 KB | Styling |
| static/js/main.js | ~2 KB | Interactions |
| projects.json | 1-10 KB | Grows with projects |
| templates/ (all) | ~15 KB | HTML files |
| venv/ | ~100+ MB | Local only, not on server |
| Total on Server | ~50 KB | Very light! |

PythonAnywhere free tier has 100MB, so you're well within limits!

---

## 🔧 Common Edits Cheat Sheet

### Update Site Name
File: `templates/base.html`
Find: `<h2>Jarvis<span>.</span></h2>`
Change to: `<h2>YOUR_NAME<span>.</span></h2>`

### Update Social Links
File: `templates/base.html`
Find: LinkedIn, GitHub, Twitter URLs
Update with your actual profile URLs

### Change Primary Color
File: `static/css/style.css`
Find: `--accent: #2563eb;` (light) and `--accent: #60a5fa;` (dark)
Update with your color codes

### Add New Project
Option 1: Edit `static/projects.json`
Option 2: Visit `/admin` → Login → Add via form

### Update Admin Password
Change: `ADMIN_PASSWORD` environment variable
Where: `.env` (local) or WSGI file (PythonAnywhere)

---

## ✅ Deployment Verification

After deployment to PythonAnywhere, verify:

- [ ] Home page loads
- [ ] Your name displays
- [ ] Profile photo shows
- [ ] Projects display
- [ ] Contact form appears
- [ ] Dark/Light theme toggle works
- [ ] `/admin` page is accessible
- [ ] Admin login works with your password
- [ ] Can add/delete projects from admin
- [ ] Static files load (CSS, JS styling)
- [ ] No 404 errors in console

---

## 📞 Quick Reference

| Need | File |
|------|------|
| Update bio | templates/base.html |
| Add projects | /admin or static/projects.json |
| Change colors | static/css/style.css |
| Deploy steps | QUICKSTART.md |
| Troubleshoot | PYTHONANYWHERE_GUIDE.md |
| Set passwords | .env or CONFIGURATION.md |
| See checklist | DEPLOYMENT_CHECKLIST.md |

---

**Ready to deploy?** Read [QUICKSTART.md](QUICKSTART.md) first! 🚀
