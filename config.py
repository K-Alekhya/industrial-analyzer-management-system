"""
Configuration file for Industrial Analyzer Management System
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'industrial-analyzer-secret-key-2024'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    
    # Database configuration - supports both local and cloud databases
    DATABASE_URL = os.environ.get('DATABASE_URL', '')
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        if self.DATABASE_URL:
            # For cloud databases (PostgreSQL on Render/Railway)
            if self.DATABASE_URL.startswith('postgres://'):
                return self.DATABASE_URL.replace('postgres://', 'postgresql://', 1)
            return self.DATABASE_URL
        else:
            # Local SQLite database
            return 'sqlite:///' + os.path.join(basedir, 'database.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Session configuration
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False') == 'True'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
