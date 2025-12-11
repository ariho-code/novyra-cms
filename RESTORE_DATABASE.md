# Restore Database and Fix Missing Content

## Problem
After deployment, the website is showing but all sections are empty because:
1. Database migrations may not have run
2. Database tables might be empty
3. SiteSettings might not be initialized

## Solution

### Step 1: Run Migrations on Render

1. Go to **Render Dashboard** → Your Service → **Shell**
2. Run these commands:

```bash
# Run migrations
python manage.py migrate

# Initialize SiteSettings
python manage.py shell
```

3. In the Python shell, run:
```python
from settings_app.models import SiteSettings
settings, created = SiteSettings.objects.get_or_create(pk=1)
print("SiteSettings created!" if created else "SiteSettings exists!")
exit()
```

### Step 2: Create Superuser (if needed)

If you can't login, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 3: Verify Database

Check if tables exist:

```bash
python manage.py shell
```

```python
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", [t[0] for t in tables])
exit()
```

### Step 4: Add Initial Content

Once logged in to CMS:

1. Go to **CMS** → **Site Settings**
2. Fill in basic site information
3. Go to **CMS** → **Homepage Sections**
4. Add sections (Hero, Features, Services, etc.)
5. Go to **CMS** → **Services**
6. Add your services
7. Go to **CMS** → **About Page**
8. Add about content

## Automatic Fix (Already Applied)

The code now includes:
- ✅ `init_db.py` - Database initialization script
- ✅ `start.sh` - Startup script that runs migrations
- ✅ Build command includes migrations
- ✅ SiteSettings auto-initialization

## If Still Empty After Fix

The database might be getting wiped on each deploy (SQLite limitation on Render). 

**Option 1: Use PostgreSQL (Recommended)**
- Render provides free PostgreSQL
- Database persists across deploys
- See `SWITCH_TO_POSTGRESQL.md` for instructions

**Option 2: Re-add Content**
- After each deploy, re-add content through CMS
- Or export/import data

## Quick Fix Command

Run this in Render Shell to quickly initialize everything:

```bash
python manage.py migrate && python init_db.py
```

Then login to CMS and add your content back.

