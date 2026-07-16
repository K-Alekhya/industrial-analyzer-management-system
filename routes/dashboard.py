"""
Dashboard routes for displaying statistics and overview
"""
from flask import Blueprint, render_template, flash
from flask_login import login_required
from models import db, Sensor, Maintenance, Calibration, ActivityLog
from datetime import datetime, timedelta

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@login_required
def index():
    """Display dashboard with statistics and charts"""
    try:
        # Get statistics
        total_sensors = Sensor.query.count()
        working_sensors = Sensor.query.filter_by(working_condition='Working').count()
        faulty_sensors = Sensor.query.filter_by(working_condition='Faulty').count()
        
        # Calibration due (next calibration within 30 days)
        today = datetime.now().date()
        thirty_days_later = today + timedelta(days=30)
        calibration_due = Sensor.query.filter(
            Sensor.next_calibration <= thirty_days_later,
            Sensor.next_calibration >= today
        ).count()
        
        # Maintenance statistics
        maintenance_pending = Maintenance.query.filter_by(status='Pending').count()
        maintenance_completed = Maintenance.query.filter_by(status='Completed').count()
        
        # Recent activity
        recent_activities = ActivityLog.query.order_by(
            ActivityLog.timestamp.desc()
        ).limit(10).all()
        
        # Upcoming calibrations
        upcoming_calibrations = Sensor.query.filter(
            Sensor.next_calibration >= today
        ).order_by(Sensor.next_calibration.asc()).limit(5).all()
        
        # Data for charts
        # Pie chart data: Working vs Faulty
        pie_chart_data = {
            'labels': ['Working', 'Faulty'],
            'data': [working_sensors, faulty_sensors]
        }
        
        # Bar chart data: Maintenance by status
        bar_chart_data = {
            'labels': ['Pending', 'In Progress', 'Completed'],
            'data': [
                Maintenance.query.filter_by(status='Pending').count(),
                Maintenance.query.filter_by(status='In Progress').count(),
                maintenance_completed
            ]
        }
        
        return render_template('dashboard/index.html',
                             total_sensors=total_sensors,
                             working_sensors=working_sensors,
                             faulty_sensors=faulty_sensors,
                             calibration_due=calibration_due,
                             maintenance_pending=maintenance_pending,
                             maintenance_completed=maintenance_completed,
                             recent_activities=recent_activities,
                             upcoming_calibrations=upcoming_calibrations,
                             pie_chart_data=pie_chart_data,
                             bar_chart_data=bar_chart_data)
    
    except Exception as e:
        flash(f'Error loading dashboard: {str(e)}', 'danger')
        return render_template('dashboard/index.html',
                             total_sensors=0,
                             working_sensors=0,
                             faulty_sensors=0,
                             calibration_due=0,
                             maintenance_pending=0,
                             maintenance_completed=0,
                             recent_activities=[],
                             upcoming_calibrations=[],
                             pie_chart_data={'labels': [], 'data': []},
                             bar_chart_data={'labels': [], 'data': []})
