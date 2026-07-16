"""
Database models for Industrial Analyzer Management System
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """User model for authentication"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Admin or Engineer
    
    def set_password(self, password):
        """Hash and set the password"""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches the hash"""
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<User {self.username}>'


class Sensor(db.Model):
    """Sensor model for analyzer management"""
    __tablename__ = 'sensors'
    
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(50), unique=True, nullable=False)
    sensor_name = db.Column(db.String(100), nullable=False)
    analyzer_type = db.Column(db.String(100), nullable=False)
    area = db.Column(db.String(100), nullable=False)
    exact_location = db.Column(db.String(200), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), nullable=False)
    installation_date = db.Column(db.Date, nullable=False)
    last_calibration = db.Column(db.Date)
    next_calibration = db.Column(db.Date)
    working_condition = db.Column(db.String(20), nullable=False)  # Working or Faulty
    status = db.Column(db.String(20), nullable=False)  # Active or Inactive
    last_status_update = db.Column(db.DateTime, default=datetime.now)
    remarks = db.Column(db.Text)
    image_path = db.Column(db.String(255))
    
    # Relationships
    maintenance_records = db.relationship('Maintenance', backref='sensor', lazy=True)
    status_history = db.relationship('SensorStatusHistory', backref='sensor', lazy=True, order_by='desc(SensorStatusHistory.change_timestamp)')
    
    
    
    def __repr__(self):
        return f'<Sensor {self.sensor_id}>'


class Maintenance(db.Model):
    """Maintenance model for tracking maintenance tickets"""
    __tablename__ = 'maintenance'
    
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(50), db.ForeignKey('sensors.sensor_id'), nullable=False)
    issue = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(20), nullable=False)  # High, Medium, Low
    status = db.Column(db.String(20), nullable=False)  # Pending, In Progress, Completed
    assigned_engineer = db.Column(db.String(100))
    raised_date = db.Column(db.Date, nullable=False, default=datetime.now)
    completed_date = db.Column(db.Date)
    description = db.Column(db.Text)
    root_cause = db.Column(db.Text)
    corrective_action = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Maintenance {self.id}>'


class Calibration(db.Model):
    """Calibration model for tracking calibration records"""
    __tablename__ = 'calibration'
    
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(50), db.ForeignKey('sensors.sensor_id'), nullable=False)
    last_calibration = db.Column(db.Date, nullable=False)
    next_calibration = db.Column(db.Date, nullable=False)
    calibrated_by = db.Column(db.String(100), nullable=False)
    remarks = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Calibration {self.id}>'


class SensorStatusHistory(db.Model):
    """Sensor status history model for tracking status changes"""
    __tablename__ = 'sensor_status_history'
    
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(50), db.ForeignKey('sensors.sensor_id'), nullable=False)
    old_status = db.Column(db.String(20))
    new_status = db.Column(db.String(20), nullable=False)
    old_working_condition = db.Column(db.String(20))
    new_working_condition = db.Column(db.String(20), nullable=False)
    changed_by = db.Column(db.String(80), nullable=False)
    change_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now)
    remarks = db.Column(db.Text)
    
    def __repr__(self):
        return f'<SensorStatusHistory {self.id}>'


class ActivityLog(db.Model):
    """Activity log model for tracking user actions"""
    __tablename__ = 'activity_log'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    def __repr__(self):
        return f'<ActivityLog {self.id}>'
