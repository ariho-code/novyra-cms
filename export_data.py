"""
Export database data to JSON file with proper UTF-8 encoding
"""
import os
import django
import sys
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novyra_cms.settings')
django.setup()

from django.core.management import call_command
from io import StringIO

def export_data():
    """Export all data to JSON file"""
    print("Exporting database data...")
    
    # Use StringIO to capture output
    output = StringIO()
    
    try:
        # Export data
        call_command('dumpdata', 
                    exclude=['contenttypes', 'auth.Permission', 'sessions'],
                    indent=2,
                    stdout=output)
        
        # Get the JSON string
        json_data = output.getvalue()
        
        # Write to file with UTF-8 encoding
        output_file = 'local_data_backup.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_data)
        
        print(f"✅ Data exported successfully to {output_file}")
        print(f"   File size: {os.path.getsize(output_file)} bytes")
        return True
        
    except Exception as e:
        print(f"❌ Error exporting data: {e}")
        return False

if __name__ == '__main__':
    success = export_data()
    sys.exit(0 if success else 1)

