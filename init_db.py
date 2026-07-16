"""
Database initialization script for Industrial Analyzer Management System
This script creates the database tables and inserts sample data if they don't exist.
"""
from app import app, db
from models import User, Sensor, Maintenance, Calibration, ActivityLog, SensorStatusHistory
from datetime import datetime, timedelta

def init_database():
    """Initialize database with sample data"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully.")
        
        # Check if users exist, if not create sample users
        if User.query.count() == 0:
            print("Creating sample users...")
            
            # Admin user
            admin = User(username='admin', role='Admin')
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Engineer user
            engineer = User(username='engineer', role='Engineer')
            engineer.set_password('eng123')
            db.session.add(engineer)
            
            db.session.commit()
            print("Sample users created: admin/admin123, engineer/eng123")
        else:
            print("Users already exist, skipping user creation.")
        
        # Check if sensors exist, if not create sample sensors
        if Sensor.query.count() == 0:
            print("Creating sample sensors...")
            
            sample_sensors = [
                Sensor(
                    sensor_id='TT-6468A',
                    sensor_name='CFB-6 - MAIN STEAM TEMP TR. -A',
                    analyzer_type='Temperature Transmitter',
                    area='CFB-6',
                    exact_location='Main Steam Line',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN001',
                    installation_date=datetime(2023, 7, 20).date(),
                    last_calibration=datetime(2025, 7, 20).date(),
                    next_calibration=datetime(2026, 7, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Main Steam Temperature Transmitter -A'
                ),
                Sensor(
                    sensor_id='TT-6468B',
                    sensor_name='CFB-6 - MAIN STEAM TEMP TR. -B',
                    analyzer_type='Temperature Transmitter',
                    area='CFB-6',
                    exact_location='Main Steam Line',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN002',
                    installation_date=datetime(2023, 7, 29).date(),
                    last_calibration=datetime(2025, 7, 29).date(),
                    next_calibration=datetime(2026, 7, 29).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Main Steam Temperature Transmitter -B'
                ),
                Sensor(
                    sensor_id='FT-6469A',
                    sensor_name='CFB-6 - MAIN STEAM FLOW TR. -A',
                    analyzer_type='Flow Transmitter',
                    area='CFB-6',
                    exact_location='Main Steam Line',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN003',
                    installation_date=datetime(2023, 7, 29).date(),
                    last_calibration=datetime(2025, 7, 29).date(),
                    next_calibration=datetime(2026, 7, 29).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Main Steam Flow Transmitter -A'
                ),
                Sensor(
                    sensor_id='FT-6469B',
                    sensor_name='CFB-6 - MAIN STEAM FLOW TR. -B',
                    analyzer_type='Flow Transmitter',
                    area='CFB-6',
                    exact_location='Main Steam Line',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN004',
                    installation_date=datetime(2023, 7, 29).date(),
                    last_calibration=datetime(2025, 7, 29).date(),
                    next_calibration=datetime(2026, 7, 29).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Main Steam Flow Transmitter -B'
                ),
                Sensor(
                    sensor_id='PT-6467',
                    sensor_name='CFB-6 - MAIN STEAM PRESSURE TR.',
                    analyzer_type='Pressure Transmitter',
                    area='CFB-6',
                    exact_location='Main Steam Line',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN005',
                    installation_date=datetime(2023, 8, 3).date(),
                    last_calibration=datetime(2025, 8, 3).date(),
                    next_calibration=datetime(2026, 8, 3).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Main Steam Pressure Transmitter'
                ),
                Sensor(
                    sensor_id='TI6404MV',
                    sensor_name='CFB-6 - FEED WATER TEMP TR.',
                    analyzer_type='Temperature Indicator',
                    area='CFB-6',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN006',
                    installation_date=datetime(2024, 5, 28).date(),
                    last_calibration=datetime(2026, 5, 28).date(),
                    next_calibration=datetime(2027, 5, 28).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Feed Water Temperature Transmitter'
                ),
                Sensor(
                    sensor_id='FT-6401A',
                    sensor_name='CFB-6 - FEED WATER FLOW TR. -A',
                    analyzer_type='Flow Transmitter',
                    area='CFB-6',
                    exact_location='Feed Water Line',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN007',
                    installation_date=datetime(2023, 7, 12).date(),
                    last_calibration=datetime(2025, 7, 12).date(),
                    next_calibration=datetime(2026, 7, 12).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Feed Water Flow Transmitter -A'
                ),
                Sensor(
                    sensor_id='FT-6401B',
                    sensor_name='CFB-6 - FEED WATER FLOW TR. -B',
                    analyzer_type='Flow Transmitter',
                    area='CFB-6',
                    exact_location='Feed Water Line',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN008',
                    installation_date=datetime(2023, 7, 12).date(),
                    last_calibration=datetime(2025, 7, 12).date(),
                    next_calibration=datetime(2026, 7, 12).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Feed Water Flow Transmitter -B'
                ),
                Sensor(
                    sensor_id='LT-6406A',
                    sensor_name='CFB-6 - DRUM LEVEL -A',
                    analyzer_type='Level Transmitter',
                    area='CFB-6',
                    exact_location='Drum',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN009',
                    installation_date=datetime(2023, 7, 21).date(),
                    last_calibration=datetime(2025, 7, 21).date(),
                    next_calibration=datetime(2026, 7, 21).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Drum Level Transmitter -A'
                ),
                Sensor(
                    sensor_id='LT-6406B',
                    sensor_name='CFB-6 - DRUM LEVEL -B',
                    analyzer_type='Level Transmitter',
                    area='CFB-6',
                    exact_location='Drum',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN010',
                    installation_date=datetime(2023, 7, 21).date(),
                    last_calibration=datetime(2025, 7, 21).date(),
                    next_calibration=datetime(2026, 7, 21).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Drum Level Transmitter -B'
                ),
                Sensor(
                    sensor_id='LT-6406C',
                    sensor_name='CFB-6 - DRUM LEVEL -C',
                    analyzer_type='Level Transmitter',
                    area='CFB-6',
                    exact_location='Drum',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN011',
                    installation_date=datetime(2023, 7, 21).date(),
                    last_calibration=datetime(2025, 7, 21).date(),
                    next_calibration=datetime(2026, 7, 21).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-6 Drum Level Transmitter -C'
                ),
                Sensor(
                    sensor_id='TI-B-7517',
                    sensor_name='CFB-7 - MAIN STEAM TEMP TR.',
                    analyzer_type='Temperature Indicator',
                    area='CFB-7',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN012',
                    installation_date=datetime(2023, 10, 5).date(),
                    last_calibration=datetime(2025, 10, 5).date(),
                    next_calibration=datetime(2026, 10, 5).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Main Steam Temperature Transmitter'
                ),
                Sensor(
                    sensor_id='FI-B-7518',
                    sensor_name='CFB-7 - MAIN STEAM FLOW TR',
                    analyzer_type='Flow Indicator',
                    area='CFB-7',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN013',
                    installation_date=datetime(2023, 10, 21).date(),
                    last_calibration=datetime(2025, 10, 21).date(),
                    next_calibration=datetime(2026, 10, 21).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Main Steam Flow Transmitter'
                ),
                Sensor(
                    sensor_id='PI-B-7516',
                    sensor_name='CFB-7 - MAIN STEAM PRESSURE TR.',
                    analyzer_type='Pressure Indicator',
                    area='CFB-7',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='EJA110A',
                    serial_number='SN014',
                    installation_date=datetime(2023, 10, 21).date(),
                    last_calibration=datetime(2025, 10, 21).date(),
                    next_calibration=datetime(2026, 10, 21).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Main Steam Pressure Transmitter'
                ),
                Sensor(
                    sensor_id='FF-TE-B-7414',
                    sensor_name='CFB-7 - FEED WATER TEMP TR.',
                    analyzer_type='Temperature Element',
                    area='CFB-7',
                    exact_location='Feed Water Line',
                    manufacturer='Rosemount',
                    model='304',
                    serial_number='SN015',
                    installation_date=datetime(2023, 9, 23).date(),
                    last_calibration=datetime(2025, 9, 23).date(),
                    next_calibration=datetime(2026, 9, 23).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Feed Water Temperature Element'
                ),
                Sensor(
                    sensor_id='FI-B-7421A',
                    sensor_name='CFB-7 - FEED WATER FLOW TR. -A',
                    analyzer_type='Flow Indicator',
                    area='CFB-7',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN016',
                    installation_date=datetime(2023, 10, 22).date(),
                    last_calibration=datetime(2025, 10, 22).date(),
                    next_calibration=datetime(2026, 10, 22).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Feed Water Flow Transmitter -A'
                ),
                Sensor(
                    sensor_id='FI-B-7421B',
                    sensor_name='CFB-7 - FEED WATER FLOW TR. -B',
                    analyzer_type='Flow Indicator',
                    area='CFB-7',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN017',
                    installation_date=datetime(2023, 10, 22).date(),
                    last_calibration=datetime(2025, 10, 22).date(),
                    next_calibration=datetime(2026, 10, 22).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Feed Water Flow Transmitter -B'
                ),
                Sensor(
                    sensor_id='FF-LT-B-7431A',
                    sensor_name='CFB-7 - DRUM LEVEL -A',
                    analyzer_type='Level Transmitter',
                    area='CFB-7',
                    exact_location='Drum',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN018',
                    installation_date=datetime(2023, 10, 4).date(),
                    last_calibration=datetime(2025, 10, 4).date(),
                    next_calibration=datetime(2026, 10, 4).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Drum Level Transmitter -A'
                ),
                Sensor(
                    sensor_id='FF-LT-B-7431B',
                    sensor_name='CFB-7 - DRUM LEVEL -B',
                    analyzer_type='Level Transmitter',
                    area='CFB-7',
                    exact_location='Drum',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN019',
                    installation_date=datetime(2023, 10, 4).date(),
                    last_calibration=datetime(2025, 10, 4).date(),
                    next_calibration=datetime(2026, 10, 4).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Drum Level Transmitter -B'
                ),
                Sensor(
                    sensor_id='FF-LT-B-7431C',
                    sensor_name='CFB-7 - DRUM LEVEL -C',
                    analyzer_type='Level Transmitter',
                    area='CFB-7',
                    exact_location='Drum',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN020',
                    installation_date=datetime(2023, 10, 4).date(),
                    last_calibration=datetime(2025, 10, 4).date(),
                    next_calibration=datetime(2026, 10, 4).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-7 Drum Level Transmitter -C'
                ),
                Sensor(
                    sensor_id='TI-B-8324',
                    sensor_name='GB - MAIN STEAM TEMP TR.',
                    analyzer_type='Temperature Indicator',
                    area='GB',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN021',
                    installation_date=datetime(2023, 7, 20).date(),
                    last_calibration=datetime(2025, 7, 20).date(),
                    next_calibration=datetime(2026, 7, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Main Steam Temperature Transmitter'
                ),
                Sensor(
                    sensor_id='FIB-8327A',
                    sensor_name='GB - MAIN STEAM FLOW TR. -A',
                    analyzer_type='Flow Indicator',
                    area='GB',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN022',
                    installation_date=datetime(2023, 11, 18).date(),
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Main Steam Flow Transmitter -A'
                ),
                Sensor(
                    sensor_id='FIB-8327B',
                    sensor_name='GB - MAIN STEAM FLOW TR. -B',
                    analyzer_type='Flow Indicator',
                    area='GB',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN023',
                    installation_date=datetime(2023, 11, 18).date(),
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Main Steam Flow Transmitter -B'
                ),
                Sensor(
                    sensor_id='PIB-8322',
                    sensor_name='GB - MAIN STEAM PRESSURE TR. -A',
                    analyzer_type='Pressure Indicator',
                    area='GB',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='EJA110A',
                    serial_number='SN024',
                    installation_date=datetime(2023, 11, 11).date(),
                    last_calibration=datetime(2025, 11, 11).date(),
                    next_calibration=datetime(2026, 11, 11).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Main Steam Pressure Transmitter -A'
                ),
                Sensor(
                    sensor_id='TIB-8322',
                    sensor_name='GB - FEED WATER TEMP TR.',
                    analyzer_type='Temperature Indicator',
                    area='GB',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN025',
                    installation_date=datetime(2023, 11, 17).date(),
                    last_calibration=datetime(2025, 11, 17).date(),
                    next_calibration=datetime(2026, 11, 17).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Feed Water Temperature Transmitter'
                ),
                Sensor(
                    sensor_id='FIC-B8225A',
                    sensor_name='GB - FEED WATER FLOW TR. -A',
                    analyzer_type='Flow Indicator Controller',
                    area='GB',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN026',
                    installation_date=datetime(2023, 11, 18).date(),
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Feed Water Flow Transmitter -A'
                ),
                Sensor(
                    sensor_id='FIC-B8225B',
                    sensor_name='GB - FEED WATER FLOW TR. -B',
                    analyzer_type='Flow Indicator Controller',
                    area='GB',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN027',
                    installation_date=datetime(2023, 11, 18).date(),
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Feed Water Flow Transmitter -B'
                ),
                Sensor(
                    sensor_id='LIB-8327A',
                    sensor_name='GB - DRUM LEVEL -A',
                    analyzer_type='Level Indicator',
                    area='GB',
                    exact_location='Drum',
                    manufacturer='Yokogawa',
                    model='EJA110A',
                    serial_number='SN028',
                    installation_date=datetime(2023, 11, 18).date(),
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Drum Level Transmitter -A'
                ),
                Sensor(
                    sensor_id='LIB-8327B',
                    sensor_name='GB - DRUM LEVEL -B',
                    analyzer_type='Level Indicator',
                    area='GB',
                    exact_location='Drum',
                    manufacturer='Yokogawa',
                    model='EJA110A',
                    serial_number='SN029',
                    installation_date=datetime(2023, 11, 18).date(),
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Drum Level Transmitter -B'
                ),
                Sensor(
                    sensor_id='LIB-8327C',
                    sensor_name='GB - DRUM LEVEL -C',
                    analyzer_type='Level Indicator',
                    area='GB',
                    exact_location='Drum',
                    manufacturer='Yokogawa',
                    model='EJA110A',
                    serial_number='SN030',
                    installation_date=datetime(2023, 11, 18).date(),
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='GB Drum Level Transmitter -C'
                ),
                Sensor(
                    sensor_id='TIB-9237A',
                    sensor_name='CFB-9 - MAIN STEAM TEMP TR. -A',
                    analyzer_type='Temperature Indicator',
                    area='CFB-9',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN031',
                    installation_date=datetime(2023, 9, 26).date(),
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Main Steam Temperature Transmitter -A'
                ),
                Sensor(
                    sensor_id='TIB-9237B',
                    sensor_name='CFB-9 - MAIN STEAM TEMP TR. -B',
                    analyzer_type='Temperature Indicator',
                    area='CFB-9',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN032',
                    installation_date=datetime(2023, 9, 26).date(),
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Main Steam Temperature Transmitter -B'
                ),
                Sensor(
                    sensor_id='FIB-9245A',
                    sensor_name='CFB-9 - MAIN STEAM FLOW TR. -A',
                    analyzer_type='Flow Indicator',
                    area='CFB-9',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN033',
                    installation_date=datetime(2023, 9, 24).date(),
                    last_calibration=datetime(2025, 9, 24).date(),
                    next_calibration=datetime(2026, 9, 24).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Main Steam Flow Transmitter -A'
                ),
                Sensor(
                    sensor_id='FIB-9245B',
                    sensor_name='CFB-9 - MAIN STEAM FLOW TR. -B',
                    analyzer_type='Flow Indicator',
                    area='CFB-9',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN034',
                    installation_date=datetime(2023, 9, 24).date(),
                    last_calibration=datetime(2025, 9, 24).date(),
                    next_calibration=datetime(2026, 9, 24).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Main Steam Flow Transmitter -B'
                ),
                Sensor(
                    sensor_id='PIB-9236A',
                    sensor_name='CFB-9 - MAIN STEAM PRESSURE TR. -A',
                    analyzer_type='Pressure Indicator',
                    area='CFB-9',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='EJA110A',
                    serial_number='SN035',
                    installation_date=datetime(2023, 9, 26).date(),
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Main Steam Pressure Transmitter -A'
                ),
                Sensor(
                    sensor_id='PIB-9236B',
                    sensor_name='CFB-9 - MAIN STEAM PRESSURE TR. -B',
                    analyzer_type='Pressure Indicator',
                    area='CFB-9',
                    exact_location='Main Steam Line',
                    manufacturer='Yokogawa',
                    model='EJA110A',
                    serial_number='SN036',
                    installation_date=datetime(2023, 9, 26).date(),
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Main Steam Pressure Transmitter -B'
                ),
                Sensor(
                    sensor_id='TI-B-9209A',
                    sensor_name='CFB-9 - FEED WATER TEMP TR. -A',
                    analyzer_type='Temperature Indicator',
                    area='CFB-9',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN037',
                    installation_date=datetime(2023, 9, 26).date(),
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Feed Water Temperature Transmitter -A'
                ),
                Sensor(
                    sensor_id='TI-B-9209B',
                    sensor_name='CFB-9 - FEED WATER TEMP TR. -B',
                    analyzer_type='Temperature Indicator',
                    area='CFB-9',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN038',
                    installation_date=datetime(2023, 9, 26).date(),
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Feed Water Temperature Transmitter -B'
                ),
                Sensor(
                    sensor_id='FI-B-9200A',
                    sensor_name='CFB-9 - FEED WATER FLOW TR. -A',
                    analyzer_type='Flow Indicator',
                    area='CFB-9',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN039',
                    installation_date=datetime(2023, 9, 26).date(),
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Feed Water Flow Transmitter -A'
                ),
                Sensor(
                    sensor_id='FI-B-9200B',
                    sensor_name='CFB-9 - FEED WATER FLOW TR. -B',
                    analyzer_type='Flow Indicator',
                    area='CFB-9',
                    exact_location='Feed Water Line',
                    manufacturer='Yokogawa',
                    model='YF100',
                    serial_number='SN040',
                    installation_date=datetime(2023, 9, 26).date(),
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='CFB-9 Feed Water Flow Transmitter -B'
                )
            ]
            
            for sensor in sample_sensors:
                db.session.add(sensor)
            
            db.session.commit()
            print(f"Sample sensors created: {len(sample_sensors)} sensors")
        else:
            print("Sensors already exist, skipping sensor creation.")
        
        # Check if maintenance records exist, if not create sample records
        if Maintenance.query.count() == 0:
            print("Creating sample maintenance records...")
            
            sample_maintenance = [
                Maintenance(
                    sensor_id='TT-6468A',
                    issue='Temperature transmitter drift detected',
                    priority='Medium',
                    status='Pending',
                    assigned_engineer='John Smith',
                    raised_date=datetime(2024, 6, 1).date(),
                    description='Temperature transmitter showing slight drift from expected values',
                    root_cause='Sensor calibration drift',
                    corrective_action='Pending recalibration'
                ),
                Maintenance(
                    sensor_id='FT-6469A',
                    issue='Routine maintenance check',
                    priority='Low',
                    status='Completed',
                    assigned_engineer='Jane Doe',
                    raised_date=datetime(2024, 5, 15).date(),
                    completed_date=datetime(2024, 5, 20).date(),
                    description='Scheduled routine maintenance check',
                    root_cause='N/A - Routine check',
                    corrective_action='Cleaned sensor, verified calibration'
                ),
                Maintenance(
                    sensor_id='PT-6467',
                    issue='Pressure sensor not responding',
                    priority='High',
                    status='In Progress',
                    assigned_engineer='Mike Johnson',
                    raised_date=datetime(2024, 6, 10).date(),
                    description='Pressure sensor stopped responding after power fluctuation',
                    root_cause='Possible electronic component failure',
                    corrective_action='Awaiting diagnostic test results'
                ),
                Maintenance(
                    sensor_id='LT-6406A',
                    issue='Level sensor drift detected',
                    priority='Medium',
                    status='Pending',
                    assigned_engineer='Sarah Williams',
                    raised_date=datetime(2024, 6, 15).date(),
                    description='Level sensor readings drifting from expected values',
                    root_cause='Calibration drift due to environmental conditions',
                    corrective_action='Recalibration in progress'
                ),
                Maintenance(
                    sensor_id='TI-B-7517',
                    issue='Temperature sensor calibration drift',
                    priority='Medium',
                    status='Pending',
                    assigned_engineer='John Smith',
                    raised_date=datetime(2024, 6, 20).date(),
                    description='Temperature sensor showing inconsistent readings',
                    root_cause='Sensor membrane degradation',
                    corrective_action='Membrane replacement scheduled'
                ),
                Maintenance(
                    sensor_id='PIB-8322',
                    issue='Pressure sensor malfunction',
                    priority='High',
                    status='In Progress',
                    assigned_engineer='Jane Doe',
                    raised_date=datetime(2024, 6, 25).date(),
                    description='Pressure sensor giving erratic readings',
                    root_cause='Signal interference from nearby equipment',
                    corrective_action='Shielding installation in progress'
                ),
                Maintenance(
                    sensor_id='TIB-9237A',
                    issue='Temperature sensor reading erratic',
                    priority='High',
                    status='Pending',
                    assigned_engineer='Mike Johnson',
                    raised_date=datetime(2024, 6, 28).date(),
                    description='Temperature sensor showing unstable readings',
                    root_cause='Thermal stress on sensor components',
                    corrective_action='Sensor replacement pending'
                ),
                Maintenance(
                    sensor_id='FIB-9245A',
                    issue='Routine sensor cleaning',
                    priority='Low',
                    status='Completed',
                    assigned_engineer='Sarah Williams',
                    raised_date=datetime(2024, 5, 1).date(),
                    completed_date=datetime(2024, 5, 3).date(),
                    description='Scheduled cleaning of flow transmitter',
                    root_cause='N/A - Routine maintenance',
                    corrective_action='Sensor cleaned and calibrated'
                ),
                Maintenance(
                    sensor_id='PIB-9236A',
                    issue='Temperature sensor fouling',
                    priority='Medium',
                    status='Completed',
                    assigned_engineer='John Smith',
                    raised_date=datetime(2024, 4, 15).date(),
                    completed_date=datetime(2024, 4, 18).date(),
                    description='Temperature sensor showing reduced sensitivity',
                    root_cause='Sensor fouling due to particulate buildup',
                    corrective_action='Sensor cleaned and recalibrated'
                ),
                Maintenance(
                    sensor_id='TI-B-9209A',
                    issue='Flow sensor replacement',
                    priority='High',
                    status='Completed',
                    assigned_engineer='Jane Doe',
                    raised_date=datetime(2024, 3, 20).date(),
                    completed_date=datetime(2024, 3, 25).date(),
                    description='Flow sensor failed calibration test',
                    root_cause='Electrode degradation',
                    corrective_action='Sensor replaced and calibrated'
                )
            ]
            
            for maintenance in sample_maintenance:
                db.session.add(maintenance)
            
            db.session.commit()
            print(f"Sample maintenance records created: {len(sample_maintenance)} records")
        else:
            print("Maintenance records already exist, skipping maintenance creation.")
        
        # Check if calibration records exist, if not create sample records
        if Calibration.query.count() == 0:
            print("Creating sample calibration records...")
            
            sample_calibration = [
                Calibration(
                    sensor_id='TT-6468A',
                    last_calibration=datetime(2025, 7, 20).date(),
                    next_calibration=datetime(2026, 7, 20).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed successfully'
                ),
                Calibration(
                    sensor_id='TT-6468B',
                    last_calibration=datetime(2025, 7, 29).date(),
                    next_calibration=datetime(2026, 7, 29).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FT-6469A',
                    last_calibration=datetime(2025, 7, 29).date(),
                    next_calibration=datetime(2026, 7, 29).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FT-6469B',
                    last_calibration=datetime(2025, 7, 29).date(),
                    next_calibration=datetime(2026, 7, 29).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='PT-6467',
                    last_calibration=datetime(2025, 8, 3).date(),
                    next_calibration=datetime(2026, 8, 3).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='TI6404MV',
                    last_calibration=datetime(2026, 5, 28).date(),
                    next_calibration=datetime(2027, 5, 28).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FT-6401A',
                    last_calibration=datetime(2025, 7, 12).date(),
                    next_calibration=datetime(2026, 7, 12).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FT-6401B',
                    last_calibration=datetime(2025, 7, 12).date(),
                    next_calibration=datetime(2026, 7, 12).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='LT-6406A',
                    last_calibration=datetime(2025, 7, 21).date(),
                    next_calibration=datetime(2026, 7, 21).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='LT-6406B',
                    last_calibration=datetime(2025, 7, 21).date(),
                    next_calibration=datetime(2026, 7, 21).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='LT-6406C',
                    last_calibration=datetime(2025, 7, 21).date(),
                    next_calibration=datetime(2026, 7, 21).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='TI-B-7517',
                    last_calibration=datetime(2025, 10, 5).date(),
                    next_calibration=datetime(2026, 10, 5).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FI-B-7518',
                    last_calibration=datetime(2025, 10, 21).date(),
                    next_calibration=datetime(2026, 10, 21).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='PI-B-7516',
                    last_calibration=datetime(2025, 10, 21).date(),
                    next_calibration=datetime(2026, 10, 21).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FF-TE-B-7414',
                    last_calibration=datetime(2025, 9, 23).date(),
                    next_calibration=datetime(2026, 9, 23).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FI-B-7421A',
                    last_calibration=datetime(2025, 10, 22).date(),
                    next_calibration=datetime(2026, 10, 22).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FI-B-7421B',
                    last_calibration=datetime(2025, 10, 22).date(),
                    next_calibration=datetime(2026, 10, 22).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FF-LT-B-7431A',
                    last_calibration=datetime(2025, 10, 4).date(),
                    next_calibration=datetime(2026, 10, 4).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FF-LT-B-7431B',
                    last_calibration=datetime(2025, 10, 4).date(),
                    next_calibration=datetime(2026, 10, 4).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FF-LT-B-7431C',
                    last_calibration=datetime(2025, 10, 4).date(),
                    next_calibration=datetime(2026, 10, 4).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='TI-B-8324',
                    last_calibration=datetime(2025, 7, 20).date(),
                    next_calibration=datetime(2026, 7, 20).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FIB-8327A',
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FIB-8327B',
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='PIB-8322',
                    last_calibration=datetime(2025, 11, 11).date(),
                    next_calibration=datetime(2026, 11, 11).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='TIB-8322',
                    last_calibration=datetime(2025, 11, 17).date(),
                    next_calibration=datetime(2026, 11, 17).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FIC-B8225A',
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FIC-B8225B',
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='LIB-8327A',
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='LIB-8327B',
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='LIB-8327C',
                    last_calibration=datetime(2025, 11, 18).date(),
                    next_calibration=datetime(2026, 11, 18).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='TIB-9237A',
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='TIB-9237B',
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FIB-9245A',
                    last_calibration=datetime(2025, 9, 24).date(),
                    next_calibration=datetime(2026, 9, 24).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FIB-9245B',
                    last_calibration=datetime(2025, 9, 24).date(),
                    next_calibration=datetime(2026, 9, 24).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='PIB-9236A',
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='PIB-9236B',
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='TI-B-9209A',
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    calibrated_by='John Smith',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='TI-B-9209B',
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    calibrated_by='Jane Doe',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FI-B-9200A',
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Yearly calibration completed'
                ),
                Calibration(
                    sensor_id='FI-B-9200B',
                    last_calibration=datetime(2025, 9, 26).date(),
                    next_calibration=datetime(2026, 9, 26).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Yearly calibration completed'
                )
            ]
            
            for calibration in sample_calibration:
                db.session.add(calibration)
            
            db.session.commit()
            print(f"Sample calibration records created: {len(sample_calibration)} records")
        else:
            print("Calibration records already exist, skipping calibration creation.")
        
        # Create initial activity log
        if ActivityLog.query.count() == 0:
            print("Creating initial activity log...")
            
            initial_activity = ActivityLog(
                user='admin',
                action='Database Initialization - Initial database setup with sample sensors, maintenance, and calibration records',
                timestamp=datetime.now()
            )
            
            db.session.add(initial_activity)
            db.session.commit()
            print("Initial activity log created.")
        else:
            print("Activity log already exists, skipping activity log creation.")
        
        print("\nDatabase initialization completed successfully!")
        print("Default login credentials:")
        print("Admin: username=admin, password=admin123")
        print("Engineer: username=engineer, password=eng123")

if __name__ == '__main__':
    init_database()
