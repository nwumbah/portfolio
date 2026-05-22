"""
WSGI entry point for PythonAnywhere deployment.
This file is required by PythonAnywhere to serve the Flask application.
"""
import sys
import os

# Add the parent directory to the Python path
app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_dir)

from app import app

if __name__ == "__main__":
    app.run()
