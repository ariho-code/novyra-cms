"""
One-time initialization views accessible via browser
Use these when you can't access Render shell
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import connection
from django.core.management import call_command
from django.http import JsonResponse
import os


def init_database(request):
    """
    Initialize database - accessible via browser
    URL: /init-database/
    """
    if request.method != 'POST':
        return render(request, 'init_database.html', {
            'title': 'Initialize Database'
        })
    
    results = []
    success = True
    
    # Run migrations
    try:
        call_command('migrate', verbosity=0, interactive=False)
        results.append(('Migrations', 'OK', 'All migrations applied'))
    except Exception as e:
        results.append(('Migrations', 'ERROR', str(e)))
        success = False
    
    # Initialize SiteSettings
    try:
        from settings_app.models import SiteSettings
        settings, created = SiteSettings.objects.get_or_create(pk=1)
        if created:
            results.append(('SiteSettings', 'CREATED', 'SiteSettings initialized'))
        else:
            results.append(('SiteSettings', 'EXISTS', 'SiteSettings already exists'))
    except Exception as e:
        results.append(('SiteSettings', 'ERROR', str(e)))
        success = False
    
    # Check for superuser
    try:
        has_superuser = User.objects.filter(is_superuser=True).exists()
        if has_superuser:
            results.append(('Superuser', 'EXISTS', 'Superuser found'))
        else:
            results.append(('Superuser', 'MISSING', 'No superuser - use /create-admin/ to create one'))
    except Exception as e:
        results.append(('Superuser', 'ERROR', str(e)))
    
    return render(request, 'init_result.html', {
        'title': 'Database Initialization',
        'results': results,
        'success': success
    })


def create_admin(request):
    """
    Create admin user - accessible via browser
    URL: /create-admin/
    """
    if request.method != 'POST':
        return render(request, 'create_admin.html', {
            'title': 'Create Admin User'
        })
    
    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip()
    password = request.POST.get('password', '').strip()
    password_confirm = request.POST.get('password_confirm', '').strip()
    
    errors = []
    
    if not username:
        errors.append('Username is required')
    if not email:
        errors.append('Email is required')
    if not password:
        errors.append('Password is required')
    if password != password_confirm:
        errors.append('Passwords do not match')
    if len(password) < 8:
        errors.append('Password must be at least 8 characters')
    
    if errors:
        return render(request, 'create_admin.html', {
            'title': 'Create Admin User',
            'errors': errors,
            'username': username,
            'email': email
        })
    
    # Check if user exists
    if User.objects.filter(username=username).exists():
        return render(request, 'create_admin.html', {
            'title': 'Create Admin User',
            'errors': ['Username already exists']
        })
    
    # Create superuser
    try:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, f'Admin user "{username}" created successfully! You can now login.')
        return redirect('accounts:login')
    except Exception as e:
        return render(request, 'create_admin.html', {
            'title': 'Create Admin User',
            'errors': [f'Error creating user: {str(e)}']
        })


def check_database(request):
    """
    Check database status - accessible via browser
    URL: /check-database/
    """
    status = {
        'migrations': 'unknown',
        'tables': [],
        'site_settings': 'unknown',
        'users': 0,
        'superusers': 0
    }
    
    try:
        # Check tables
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        status['tables'] = [row[0] for row in cursor.fetchall()]
        status['migrations'] = 'OK' if len(status['tables']) > 0 else 'NO TABLES'
    except Exception as e:
        status['migrations'] = f'ERROR: {str(e)}'
    
    try:
        from settings_app.models import SiteSettings
        if SiteSettings.objects.exists():
            status['site_settings'] = 'EXISTS'
        else:
            status['site_settings'] = 'MISSING'
    except Exception as e:
        status['site_settings'] = f'ERROR: {str(e)}'
    
    try:
        status['users'] = User.objects.count()
        status['superusers'] = User.objects.filter(is_superuser=True).count()
    except Exception as e:
        status['users'] = f'ERROR: {str(e)}'
    
    return render(request, 'check_database.html', {
        'title': 'Database Status',
        'status': status
    })


def import_data(request):
    """
    Import data from JSON file - accessible via browser
    URL: /import-data/
    """
    if request.method != 'POST':
        return render(request, 'import_data.html', {
            'title': 'Import Data from Local Database'
        })
    
    if 'data_file' not in request.FILES:
        return render(request, 'import_data.html', {
            'title': 'Import Data',
            'error': 'Please select a JSON file to import'
        })
    
    data_file = request.FILES['data_file']
    
    # Read JSON file
    try:
        import json
        data = json.loads(data_file.read().decode('utf-8'))
    except Exception as e:
        return render(request, 'import_data.html', {
            'title': 'Import Data',
            'error': f'Error reading JSON file: {str(e)}'
        })
    
    # Import data
    results = []
    try:
        from django.core.management import call_command
        from io import StringIO
        import tempfile
        import os
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(data, f, indent=2)
            temp_path = f.name
        
        try:
            # Load data
            call_command('loaddata', temp_path, verbosity=0)
            results.append(('Import', 'SUCCESS', f'Imported {len(data)} objects'))
        finally:
            # Clean up
            if os.path.exists(temp_path):
                os.unlink(temp_path)
                
    except Exception as e:
        results.append(('Import', 'ERROR', str(e)))
    
    return render(request, 'import_result.html', {
        'title': 'Data Import Result',
        'results': results
    })

