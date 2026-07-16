"""
Search routes for global search functionality
"""
from flask import Blueprint, render_template, request
from flask_login import login_required
from models import db, Sensor, Maintenance, Calibration

search_bp = Blueprint('search', __name__)


@search_bp.route('/')
@login_required
def index():
    """Global search across all entities"""
    query = request.args.get('q', '')
    
    if not query:
        return render_template('search/index.html', 
                             sensors=[], 
                             maintenance=[], 
                             calibration=[],
                             query=query)
    
    # Search in sensors
    sensors = Sensor.query.filter(
        (Sensor.sensor_id.ilike(f'%{query}%')) |
        (Sensor.sensor_name.ilike(f'%{query}%')) |
        (Sensor.analyzer_type.ilike(f'%{query}%')) |
        (Sensor.area.ilike(f'%{query}%')) |
        (Sensor.exact_location.ilike(f'%{query}%'))
    ).limit(10).all()
    
    # Search in maintenance
    maintenance = Maintenance.query.filter(
        (Maintenance.sensor_id.ilike(f'%{query}%')) |
        (Maintenance.issue.ilike(f'%{query}%'))
    ).limit(10).all()
    
    # Search in calibration
    calibration = Calibration.query.filter(
        (Calibration.sensor_id.ilike(f'%{query}%')) |
        (Calibration.calibrated_by.ilike(f'%{query}%'))
    ).limit(10).all()
    
    return render_template('search/index.html',
                         sensors=sensors,
                         maintenance=maintenance,
                         calibration=calibration,
                         query=query)
