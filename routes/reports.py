"""
Reports routes for exporting data in various formats
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file, current_app
from flask_login import login_required
from models import db, Sensor, Maintenance, Calibration
from datetime import datetime
import os
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

reports_bp = Blueprint('reports', __name__)


@reports_bp.route('/')
@login_required
def index():
    """Display reports page with filters"""
    return render_template('reports/index.html')


@reports_bp.route('/export/<format>')
@login_required
def export(format):
    """Export data in specified format (pdf, excel, csv)"""
    report_type = request.args.get('type', 'sensors')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    area = request.args.get('area')
    
    try:
        if report_type == 'sensors':
            data = get_sensor_data(start_date, end_date, area)
            columns = ['Sensor ID', 'Name', 'Analyzer Type', 'Area', 'Location', 
                      'Manufacturer', 'Model', 'Serial No', 'Install Date', 
                      'Last Calibration', 'Next Calibration', 'Condition', 'Status']
        elif report_type == 'maintenance':
            data = get_maintenance_data(start_date, end_date, area)
            columns = ['ID', 'Sensor ID', 'Issue', 'Priority', 'Status', 
                      'Assigned Engineer', 'Raised Date', 'Completed Date']
        elif report_type == 'calibration':
            data = get_calibration_data(start_date, end_date, area)
            columns = ['ID', 'Sensor ID', 'Last Calibration', 'Next Calibration', 
                      'Calibrated By', 'Remarks']
        else:
            flash('Invalid report type', 'danger')
            return redirect(url_for('reports.index'))
        
        if not data:
            flash('No data found for the selected criteria', 'warning')
            return redirect(url_for('reports.index'))
        
        # Create reports directory if it doesn't exist
        reports_dir = os.path.join(current_app.root_path, 'reports')
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if format == 'excel':
            filename = f'{report_type}_report_{timestamp}.xlsx'
            filepath = os.path.join(reports_dir, filename)
            df = pd.DataFrame(data, columns=columns)
            df.to_excel(filepath, index=False)
            return send_file(filepath, as_attachment=True, download_name=filename)
        
        elif format == 'csv':
            filename = f'{report_type}_report_{timestamp}.csv'
            filepath = os.path.join(reports_dir, filename)
            df = pd.DataFrame(data, columns=columns)
            df.to_csv(filepath, index=False)
            return send_file(filepath, as_attachment=True, download_name=filename)
        
        elif format == 'pdf':
            filename = f'{report_type}_report_{timestamp}.pdf'
            filepath = os.path.join(reports_dir, filename)
            generate_pdf_report(filepath, columns, data, report_type)
            return send_file(filepath, as_attachment=True, download_name=filename)
        
        else:
            flash('Invalid export format', 'danger')
            return redirect(url_for('reports.index'))
    
    except Exception as e:
        flash(f'Error generating report: {str(e)}', 'danger')
        return redirect(url_for('reports.index'))


def get_sensor_data(start_date, end_date, area):
    """Get sensor data based on filters"""
    query = Sensor.query
    
    if area:
        query = query.filter(Sensor.area == area)
    
    sensors = query.all()
    
    data = []
    for sensor in sensors:
        data.append([
            sensor.sensor_id,
            sensor.sensor_name,
            sensor.analyzer_type,
            sensor.area,
            sensor.exact_location,
            sensor.manufacturer,
            sensor.model,
            sensor.serial_number,
            sensor.installation_date.strftime('%Y-%m-%d') if sensor.installation_date else '',
            sensor.last_calibration.strftime('%Y-%m-%d') if sensor.last_calibration else '',
            sensor.next_calibration.strftime('%Y-%m-%d') if sensor.next_calibration else '',
            sensor.working_condition,
            sensor.status
        ])
    
    return data


def get_maintenance_data(start_date, end_date, area):
    """Get maintenance data based on filters"""
    query = Maintenance.query.join(Sensor, Maintenance.sensor_id == Sensor.sensor_id)
    
    if area:
        query = query.filter(Sensor.area == area)
    
    if start_date:
        query = query.filter(Maintenance.raised_date >= datetime.strptime(start_date, '%Y-%m-%d').date())
    
    if end_date:
        query = query.filter(Maintenance.raised_date <= datetime.strptime(end_date, '%Y-%m-%d').date())
    
    tickets = query.all()
    
    data = []
    for ticket in tickets:
        data.append([
            ticket.id,
            ticket.sensor_id,
            ticket.issue,
            ticket.priority,
            ticket.status,
            ticket.assigned_engineer or '',
            ticket.raised_date.strftime('%Y-%m-%d') if ticket.raised_date else '',
            ticket.completed_date.strftime('%Y-%m-%d') if ticket.completed_date else ''
        ])
    
    return data


def get_calibration_data(start_date, end_date, area):
    """Get calibration data based on filters"""
    query = Calibration.query.join(Sensor, Calibration.sensor_id == Sensor.sensor_id)
    
    if area:
        query = query.filter(Sensor.area == area)
    
    if start_date:
        query = query.filter(Calibration.last_calibration >= datetime.strptime(start_date, '%Y-%m-%d').date())
    
    if end_date:
        query = query.filter(Calibration.last_calibration <= datetime.strptime(end_date, '%Y-%m-%d').date())
    
    records = query.all()
    
    data = []
    for record in records:
        data.append([
            record.id,
            record.sensor_id,
            record.last_calibration.strftime('%Y-%m-%d'),
            record.next_calibration.strftime('%Y-%m-%d'),
            record.calibrated_by,
            record.remarks or ''
        ])
    
    return data


def generate_pdf_report(filepath, columns, data, report_type):
    """Generate PDF report using ReportLab"""
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    elements = []
    
    # Add title
    styles = getSampleStyleSheet()
    title = Paragraph(f"{report_type.capitalize()} Report", styles['Title'])
    elements.append(title)
    
    # Create table
    table_data = [columns] + data
    table = Table(table_data)
    
    # Style the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(table)
    doc.build(elements)
