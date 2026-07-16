"""
Maintenance routes for managing maintenance tickets
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import db, Maintenance, Sensor, ActivityLog
from datetime import datetime

maintenance_bp = Blueprint('maintenance', __name__)


@maintenance_bp.route('/')
@login_required
def index():
    """Display all maintenance tickets"""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # Get filters
    status = request.args.get('status', '')
    priority = request.args.get('priority', '')
    
    # Build query
    query = Maintenance.query
    
    if status:
        query = query.filter(Maintenance.status == status)
    
    if priority:
        query = query.filter(Maintenance.priority == priority)
    
    # Paginate
    tickets = query.order_by(Maintenance.raised_date.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('maintenance/index.html',
                         tickets=tickets,
                         status_filter=status,
                         priority_filter=priority)


@maintenance_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    """Raise a new maintenance ticket"""
    if request.method == 'POST':
        try:
            ticket = Maintenance(
                sensor_id=request.form.get('sensor_id'),
                issue=request.form.get('issue'),
                priority=request.form.get('priority'),
                status='Pending',
                assigned_engineer=request.form.get('assigned_engineer'),
                raised_date=datetime.now().date(),
                description=request.form.get('description')
            )
            
            db.session.add(ticket)
            db.session.commit()
            
            # Log activity
            activity = ActivityLog(
                user=current_user.username,
                action=f'Raised maintenance ticket for sensor: {ticket.sensor_id}',
                timestamp=datetime.now()
            )
            db.session.add(activity)
            db.session.commit()
            
            flash('Maintenance ticket raised successfully!', 'success')
            return redirect(url_for('maintenance.index'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error raising ticket: {str(e)}', 'danger')
    
    sensors = Sensor.query.all()
    return render_template('maintenance/add.html', sensors=sensors)


@maintenance_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Edit maintenance ticket"""
    ticket = Maintenance.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            ticket.sensor_id = request.form.get('sensor_id')
            ticket.issue = request.form.get('issue')
            ticket.priority = request.form.get('priority')
            ticket.status = request.form.get('status')
            ticket.assigned_engineer = request.form.get('assigned_engineer')
            ticket.description = request.form.get('description')
            ticket.root_cause = request.form.get('root_cause')
            ticket.corrective_action = request.form.get('corrective_action')
            
            # Set completed date if status is completed
            if ticket.status == 'Completed' and not ticket.completed_date:
                ticket.completed_date = datetime.now().date()
            
            db.session.commit()
            
            # Log activity
            activity = ActivityLog(
                user=current_user.username,
                action=f'Updated maintenance ticket #{ticket.id}',
                timestamp=datetime.now()
            )
            db.session.add(activity)
            db.session.commit()
            
            flash('Maintenance ticket updated successfully!', 'success')
            return redirect(url_for('maintenance.index'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating ticket: {str(e)}', 'danger')
    
    sensors = Sensor.query.all()
    return render_template('maintenance/edit.html', ticket=ticket, sensors=sensors)


@maintenance_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    """Delete maintenance ticket"""
    ticket = Maintenance.query.get_or_404(id)
    
    try:
        db.session.delete(ticket)
        db.session.commit()
        
        # Log activity
        activity = ActivityLog(
            user=current_user.username,
            action=f'Deleted maintenance ticket #{ticket.id}',
            timestamp=datetime.now()
        )
        db.session.add(activity)
        db.session.commit()
        
        flash('Maintenance ticket deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting ticket: {str(e)}', 'danger')
    
    return redirect(url_for('maintenance.index'))


@maintenance_bp.route('/view/<int:id>')
@login_required
def view(id):
    """View maintenance ticket details"""
    ticket = Maintenance.query.get_or_404(id)
    return render_template('maintenance/view.html', ticket=ticket)
