# Render Deployment Fix

## Problem
After deploying to Render, the application showed this error:
```
OperationalError: no such table: settings_app_sitesettings
```

## Root Cause
The database migrations were not being run during the build process on Render. The database tables were never created.

## Solution Applied

### 1. Updated `render.yaml`
Added `python manage.py migrate --noinput` to the build command:
```yaml
buildCommand: pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput
```

### 2. Fixed DEBUG Setting
Updated `novyra_cms/settings.py` to properly handle DEBUG setting on Render:
- On Render: Defaults to `False` (production mode)
- Locally: Defaults to `True` (development mode)

### 3. Created `build.sh`
Added a build script for better error handling and logging during deployment.

## Next Steps

### Push Changes to GitHub
```powershell
# Refresh PATH (if needed)
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Push to GitHub
git push origin main
```

### Render Will Auto-Deploy
Once you push to GitHub, Render will:
1. Detect the changes
2. Run the new build command (which includes migrations)
3. Create all database tables
4. Deploy the application

### After Deployment
1. **Create Superuser** (if needed):
   - Go to Render Dashboard → Your Service → Shell
   - Run: `python manage.py createsuperuser`

2. **Initialize Site Settings** (if needed):
   - In Shell, run: `python manage.py shell`
   - Then: 
     ```python
     from settings_app.models import SiteSettings
     SiteSettings.load()
     exit()
     ```

## Verification
After deployment, check:
- ✅ Website loads without errors
- ✅ Database tables exist
- ✅ CMS login page works
- ✅ No "no such table" errors

## Files Changed
- `render.yaml` - Added migrations to build command
- `novyra_cms/settings.py` - Fixed DEBUG setting for Render
- `build.sh` - Added build script (optional)

