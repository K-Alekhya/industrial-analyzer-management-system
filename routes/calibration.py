"""
Calibration routes for managing calibration records
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import db, Calibration, Sensor, ActivityLog
from datetime import datetime, timedelta

calibration_bp = Blueprint('calibration', __name__)


@calibration_bp.route('/')
@login_required
def index():
    """Display all calibration records"""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # Get filter
    sensor_id = request.args.get('sensor_id', '')
    
    # Build query
    query = Calibration.query
    
    if sensor_id:
        query = query.filter(Calibration.sensor_id.ilike(f'%{sensor_id}%'))
    
    # Paginate
    records = query.order_by(Calibration.last_calibration.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('calibration/index.html',
                         records=records,
                         sensor_id_filter=sensor_id)


@calibration_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    """Add a new calibration record"""
    if request.method == 'POST':
        try:
            record = Calibration(
                sensor_id=request.form.get('sensor_id'),
                last_calibration=datetime.strptime(request.form.get('last_calibration'), '%Y-%m-%d').date(),
                next_calibration=datetime.strptime(request.form.get('next_calibration'), '%Y-%m-%d').date(),
                calibrated_by=request.form.get('calibrated_by'),
                remarks=request.form.get('remarks')
            )
            
            db.session.add(record)
            db.session.commit()
            
            # Update sensor's calibration dates
            sensor = Sensor.query.filter_by(sensor_id=record.sensor_id).first()
            if sensor:
                sensor.last_calibration = record.last_calibration
                sensor.next_calibration = record.next_calibration
                db.session.commit()
            
            # Log activity
            activity = ActivityLog(
                user=current_user.username,
                action=f'Added calibration record for sensor: {record.sensor_id}',
                timestamp=datetime.now()
            )
            db.session.add(activity)
            db.session.commit()
            
            flash('Calibration record added successfully!', 'success')
            return redirect(url_for('calibration.index'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding calibration: {str(e)}', 'danger')
    
    sensors = Sensor.query.all()
    return render_template('calibration/add.html', sensors=sensors)


@calibration_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Edit calibration record"""
    record = Calibration.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            old_sensor_id = record.sensor_id
            
            record.sensor_id = request.form.get('sensor_id')
            record.last_calibration = datetime.strptime(request.form.get('last_calibration'), '%Y-%m-%d').date()
            record.next_calibration = datetime.strptime(request.form.get('next_calibration'), '%Y-%m-%d').date()
            record.calibrated_by = request.form.get('calibrated_by')
            record.remarks = request.form.get('remarks')
            
            db.session.commit()
            
            # Update sensor's calibration dates
            sensor = Sensor.query.filter_by(sensor_id=record.sensor_id).first()
            if sensor:
                sensor.last_calibration = record.last_calibration
                sensor.next_calibration = record.next_calibration
                db.session.commit()
            
            # Log activity
            activity = ActivityLog(
                user=current_user.username,
                action=f'Updated calibration record #{record.id}',
                timestamp=datetime.now()
            )
            db.session.add(activity)
            db.session.commit()
            
            flash('Calibration record updated successfully!', 'success')
            return redirect(url_for('calibration.index'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating calibration: {str(e)}', 'danger')
    
    sensors = Sensor.query.all()
    return render_template('calibration/edit.html', record=record, sensors=sensors)


@calibration_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    """Delete calibration record"""
    record = Calibration.query.get_or_404(id)
    
    try:
        db.session.delete(record)
        db.session.commit()
        
        # Log activity
        activity = ActivityLog(
            user=current_user.username,
            action=f'Deleted calibration record #{record.id}',
            timestamp=datetime.now()
        )
        db.session.add(activity)
        db.session.commit()
        
        flash('Calibration record deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting calibration: {str(e)}', 'danger')
    
    return redirect(url_for('calibration.index'))


@calibration_bp.route('/due')
@login_required
def due():
    """Display sensors with calibration due"""
    today = datetime.now().date()
    thirty_days_later = today + timedelta(days=30)
    
    sensors_due = Sensor.query.filter(
        Sensor.next_calibration <= thirty_days_later,
        Sensor.next_calibration >= today
    ).order_by(Sensor.next_calibration.asc()).all()
    
    return render_template('calibration/due.html', sensors=sensors_due)


@calibration_bp.route('/calendar')
@login_required
def calendar():
    """Display calendar view of calibrations"""
    today = datetime.now().date()
    
    # Get all upcoming calibrations
    upcoming = Sensor.query.filter(
        Sensor.next_calibration >= today
    ).order_by(Sensor.next_calibration.asc()).all()
    
    return render_template('calibration/calendar.html', upcoming=upcoming)
