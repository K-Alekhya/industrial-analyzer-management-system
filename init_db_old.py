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
                    sensor_id='FIB-1101D',
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
                    sensor_id='PRDS-TT-01',
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
                    sensor_id='TG#3 I/L STEAM',
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
                Sensor(
                    sensor_id='TEMP-001',
                    sensor_name='Temperature Sensor 1',
                    analyzer_type='Temperature Sensor',
                    area='Production Line A',
                    exact_location='Reactor Vessel',
                    manufacturer='Siemens',
                    model='SITRANS T',
                    serial_number='SN002345',
                    installation_date=datetime(2023, 2, 20).date(),
                    last_calibration=datetime(2024, 2, 20).date(),
                    next_calibration=datetime(2024, 8, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Temperature monitoring for reactor vessel'
                ),
                Sensor(
                    sensor_id='TEMP-002',
                    sensor_name='Temperature Sensor 2',
                    analyzer_type='Temperature Sensor',
                    area='Production Line C',
                    exact_location='Heat Exchanger',
                    manufacturer='Siemens',
                    model='SITRANS T',
                    serial_number='SN002346',
                    installation_date=datetime(2023, 3, 15).date(),
                    last_calibration=datetime(2024, 3, 15).date(),
                    next_calibration=datetime(2024, 9, 15).date(),
                    working_condition='Faulty',
                    status='Inactive',
                    remarks='Temperature sensor malfunction - needs replacement'
                ),
                Sensor(
                    sensor_id='TEMP-003',
                    sensor_name='Temperature Sensor 3',
                    analyzer_type='Temperature Sensor',
                    area='Storage Area',
                    exact_location='Cold Storage Unit',
                    manufacturer='Honeywell',
                    model='STT300',
                    serial_number='SN002347',
                    installation_date=datetime(2023, 6, 1).date(),
                    last_calibration=datetime(2024, 6, 1).date(),
                    next_calibration=datetime(2024, 12, 1).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Cold storage temperature monitoring'
                ),
                Sensor(
                    sensor_id='FLOW-001',
                    sensor_name='Flow Meter 1',
                    analyzer_type='Flow Meter',
                    area='Production Line B',
                    exact_location='Pipe Section 3',
                    manufacturer='Krohne',
                    model='Optiflux 4300',
                    serial_number='SN003456',
                    installation_date=datetime(2023, 3, 10).date(),
                    last_calibration=datetime(2024, 3, 10).date(),
                    next_calibration=datetime(2024, 9, 10).date(),
                    working_condition='Faulty',
                    status='Inactive',
                    remarks='Currently under maintenance'
                ),
                Sensor(
                    sensor_id='FLOW-002',
                    sensor_name='Flow Meter 2',
                    analyzer_type='Flow Meter',
                    area='Production Line A',
                    exact_location='Main Inlet Pipe',
                    manufacturer='Krohne',
                    model='Optiflux 4300',
                    serial_number='SN003457',
                    installation_date=datetime(2023, 4, 20).date(),
                    last_calibration=datetime(2024, 4, 20).date(),
                    next_calibration=datetime(2024, 10, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Main inlet flow measurement'
                ),
                Sensor(
                    sensor_id='COND-001',
                    sensor_name='Conductivity Sensor 1',
                    analyzer_type='Conductivity Analyzer',
                    area='Production Line C',
                    exact_location='Mixing Tank',
                    manufacturer='Endress+Hauser',
                    model='Indumax CLS50D',
                    serial_number='SN004567',
                    installation_date=datetime(2023, 4, 5).date(),
                    last_calibration=datetime(2024, 4, 5).date(),
                    next_calibration=datetime(2024, 10, 5).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Conductivity monitoring for mixing process'
                ),
                Sensor(
                    sensor_id='COND-002',
                    sensor_name='Conductivity Sensor 2',
                    analyzer_type='Conductivity Analyzer',
                    area='Water Treatment',
                    exact_location='Effluent Tank',
                    manufacturer='Endress+Hauser',
                    model='Indumax CLS50D',
                    serial_number='SN004568',
                    installation_date=datetime(2023, 5, 25).date(),
                    last_calibration=datetime(2024, 5, 25).date(),
                    next_calibration=datetime(2024, 11, 25).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Effluent conductivity monitoring'
                ),
                Sensor(
                    sensor_id='DO-001',
                    sensor_name='Dissolved Oxygen Sensor 1',
                    analyzer_type='DO Analyzer',
                    area='Production Line A',
                    exact_location='Aeration Tank',
                    manufacturer='Hach',
                    model='LDO101',
                    serial_number='SN005678',
                    installation_date=datetime(2023, 5, 15).date(),
                    last_calibration=datetime(2024, 5, 15).date(),
                    next_calibration=datetime(2024, 11, 15).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Dissolved oxygen monitoring for aeration process'
                ),
                Sensor(
                    sensor_id='DO-002',
                    sensor_name='Dissolved Oxygen Sensor 2',
                    analyzer_type='DO Analyzer',
                    area='Water Treatment',
                    exact_location='Bioreactor',
                    manufacturer='Hach',
                    model='LDO101',
                    serial_number='SN005679',
                    installation_date=datetime(2023, 7, 10).date(),
                    last_calibration=datetime(2024, 7, 10).date(),
                    next_calibration=datetime(2025, 1, 10).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Bioreactor dissolved oxygen monitoring'
                ),
                Sensor(
                    sensor_id='TURB-001',
                    sensor_name='Turbidity Sensor 1',
                    analyzer_type='Turbidity Analyzer',
                    area='Water Treatment',
                    exact_location='Clarifier Outlet',
                    manufacturer='Hach',
                    model='1720E',
                    serial_number='SN006789',
                    installation_date=datetime(2023, 8, 5).date(),
                    last_calibration=datetime(2024, 8, 5).date(),
                    next_calibration=datetime(2025, 2, 5).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Clarifier effluent turbidity monitoring'
                ),
                Sensor(
                    sensor_id='ORP-001',
                    sensor_name='ORP Sensor 1',
                    analyzer_type='ORP Analyzer',
                    area='Production Line A',
                    exact_location='Chemical Dosing Point',
                    manufacturer='Emerson',
                    model='Rosemount 1056',
                    serial_number='SN007890',
                    installation_date=datetime(2023, 9, 20).date(),
                    last_calibration=datetime(2024, 9, 20).date(),
                    next_calibration=datetime(2025, 3, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Oxidation reduction potential monitoring'
                ),
                Sensor(
                    sensor_id='LEVEL-001',
                    sensor_name='Level Sensor 1',
                    analyzer_type='Level Transmitter',
                    area='Storage Area',
                    exact_location='Tank 3',
                    manufacturer='Siemens',
                    model='SITRANS LR',
                    serial_number='SN008901',
                    installation_date=datetime(2023, 10, 15).date(),
                    last_calibration=datetime(2024, 10, 15).date(),
                    next_calibration=datetime(2025, 4, 15).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Tank 3 level measurement'
                ),
                Sensor(
                    sensor_id='PRESS-001',
                    sensor_name='Pressure Sensor 1',
                    analyzer_type='Pressure Transmitter',
                    area='Production Line B',
                    exact_location='Compressor Outlet',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN009012',
                    installation_date=datetime(2023, 11, 1).date(),
                    last_calibration=datetime(2024, 11, 1).date(),
                    next_calibration=datetime(2025, 5, 1).date(),
                    working_condition='Faulty',
                    status='Inactive',
                    remarks='Pressure sensor drift detected - needs recalibration'
                ),
                Sensor(
                    sensor_id='PRESS-002',
                    sensor_name='Pressure Sensor 2',
                    analyzer_type='Pressure Transmitter',
                    area='Production Line A',
                    exact_location='Steam Line',
                    manufacturer='Rosemount',
                    model='3051S',
                    serial_number='SN009013',
                    installation_date=datetime(2023, 12, 10).date(),
                    last_calibration=datetime(2024, 12, 10).date(),
                    next_calibration=datetime(2025, 6, 10).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Steam line pressure monitoring'
                ),
                Sensor(
                    sensor_id='PH-003',
                    sensor_name='pH Analyzer 3',
                    analyzer_type='pH Analyzer',
                    area='Production Line C',
                    exact_location='Neutralization Tank',
                    manufacturer='Mettler Toledo',
                    model='InPro 4260',
                    serial_number='SN010123',
                    installation_date=datetime(2024, 1, 5).date(),
                    last_calibration=datetime(2024, 1, 5).date(),
                    next_calibration=datetime(2024, 7, 5).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Neutralization pH monitoring'
                ),
                Sensor(
                    sensor_id='PH-004',
                    sensor_name='pH Analyzer 4',
                    analyzer_type='pH Analyzer',
                    area='Water Treatment',
                    exact_location='pH Adjustment Tank',
                    manufacturer='Mettler Toledo',
                    model='InPro 4260',
                    serial_number='SN010124',
                    installation_date=datetime(2024, 2, 15).date(),
                    last_calibration=datetime(2024, 2, 15).date(),
                    next_calibration=datetime(2024, 8, 15).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='pH adjustment monitoring'
                ),
                Sensor(
                    sensor_id='TEMP-004',
                    sensor_name='Temperature Sensor 4',
                    analyzer_type='Temperature Sensor',
                    area='Production Line B',
                    exact_location='Cooling Tower',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN011234',
                    installation_date=datetime(2024, 3, 1).date(),
                    last_calibration=datetime(2024, 3, 1).date(),
                    next_calibration=datetime(2024, 9, 1).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Cooling tower temperature monitoring'
                ),
                Sensor(
                    sensor_id='TEMP-005',
                    sensor_name='Temperature Sensor 5',
                    analyzer_type='Temperature Sensor',
                    area='Production Line A',
                    exact_location='Distillation Column',
                    manufacturer='Yokogawa',
                    model='YTA510',
                    serial_number='SN011235',
                    installation_date=datetime(2024, 4, 10).date(),
                    last_calibration=datetime(2024, 4, 10).date(),
                    next_calibration=datetime(2024, 10, 10).date(),
                    working_condition='Faulty',
                    status='Inactive',
                    remarks='Temperature sensor failure - needs replacement'
                ),
                Sensor(
                    sensor_id='FLOW-003',
                    sensor_name='Flow Meter 3',
                    analyzer_type='Flow Meter',
                    area='Production Line C',
                    exact_location='Recirculation Line',
                    manufacturer='Endress+Hauser',
                    model='Promag 53',
                    serial_number='SN012345',
                    installation_date=datetime(2024, 5, 20).date(),
                    last_calibration=datetime(2024, 5, 20).date(),
                    next_calibration=datetime(2024, 11, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Recirculation flow measurement'
                ),
                Sensor(
                    sensor_id='FLOW-004',
                    sensor_name='Flow Meter 4',
                    analyzer_type='Flow Meter',
                    area='Water Treatment',
                    exact_location='Influent Line',
                    manufacturer='Endress+Hauser',
                    model='Promag 53',
                    serial_number='SN012346',
                    installation_date=datetime(2024, 6, 5).date(),
                    last_calibration=datetime(2024, 6, 5).date(),
                    next_calibration=datetime(2024, 12, 5).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Influent flow measurement'
                ),
                Sensor(
                    sensor_id='COND-003',
                    sensor_name='Conductivity Sensor 3',
                    analyzer_type='Conductivity Analyzer',
                    area='Production Line A',
                    exact_location='Demineralization Unit',
                    manufacturer='Hach',
                    model='SC450',
                    serial_number='SN013456',
                    installation_date=datetime(2024, 7, 15).date(),
                    last_calibration=datetime(2024, 7, 15).date(),
                    next_calibration=datetime(2025, 1, 15).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Demineralization conductivity monitoring'
                ),
                Sensor(
                    sensor_id='COND-004',
                    sensor_name='Conductivity Sensor 4',
                    analyzer_type='Conductivity Analyzer',
                    area='Storage Area',
                    exact_location='Chemical Tank',
                    manufacturer='Hach',
                    model='SC450',
                    serial_number='SN013457',
                    installation_date=datetime(2024, 8, 25).date(),
                    last_calibration=datetime(2024, 8, 25).date(),
                    next_calibration=datetime(2025, 2, 25).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Chemical tank conductivity monitoring'
                ),
                Sensor(
                    sensor_id='DO-003',
                    sensor_name='Dissolved Oxygen Sensor 3',
                    analyzer_type='DO Analyzer',
                    area='Production Line B',
                    exact_location='Fermentation Tank',
                    manufacturer='Mettler Toledo',
                    model='InPro 6850i',
                    serial_number='SN014567',
                    installation_date=datetime(2024, 9, 10).date(),
                    last_calibration=datetime(2024, 9, 10).date(),
                    next_calibration=datetime(2025, 3, 10).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Fermentation DO monitoring'
                ),
                Sensor(
                    sensor_id='DO-004',
                    sensor_name='Dissolved Oxygen Sensor 4',
                    analyzer_type='DO Analyzer',
                    area='Water Treatment',
                    exact_location='Aeration Basin 2',
                    manufacturer='Mettler Toledo',
                    model='InPro 6850i',
                    serial_number='SN014568',
                    installation_date=datetime(2024, 10, 5).date(),
                    last_calibration=datetime(2024, 10, 5).date(),
                    next_calibration=datetime(2025, 4, 5).date(),
                    working_condition='Faulty',
                    status='Inactive',
                    remarks='DO sensor calibration drift detected'
                ),
                Sensor(
                    sensor_id='TURB-002',
                    sensor_name='Turbidity Sensor 2',
                    analyzer_type='Turbidity Analyzer',
                    area='Production Line A',
                    exact_location='Filtration Unit',
                    manufacturer='Endress+Hauser',
                    model='CUS50D',
                    serial_number='SN015678',
                    installation_date=datetime(2024, 11, 20).date(),
                    last_calibration=datetime(2024, 11, 20).date(),
                    next_calibration=datetime(2025, 5, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Filtration unit turbidity monitoring'
                ),
                Sensor(
                    sensor_id='TURB-003',
                    sensor_name='Turbidity Sensor 3',
                    analyzer_type='Turbidity Analyzer',
                    area='Water Treatment',
                    exact_location='Sand Filter Outlet',
                    manufacturer='Endress+Hauser',
                    model='CUS50D',
                    serial_number='SN015679',
                    installation_date=datetime(2024, 12, 1).date(),
                    last_calibration=datetime(2024, 12, 1).date(),
                    next_calibration=datetime(2025, 6, 1).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Sand filter turbidity monitoring'
                ),
                Sensor(
                    sensor_id='ORP-002',
                    sensor_name='ORP Sensor 2',
                    analyzer_type='ORP Analyzer',
                    area='Production Line B',
                    exact_location='Oxidation Tank',
                    manufacturer='Hach',
                    model='PPR',
                    serial_number='SN016789',
                    installation_date=datetime(2025, 1, 15).date(),
                    last_calibration=datetime(2025, 1, 15).date(),
                    next_calibration=datetime(2025, 7, 15).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Oxidation tank ORP monitoring'
                ),
                Sensor(
                    sensor_id='ORP-003',
                    sensor_name='ORP Sensor 3',
                    analyzer_type='ORP Analyzer',
                    area='Water Treatment',
                    exact_location='Disinfection Point',
                    manufacturer='Hach',
                    model='PPR',
                    serial_number='SN016790',
                    installation_date=datetime(2025, 2, 28).date(),
                    last_calibration=datetime(2025, 2, 28).date(),
                    next_calibration=datetime(2025, 8, 28).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Disinfection ORP monitoring'
                ),
                Sensor(
                    sensor_id='LEVEL-002',
                    sensor_name='Level Sensor 2',
                    analyzer_type='Level Transmitter',
                    area='Production Line B',
                    exact_location='Tank 4',
                    manufacturer='Vega',
                    model='VEGAPULS 62',
                    serial_number='SN017890',
                    installation_date=datetime(2025, 3, 10).date(),
                    last_calibration=datetime(2025, 3, 10).date(),
                    next_calibration=datetime(2025, 9, 10).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Tank 4 level measurement'
                ),
                Sensor(
                    sensor_id='LEVEL-003',
                    sensor_name='Level Sensor 3',
                    analyzer_type='Level Transmitter',
                    area='Storage Area',
                    exact_location='Tank 5',
                    manufacturer='Vega',
                    model='VEGAPULS 62',
                    serial_number='SN017891',
                    installation_date=datetime(2025, 4, 5).date(),
                    last_calibration=datetime(2025, 4, 5).date(),
                    next_calibration=datetime(2025, 10, 5).date(),
                    working_condition='Faulty',
                    status='Inactive',
                    remarks='Level sensor malfunction - under investigation'
                ),
                Sensor(
                    sensor_id='PRESS-003',
                    sensor_name='Pressure Sensor 3',
                    analyzer_type='Pressure Transmitter',
                    area='Production Line C',
                    exact_location='Pump Discharge',
                    manufacturer='ABB',
                    model='266HST',
                    serial_number='SN018901',
                    installation_date=datetime(2025, 5, 20).date(),
                    last_calibration=datetime(2025, 5, 20).date(),
                    next_calibration=datetime(2025, 11, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Pump discharge pressure monitoring'
                ),
                Sensor(
                    sensor_id='PRESS-004',
                    sensor_name='Pressure Sensor 4',
                    analyzer_type='Pressure Transmitter',
                    area='Production Line A',
                    exact_location='Gas Line',
                    manufacturer='ABB',
                    model='266HST',
                    serial_number='SN018902',
                    installation_date=datetime(2025, 6, 15).date(),
                    last_calibration=datetime(2025, 6, 15).date(),
                    next_calibration=datetime(2025, 12, 15).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Gas line pressure monitoring'
                ),
                Sensor(
                    sensor_id='PH-005',
                    sensor_name='pH Analyzer 5',
                    analyzer_type='pH Analyzer',
                    area='Production Line B',
                    exact_location='Reaction Vessel',
                    manufacturer='Yokogawa',
                    model='pH8',
                    serial_number='SN019012',
                    installation_date=datetime(2025, 7, 1).date(),
                    last_calibration=datetime(2025, 7, 1).date(),
                    next_calibration=datetime(2026, 1, 1).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Reaction vessel pH monitoring'
                ),
                Sensor(
                    sensor_id='PH-006',
                    sensor_name='pH Analyzer 6',
                    analyzer_type='pH Analyzer',
                    area='Water Treatment',
                    exact_location='Sludge Tank',
                    manufacturer='Yokogawa',
                    model='pH8',
                    serial_number='SN019013',
                    installation_date=datetime(2025, 8, 10).date(),
                    last_calibration=datetime(2025, 8, 10).date(),
                    next_calibration=datetime(2026, 2, 10).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Sludge tank pH monitoring'
                ),
                Sensor(
                    sensor_id='TEMP-006',
                    sensor_name='Temperature Sensor 6',
                    analyzer_type='Temperature Sensor',
                    area='Production Line C',
                    exact_location='Dryer Unit',
                    manufacturer='Honeywell',
                    model='STT350',
                    serial_number='SN020123',
                    installation_date=datetime(2025, 9, 25).date(),
                    last_calibration=datetime(2025, 9, 25).date(),
                    next_calibration=datetime(2026, 3, 25).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Dryer unit temperature monitoring'
                ),
                Sensor(
                    sensor_id='TEMP-007',
                    sensor_name='Temperature Sensor 7',
                    analyzer_type='Temperature Sensor',
                    area='Storage Area',
                    exact_location='Hot Oil Tank',
                    manufacturer='Honeywell',
                    model='STT350',
                    serial_number='SN020124',
                    installation_date=datetime(2025, 10, 15).date(),
                    last_calibration=datetime(2025, 10, 15).date(),
                    next_calibration=datetime(2026, 4, 15).date(),
                    working_condition='Faulty',
                    status='Inactive',
                    remarks='Temperature sensor reading erratic'
                ),
                Sensor(
                    sensor_id='FLOW-005',
                    sensor_name='Flow Meter 5',
                    analyzer_type='Flow Meter',
                    area='Production Line A',
                    exact_location='Bypass Line',
                    manufacturer='Siemens',
                    model='SITRANS F M',
                    serial_number='SN021234',
                    installation_date=datetime(2025, 11, 5).date(),
                    last_calibration=datetime(2025, 11, 5).date(),
                    next_calibration=datetime(2026, 5, 5).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Bypass line flow measurement'
                ),
                Sensor(
                    sensor_id='FLOW-006',
                    sensor_name='Flow Meter 6',
                    analyzer_type='Flow Meter',
                    area='Production Line B',
                    exact_location='Transfer Line',
                    manufacturer='Siemens',
                    model='SITRANS F M',
                    serial_number='SN021235',
                    installation_date=datetime(2025, 12, 20).date(),
                    last_calibration=datetime(2025, 12, 20).date(),
                    next_calibration=datetime(2026, 6, 20).date(),
                    working_condition='Working',
                    status='Active',
                    remarks='Transfer line flow measurement'
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
                    sensor_id='FLOW-001',
                    issue='Flow meter showing erratic readings',
                    priority='High',
                    status='In Progress',
                    assigned_engineer='John Smith',
                    raised_date=datetime(2024, 6, 1).date(),
                    description='Flow meter is showing fluctuating readings that don match actual flow rates',
                    root_cause='Sensor calibration drift',
                    corrective_action='Pending recalibration'
                ),
                Maintenance(
                    sensor_id='PH-001',
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
                    sensor_id='TEMP-002',
                    issue='Temperature sensor not responding',
                    priority='High',
                    status='Pending',
                    assigned_engineer='Mike Johnson',
                    raised_date=datetime(2024, 6, 10).date(),
                    description='Temperature sensor stopped responding after power fluctuation',
                    root_cause='Possible electronic component failure',
                    corrective_action='Awaiting diagnostic test results'
                ),
                Maintenance(
                    sensor_id='PRESS-001',
                    issue='Pressure sensor drift detected',
                    priority='Medium',
                    status='In Progress',
                    assigned_engineer='Sarah Williams',
                    raised_date=datetime(2024, 6, 15).date(),
                    description='Pressure sensor readings drifting from expected values',
                    root_cause='Calibration drift due to environmental conditions',
                    corrective_action='Recalibration in progress'
                ),
                Maintenance(
                    sensor_id='DO-004',
                    issue='DO sensor calibration drift',
                    priority='Medium',
                    status='Pending',
                    assigned_engineer='John Smith',
                    raised_date=datetime(2024, 6, 20).date(),
                    description='Dissolved oxygen sensor showing inconsistent readings',
                    root_cause='Sensor membrane degradation',
                    corrective_action='Membrane replacement scheduled'
                ),
                Maintenance(
                    sensor_id='LEVEL-003',
                    issue='Level sensor malfunction',
                    priority='High',
                    status='In Progress',
                    assigned_engineer='Jane Doe',
                    raised_date=datetime(2024, 6, 25).date(),
                    description='Level sensor giving erratic readings',
                    root_cause='Signal interference from nearby equipment',
                    corrective_action='Shielding installation in progress'
                ),
                Maintenance(
                    sensor_id='TEMP-007',
                    issue='Temperature sensor reading erratic',
                    priority='High',
                    status='Pending',
                    assigned_engineer='Mike Johnson',
                    raised_date=datetime(2024, 6, 28).date(),
                    description='Temperature sensor in hot oil tank showing unstable readings',
                    root_cause='Thermal stress on sensor components',
                    corrective_action='Sensor replacement pending'
                ),
                Maintenance(
                    sensor_id='COND-001',
                    issue='Routine sensor cleaning',
                    priority='Low',
                    status='Completed',
                    assigned_engineer='Sarah Williams',
                    raised_date=datetime(2024, 5, 1).date(),
                    completed_date=datetime(2024, 5, 3).date(),
                    description='Scheduled cleaning of conductivity sensor',
                    root_cause='N/A - Routine maintenance',
                    corrective_action='Sensor cleaned and calibrated'
                ),
                Maintenance(
                    sensor_id='TURB-001',
                    issue='Turbidity sensor fouling',
                    priority='Medium',
                    status='Completed',
                    assigned_engineer='John Smith',
                    raised_date=datetime(2024, 4, 15).date(),
                    completed_date=datetime(2024, 4, 18).date(),
                    description='Turbidity sensor showing reduced sensitivity',
                    root_cause='Sensor fouling due to particulate buildup',
                    corrective_action='Sensor cleaned and recalibrated'
                ),
                Maintenance(
                    sensor_id='ORP-001',
                    issue='ORP sensor replacement',
                    priority='High',
                    status='Completed',
                    assigned_engineer='Jane Doe',
                    raised_date=datetime(2024, 3, 20).date(),
                    completed_date=datetime(2024, 3, 25).date(),
                    description='ORP sensor failed calibration test',
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
                    sensor_id='PH-001',
                    last_calibration=datetime(2024, 1, 15).date(),
                    next_calibration=datetime(2024, 7, 15).date(),
                    calibrated_by='John Smith',
                    remarks='Quarterly calibration completed successfully'
                ),
                Calibration(
                    sensor_id='PH-002',
                    last_calibration=datetime(2024, 2, 10).date(),
                    next_calibration=datetime(2024, 8, 10).date(),
                    calibrated_by='Jane Doe',
                    remarks='Quarterly calibration completed'
                ),
                Calibration(
                    sensor_id='TEMP-001',
                    last_calibration=datetime(2024, 2, 20).date(),
                    next_calibration=datetime(2024, 8, 20).date(),
                    calibrated_by='Jane Doe',
                    remarks='Bi-annual calibration completed'
                ),
                Calibration(
                    sensor_id='TEMP-003',
                    last_calibration=datetime(2024, 6, 1).date(),
                    next_calibration=datetime(2024, 12, 1).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Annual calibration completed'
                ),
                Calibration(
                    sensor_id='FLOW-001',
                    last_calibration=datetime(2024, 3, 10).date(),
                    next_calibration=datetime(2024, 9, 10).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Semi-annual calibration completed'
                ),
                Calibration(
                    sensor_id='FLOW-002',
                    last_calibration=datetime(2024, 4, 20).date(),
                    next_calibration=datetime(2024, 10, 20).date(),
                    calibrated_by='John Smith',
                    remarks='Semi-annual calibration completed'
                ),
                Calibration(
                    sensor_id='COND-001',
                    last_calibration=datetime(2024, 4, 5).date(),
                    next_calibration=datetime(2024, 10, 5).date(),
                    calibrated_by='John Smith',
                    remarks='Semi-annual calibration completed'
                ),
                Calibration(
                    sensor_id='COND-002',
                    last_calibration=datetime(2024, 5, 25).date(),
                    next_calibration=datetime(2024, 11, 25).date(),
                    calibrated_by='Jane Doe',
                    remarks='Semi-annual calibration completed'
                ),
                Calibration(
                    sensor_id='DO-001',
                    last_calibration=datetime(2024, 5, 15).date(),
                    next_calibration=datetime(2024, 11, 15).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Quarterly calibration completed'
                ),
                Calibration(
                    sensor_id='DO-002',
                    last_calibration=datetime(2024, 7, 10).date(),
                    next_calibration=datetime(2025, 1, 10).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Quarterly calibration completed'
                ),
                Calibration(
                    sensor_id='TURB-001',
                    last_calibration=datetime(2024, 8, 5).date(),
                    next_calibration=datetime(2025, 2, 5).date(),
                    calibrated_by='John Smith',
                    remarks='Semi-annual calibration completed'
                ),
                Calibration(
                    sensor_id='ORP-001',
                    last_calibration=datetime(2024, 9, 20).date(),
                    next_calibration=datetime(2025, 3, 20).date(),
                    calibrated_by='Jane Doe',
                    remarks='Quarterly calibration completed'
                ),
                Calibration(
                    sensor_id='LEVEL-001',
                    last_calibration=datetime(2024, 10, 15).date(),
                    next_calibration=datetime(2025, 4, 15).date(),
                    calibrated_by='Mike Johnson',
                    remarks='Annual calibration completed'
                ),
                Calibration(
                    sensor_id='PRESS-001',
                    last_calibration=datetime(2024, 11, 1).date(),
                    next_calibration=datetime(2025, 5, 1).date(),
                    calibrated_by='Sarah Williams',
                    remarks='Semi-annual calibration completed'
                ),
                Calibration(
                    sensor_id='PRESS-002',
                    last_calibration=datetime(2024, 12, 10).date(),
                    next_calibration=datetime(2025, 6, 10).date(),
                    calibrated_by='John Smith',
                    remarks='Semi-annual calibration completed'
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
            
            activity = ActivityLog(
                user='System',
                action='Database initialized with sample data',
                timestamp=datetime.utcnow()
            )
            db.session.add(activity)
            db.session.commit()
            print("Initial activity log created.")
        else:
            print("Activity log already exists, skipping activity log creation.")
        
        print("\nDatabase initialization completed successfully!")
        print("\nDefault login credentials:")
        print("Admin: username=admin, password=admin123")
        print("Engineer: username=engineer, password=eng123")

if __name__ == '__main__':
    init_database()
