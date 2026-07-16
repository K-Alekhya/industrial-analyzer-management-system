# Industrial Analyzer Management System

A comprehensive web-based application for managing industrial analyzers, sensors, maintenance schedules, and calibration records.

## Features

### Authentication
- User login with role-based access (Admin/Engineer)
- Secure password hashing
- Session management
- Logout functionality

### Dashboard
- Real-time statistics overview
- Interactive charts (Pie chart for sensor status, Bar chart for maintenance status)
- Recent activity log
- Upcoming calibrations display
- Key metrics: Total sensors, Working/Faulty sensors, Calibration due, Maintenance status

### Sensor Management
- Add, edit, delete sensors
- View detailed sensor information
- Upload sensor images
- Search and filter sensors
- Pagination for large datasets
- Track installation details, calibration dates, working condition

### Maintenance
- Raise maintenance tickets
- Assign engineers to tickets
- Track priority levels (High, Medium, Low)
- Monitor ticket status (Pending, In Progress, Completed)
- Record root cause and corrective actions
- View maintenance history

### Calibration
- Add and edit calibration records
- Track last and next calibration dates
- View due calibrations (next 30 days)
- Calendar view of upcoming calibrations
- Record calibration technician and remarks

### Reports
- Export data in multiple formats (PDF, Excel, CSV)
- Filter by date range, area, and sensor type
- Generate reports for sensors, maintenance, and calibration

### Search
- Global search across all entities
- Search by sensor ID, analyzer type, area, location, status
- Quick access to relevant records

### Security
- CSRF protection on all forms
- SQL injection protection (SQLAlchemy ORM)
- Input validation
- Password hashing using Werkzeug

## Tech Stack

### Backend
- Python 3.12
- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- Flask-Login 0.6.3
- Flask-WTF 1.2.1
- SQLite database

### Frontend
- Bootstrap 5.3.0
- HTML5
- CSS3
- JavaScript (ES6+)

### Charts & Visualization
- Chart.js 4.4.0

### Icons
- Bootstrap Icons 1.11.0

### Reports
- ReportLab 4.0.7 (PDF generation)
- openpyxl 3.1.2 (Excel export)
- pandas 2.1.3 (CSV export)

## Project Structure

```
Industrial-Analyzer-Management-System/
├── app.py                      # Main application file
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── init_db.py                  # Database initialization script
├── database.db                 # SQLite database (created automatically)
├── models/                     # Database models
│   └── __init__.py            # User, Sensor, Maintenance, Calibration, ActivityLog
├── routes/                     # Application routes (blueprints)
│   ├── __init__.py
│   ├── auth.py                # Authentication routes
│   ├── dashboard.py           # Dashboard routes
│   ├── sensors.py             # Sensor management routes
│   ├── maintenance.py         # Maintenance routes
│   ├── calibration.py         # Calibration routes
│   ├── reports.py             # Report generation routes
│   └── search.py              # Search routes
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── auth/                  # Authentication templates
│   │   └── login.html
│   ├── dashboard/             # Dashboard templates
│   │   └── index.html
│   ├── sensors/               # Sensor templates
│   │   ├── index.html
│   │   ├── add.html
│   │   ├── edit.html
│   │   └── view.html
│   ├── maintenance/           # Maintenance templates
│   │   ├── index.html
│   │   ├── add.html
│   │   ├── edit.html
│   │   └── view.html
│   ├── calibration/           # Calibration templates
│   │   ├── index.html
│   │   ├── add.html
│   │   ├── edit.html
│   │   ├── due.html
│   │   └── calendar.html
│   ├── reports/               # Reports templates
│   │   └── index.html
│   ├── search/                # Search templates
│   │   └── index.html
│   └── errors/                # Error pages
│       ├── 404.html
│       └── 500.html
├── static/                     # Static files
│   ├── css/
│   │   └── style.css          # Custom styles
│   ├── js/
│   │   └── main.js            # Custom JavaScript
│   ├── images/                # Image assets
│   └── uploads/               # Uploaded sensor images
├── services/                   # Business logic (future expansion)
├── reports/                    # Generated reports
└── migrations/                 # Database migrations (future use)
```

## Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### Steps

1. **Navigate to the project directory**
   ```bash
   cd c:/Users/alekh/OneDrive/Desktop/ITC/app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the database**
   ```bash
   python init_db.py
   ```
   This will create the SQLite database and insert sample data.

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the application**
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Default Login Credentials

After running the initialization script, you can log in with:

- **Admin**: Username: `admin`, Password: `admin123`
- **Engineer**: Username: `engineer`, Password: `eng123`

**Note**: Change these passwords in production!

## Usage

### Dashboard
- View overall system statistics
- Monitor sensor status and maintenance tickets
- Check upcoming calibrations
- Review recent activity

### Managing Sensors
1. Navigate to Sensors from the sidebar
2. Click "Add Sensor" to register a new analyzer
3. Fill in the required fields (marked with *)
4. Optionally upload an image
5. Click "Add Sensor" to save

### Maintenance Tickets
1. Navigate to Maintenance from the sidebar
2. Click "Raise Ticket" to create a new maintenance request
3. Select the sensor, describe the issue, and set priority
4. Assign an engineer if needed
5. Track progress through the ticket lifecycle

### Calibration Records
1. Navigate to Calibration from the sidebar
2. Click "Add Record" to log a calibration
3. Select the sensor and enter calibration dates
4. Record who performed the calibration
5. View "Due Calibrations" to see sensors needing attention

### Reports
1. Navigate to Reports from the sidebar
2. Select the report type (Sensors, Maintenance, Calibration)
3. Choose the export format (PDF, Excel, CSV)
4. Apply filters if needed (date range, area)
5. Click the export button to download

### Search
1. Navigate to Search from the sidebar
2. Enter your search query
3. View results across sensors, maintenance, and calibration
4. Click on any result to view details

## Database Schema

### Users
- `id`: Primary key
- `username`: Unique username
- `password`: Hashed password
- `role`: Admin or Engineer

### Sensors
- `id`: Primary key
- `sensor_id`: Unique sensor identifier
- `sensor_name`: Sensor name
- `analyzer_type`: Type of analyzer
- `area`: Plant area/location
- `exact_location`: Specific location
- `manufacturer`: Equipment manufacturer
- `model`: Equipment model
- `serial_number`: Serial number
- `installation_date`: Installation date
- `last_calibration`: Last calibration date
- `next_calibration`: Next calibration due date
- `working_condition`: Working or Faulty
- `status`: Active or Inactive
- `remarks`: Additional notes
- `image_path`: Path to uploaded image

### Maintenance
- `id`: Primary key
- `sensor_id`: Foreign key to Sensors
- `issue`: Description of the issue
- `priority`: High, Medium, or Low
- `status`: Pending, In Progress, or Completed
- `assigned_engineer`: Assigned engineer name
- `raised_date`: Date ticket was raised
- `completed_date`: Date ticket was completed
- `description`: Detailed description
- `root_cause`: Root cause analysis
- `corrective_action`: Corrective action taken

### Calibration
- `id`: Primary key
- `sensor_id`: Foreign key to Sensors
- `last_calibration`: Last calibration date
- `next_calibration`: Next calibration due date
- `calibrated_by`: Name of technician
- `remarks`: Additional notes

### Activity Log
- `id`: Primary key
- `user`: Username who performed the action
- `action`: Description of the action
- `timestamp`: When the action occurred

## Screenshots

*Placeholder for application screenshots*

## Future Improvements

- [ ] Email notifications for calibration due dates
- [ ] Mobile app version
- [ ] Advanced analytics and reporting
- [ ] Integration with IoT sensors for real-time data
- [ ] Multi-language support
- [ ] Advanced permissions and access control
- [ ] API endpoints for external integrations
- [ ] Data backup and restore functionality
- [ ] Audit trail for all changes
- [ ] Custom dashboard widgets

## Troubleshooting

### Database Issues
If you encounter database errors, delete the `database.db` file and run `python init_db.py` again.

### Port Already in Use
If port 5000 is already in use, modify the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001 or another available port
```

### Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## License

This project is for educational and demonstration purposes.

## Support

For issues or questions, please contact the development team.

## Acknowledgments

- Flask and its ecosystem
- Bootstrap for the UI framework
- Chart.js for data visualization
- The open-source community
