"""
Authentication routes for login, logout, and session management
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, ActivityLog
from datetime import datetime

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Please provide both username and password.', 'danger')
            return render_template('auth/login.html')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            
            # Log the login activity
            try:
                activity = ActivityLog(
                    user=username,
                    action='User logged in',
                    timestamp=datetime.now()
                )
                db.session.add(activity)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(f"Error logging activity: {e}")
            
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    """Handle user logout"""
    username = current_user.username
    
    # Log the logout activity
    try:
        activity = ActivityLog(
            user=username,
            action='User logged out',
            timestamp=datetime.now()
        )
        db.session.add(activity)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error logging activity: {e}")
    
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
