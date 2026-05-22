from flask import Flask, render_template, request, flash, redirect, url_for, session
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
# Use environment variable for secret key, fallback to a default for development
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# ====================== CONFIG ======================
# Load configuration from environment variables or use defaults
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'your_secure_password_here')  # ← CHANGE THIS!
GMAIL_EMAIL = os.environ.get('GMAIL_EMAIL', 'jnwumbah@gmail.com')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD', 'your_16char_app_password_here')  # ← Generate from Google App Passwords

PROJECTS_FILE = 'static/projects.json'

def load_projects():
    if os.path.exists(PROJECTS_FILE):
        with open(PROJECTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_projects(projects):
    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f, indent=4)

def send_email(name, email, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_EMAIL
        msg['To'] = GMAIL_EMAIL
        msg['Subject'] = f"New Contact Form Message from {name}"

        body = f"""
        New message from your portfolio website:

        Name: {name}
        Email: {email}
        Message:
        {message}
        """
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

@app.route('/')
def home():
    projects = load_projects()
    return render_template('index.html', projects=projects)

@app.route('/projects')
def projects_page():
    projects = load_projects()
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if send_email(name, email, message):
            flash("✅ Thank you! Your message has been sent successfully.", "success")
        else:
            flash("❌ Sorry, there was an error sending your message.", "error")
    return render_template('contact.html')

# ====================== ADMIN ======================
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form.get('password') == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('admin_dashboard'))
        flash("Incorrect password!", "error")
    return render_template('admin_login.html')

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin'))
    
    projects = load_projects()
    
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_project = {
                "title": request.form.get('title'),
                "description": request.form.get('description'),
                "technologies": request.form.get('technologies'),
                "details": request.form.get('details', '')
            }
            projects.append(new_project)
            save_projects(projects)
            flash("Project added successfully!", "success")
        
        elif action == 'delete':
            index = int(request.form.get('index'))
            if 0 <= index < len(projects):
                projects.pop(index)
                save_projects(projects)
                flash("Project deleted.", "success")
    
    return render_template('admin_dashboard.html', projects=projects)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    # Use debug=False for production (PythonAnywhere)
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)