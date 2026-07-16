"""
Main application file for Industrial Analyzer Management System
"""
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config
from models import db, User, ActivityLog
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Initialize database
db.init_app(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login"""
    return User.query.get(int(user_id))


# Register blueprints
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.sensors import sensors_bp
from routes.maintenance import maintenance_bp
from routes.calibration import calibration_bp
from routes.reports import reports_bp
from routes.search import search_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(sensors_bp, url_prefix='/sensors')
app.register_blueprint(maintenance_bp, url_prefix='/maintenance')
app.register_blueprint(calibration_bp, url_prefix='/calibration')
app.register_blueprint(reports_bp, url_prefix='/reports')
app.register_blueprint(search_bp, url_prefix='/search')


# Create upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def index():
    """Redirect to login page"""
    return redirect(url_for('auth.login'))


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('errors/500.html'), 500


def log_activity(user, action):
    """Log user activity to the database"""
    try:
        activity = ActivityLog(user=user, action=action, timestamp=datetime.now())
        db.session.add(activity)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error logging activity: {e}")


# Create database tables only in development
if not os.environ.get('DATABASE_URL'):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
