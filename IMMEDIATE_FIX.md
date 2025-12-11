# IMMEDIATE FIX - Restore Website Content

## The Problem
- Homepage sections are empty
- CMS login not working
- All pages showing but no content

## Root Cause
The database is empty or migrations haven't run on Render.

## IMMEDIATE SOLUTION (Do This Now)

### Step 1: Go to Render Dashboard
1. Open https://dashboard.render.com
2. Click on your service: **novyra-cms**

### Step 2: Open Shell
1. Click **Shell** tab
2. Run these commands one by one:

```bash
# 1. Run migrations (creates all tables)
python manage.py migrate

# 2. Initialize SiteSettings
python manage.py shell
```

3. In the Python shell that opens, paste this:
```python
from settings_app.models import SiteSettings
settings, created = SiteSettings.objects.get_or_create(pk=1)
print("SiteSettings OK!" if created else "SiteSettings exists!")
exit()
```

### Step 3: Create Admin User
```bash
python manage.py createsuperuser
```

Enter:
- Username: (your choice)
- Email: (your email)
- Password: (strong password)

### Step 4: Test Login
1. Go to https://novyra-cms.onrender.com/cms/accounts/login/
2. Login with the credentials you just created
3. You should now be able to access CMS!

### Step 5: Add Content Back
Once logged in:

1. **Site Settings** (`/cms/settings/`)
   - Add site name, logo, contact info
   - Add social media handles

2. **Homepage Sections** (`/cms/website/homepage-sections/`)
   - Add Hero section
   - Add Features section
   - Add Services section
   - Add Process section
   - Add Team section
   - Add Testimonials section

3. **Services** (`/cms/website/service-pages/`)
   - Add your services

4. **About Page** (`/cms/website/about-page/`)
   - Add about content

5. **Footer** (`/cms/website/footer/`)
   - Add footer content

## Why This Happened

SQLite databases on Render are **ephemeral** - they get wiped on each deploy unless you use persistent storage. The error handling we added prevents crashes but shows empty content when the database is empty.

## Permanent Solution

**Option 1: Use PostgreSQL (Recommended)**
- Render provides free PostgreSQL
- Database persists across deploys
- See `SWITCH_TO_POSTGRESQL.md`

**Option 2: Keep SQLite but backup/restore**
- Export data before deploy
- Import after deploy

## Quick Commands Summary

```bash
# In Render Shell, run:
python manage.py migrate
python manage.py createsuperuser
python init_db.py
```

Then login and add your content!

---

**After following these steps, your website should be fully restored!**

