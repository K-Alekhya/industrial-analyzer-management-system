"""
Sensor management routes for CRUD operations
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from models import db, Sensor, ActivityLog, SensorStatusHistory
from datetime import datetime
import os
from werkzeug.utils import secure_filename

sensors_bp = Blueprint('sensors', __name__)


def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@sensors_bp.route('/')
@login_required
def index():
    """Display all sensors with pagination and filters"""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # Get filters
    search = request.args.get('search', '')
    analyzer_type = request.args.get('analyzer_type', '')
    area = request.args.get('area', '')
    status = request.args.get('status', '')
    
    # Build query
    query = Sensor.query
    
    if search:
        query = query.filter(
            (Sensor.sensor_id.ilike(f'%{search}%')) |
            (Sensor.sensor_name.ilike(f'%{search}%'))
        )
    
    if analyzer_type:
        query = query.filter(Sensor.analyzer_type == analyzer_type)
    
    if area:
        query = query.filter(Sensor.area.ilike(f'%{area}%'))
    
    if status:
        query = query.filter(Sensor.status == status)
    
    # Paginate
    sensors = query.order_by(Sensor.id.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    # Get unique values for filters
    analyzer_types = db.session.query(Sensor.analyzer_type).distinct().all()
    areas = db.session.query(Sensor.area).distinct().all()
    
    return render_template('sensors/index.html',
                         sensors=sensors,
                         analyzer_types=analyzer_types,
                         areas=areas,
                         search=search,
                         analyzer_type_filter=analyzer_type,
                         area_filter=area,
                         status_filter=status)


@sensors_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    """Add a new sensor"""
    if request.method == 'POST':
        try:
            # Check for duplicate sensor_id
            sensor_id = request.form.get('sensor_id')
            if Sensor.query.filter_by(sensor_id=sensor_id).first():
                flash('Sensor ID already exists!', 'danger')
                return render_template('sensors/add.html')
            
            sensor = Sensor(
                sensor_id=sensor_id,
                sensor_name=request.form.get('sensor_name'),
                analyzer_type=request.form.get('analyzer_type'),
                area=request.form.get('area'),
                exact_location=request.form.get('exact_location'),
                manufacturer=request.form.get('manufacturer'),
                model=request.form.get('model'),
                serial_number=request.form.get('serial_number'),
                installation_date=datetime.strptime(request.form.get('installation_date'), '%Y-%m-%d').date(),
                last_calibration=datetime.strptime(request.form.get('last_calibration'), '%Y-%m-%d').date() if request.form.get('last_calibration') else None,
                next_calibration=datetime.strptime(request.form.get('next_calibration'), '%Y-%m-%d').date() if request.form.get('next_calibration') else None,
                working_condition=request.form.get('working_condition'),
                status=request.form.get('status'),
                remarks=request.form.get('remarks')
            )
            
            # Handle image upload
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    # Add timestamp to filename to make it unique
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = f"{timestamp}_{filename}"
                    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    sensor.image_path = filename
            
            db.session.add(sensor)
            db.session.commit()
            
            # Log activity
            activity = ActivityLog(
                user=current_user.username,
                action=f'Added sensor: {sensor_id}',
                timestamp=datetime.now()
            )
            db.session.add(activity)
            db.session.commit()
            
            flash('Sensor added successfully!', 'success')
            return redirect(url_for('sensors.index'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding sensor: {str(e)}', 'danger')
    
    return render_template('sensors/add.html')


@sensors_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Edit an existing sensor"""
    sensor = Sensor.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            # Check if sensor_id is being changed and if it's already in use
            new_sensor_id = request.form.get('sensor_id')
            if new_sensor_id != sensor.sensor_id:
                if Sensor.query.filter_by(sensor_id=new_sensor_id).first():
                    flash('Sensor ID already exists!', 'danger')
                    return render_template('sensors/edit.html', sensor=sensor)
            
            # Store old values for status tracking
            old_status = sensor.status
            old_working_condition = sensor.working_condition
            
            sensor.sensor_id = new_sensor_id
            sensor.sensor_name = request.form.get('sensor_name')
            sensor.analyzer_type = request.form.get('analyzer_type')
            sensor.area = request.form.get('area')
            sensor.exact_location = request.form.get('exact_location')
            sensor.manufacturer = request.form.get('manufacturer')
            sensor.model = request.form.get('model')
            sensor.serial_number = request.form.get('serial_number')
            sensor.installation_date = datetime.strptime(request.form.get('installation_date'), '%Y-%m-%d').date()
            sensor.last_calibration = datetime.strptime(request.form.get('last_calibration'), '%Y-%m-%d').date() if request.form.get('last_calibration') else None
            sensor.next_calibration = datetime.strptime(request.form.get('next_calibration'), '%Y-%m-%d').date() if request.form.get('next_calibration') else None
            sensor.working_condition = request.form.get('working_condition')
            sensor.status = request.form.get('status')
            sensor.remarks = request.form.get('remarks')
            
            # Update last_status_update timestamp
            sensor.last_status_update = datetime.utcnow()
            
            # Handle image upload
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename and allowed_file(file.filename):
                    # Delete old image if exists
                    if sensor.image_path:
                        old_path = os.path.join(current_app.config['UPLOAD_FOLDER'], sensor.image_path)
                        if os.path.exists(old_path):
                            os.remove(old_path)
                    
                    filename = secure_filename(file.filename)
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = f"{timestamp}_{filename}"
                    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    sensor.image_path = filename
            
            db.session.commit()
            
            # Log status changes to history
            if old_status != sensor.status or old_working_condition != sensor.working_condition:
                status_history = SensorStatusHistory(
                    sensor_id=sensor.sensor_id,
                    old_status=old_status,
                    new_status=sensor.status,
                    old_working_condition=old_working_condition,
                    new_working_condition=sensor.working_condition,
                    changed_by=current_user.username,
                    change_timestamp=datetime.now(),
                    remarks='Status updated via edit form'
                )
                db.session.add(status_history)
                db.session.commit()
            
            # Log activity
            activity = ActivityLog(
                user=current_user.username,
                action=f'Edited sensor: {sensor.sensor_id}',
                timestamp=datetime.now()
            )
            db.session.add(activity)
            db.session.commit()
            
            flash('Sensor updated successfully!', 'success')
            return redirect(url_for('sensors.index'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating sensor: {str(e)}', 'danger')
    
    return render_template('sensors/edit.html', sensor=sensor)


@sensors_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    """Delete a sensor"""
    sensor = Sensor.query.get_or_404(id)
    
    try:
        # Delete image if exists
        if sensor.image_path:
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], sensor.image_path)
            if os.path.exists(image_path):
                os.remove(image_path)
        
        sensor_id = sensor.sensor_id
        db.session.delete(sensor)
        db.session.commit()
        
        # Log activity
        activity = ActivityLog(
            user=current_user.username,
            action=f'Deleted sensor: {sensor_id}',
            timestamp=datetime.now()
        )
        db.session.add(activity)
        db.session.commit()
        
        flash('Sensor deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting sensor: {str(e)}', 'danger')
    
    return redirect(url_for('sensors.index'))


@sensors_bp.route('/view/<int:id>')
@login_required
def view(id):
    """View sensor details"""
    sensor = Sensor.query.get_or_404(id)
    return render_template('sensors/view.html', sensor=sensor)
