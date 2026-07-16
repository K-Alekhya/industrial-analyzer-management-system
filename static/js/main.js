// Industrial Analyzer Management System - Main JavaScript

// Document ready function
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Auto-hide flash messages after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
    
    // Form validation
    var forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
    
    // Confirm delete actions
    var deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(function(button) {
        if (button.getAttribute('onclick') === null) {
            button.addEventListener('click', function(event) {
                if (!confirm('Are you sure you want to perform this action?')) {
                    event.preventDefault();
                }
            });
        }
    });
    
    // Search functionality enhancement
    var searchInputs = document.querySelectorAll('input[type="search"], input[name="search"]');
    searchInputs.forEach(function(input) {
        input.addEventListener('keyup', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                input.closest('form').submit();
            }
        });
    });
    
    // Date picker enhancements
    var dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        // Set minimum date to today for future dates
        if (input.id === 'next_calibration' || input.id === 'completed_date') {
            var today = new Date().toISOString().split('T')[0];
            input.setAttribute('min', today);
        }
    });
    
    // Loading spinner for form submissions - disabled to prevent blocking submissions
    // var submitButtons = document.querySelectorAll('button[type="submit"]');
    // submitButtons.forEach(function(button) {
    //     button.addEventListener('click', function() {
    //         var form = button.closest('form');
    //         if (form && form.checkValidity()) {
    //             button.disabled = true;
    //             button.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
    //         }
    //     });
    // });
    
    // Sidebar toggle for mobile
    var sidebarToggle = document.querySelector('.navbar-toggler');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            var sidebar = document.querySelector('.sidebar');
            if (sidebar) {
                sidebar.classList.toggle('show');
            }
        });
    }
    
    // Active link highlighting
    var currentPath = window.location.pathname;
    var navLinks = document.querySelectorAll('.sidebar .nav-link');
    navLinks.forEach(function(link) {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
    
    // Table row click for navigation
    var tableRows = document.querySelectorAll('tbody tr');
    tableRows.forEach(function(row) {
        row.addEventListener('click', function(event) {
            // Don't trigger if clicking on a button or link
            if (event.target.tagName !== 'BUTTON' && event.target.tagName !== 'A' && 
                !event.target.closest('button') && !event.target.closest('a')) {
                var viewLink = row.querySelector('a[href*="/view"]');
                if (viewLink) {
                    window.location.href = viewLink.getAttribute('href');
                }
            }
        });
    });
});

// Function to show loading spinner
function showSpinner() {
    var spinner = document.createElement('div');
    spinner.className = 'spinner-overlay';
    spinner.innerHTML = '<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>';
    document.body.appendChild(spinner);
}

// Function to hide loading spinner
function hideSpinner() {
    var spinner = document.querySelector('.spinner-overlay');
    if (spinner) {
        spinner.remove();
    }
}

// Function to format dates
function formatDate(dateString) {
    if (!dateString) return 'N/A';
    var date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

// Function to calculate days until due
function daysUntilDue(dueDate) {
    var today = new Date();
    var due = new Date(dueDate);
    var diffTime = due - today;
    var diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
}

// Function to export data (for reports)
function exportData(format, type) {
    showSpinner();
    // The actual export is handled by the server
    // This is just for UI feedback
}

// Function to refresh dashboard data
function refreshDashboard() {
    showSpinner();
    location.reload();
}

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
    // Ctrl/Cmd + K for search
    if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
        event.preventDefault();
        var searchInput = document.querySelector('input[name="q"], input[name="search"]');
        if (searchInput) {
            searchInput.focus();
        }
    }
    
    // Escape to close modals
    if (event.key === 'Escape') {
        var modals = document.querySelectorAll('.modal.show');
        modals.forEach(function(modal) {
            var bsModal = bootstrap.Modal.getInstance(modal);
            if (bsModal) {
                bsModal.hide();
            }
        });
    }
});

// Console message for debugging
console.log('Industrial Analyzer Management System loaded successfully');
