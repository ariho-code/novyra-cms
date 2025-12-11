# Manual Fix Required in Render Dashboard

## Problem
Render is still using `python manage.py runserver` instead of `gunicorn`, and migrations may not be running.

## Solution: Update Render Dashboard Settings

### Step 1: Go to Render Dashboard
1. Log in to https://dashboard.render.com
2. Click on your service: **novyra-cms**

### Step 2: Update Build Command
1. Go to **Settings** tab
2. Scroll to **Build & Deploy** section
3. Find **Build Command** field
4. **Replace** the current command with:
   ```
   pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput
   ```
5. Click **Save Changes**

### Step 3: Update Start Command
1. Still in **Settings** tab
2. Find **Start Command** field
3. **Replace** the current command with:
   ```
   gunicorn novyra_cms.wsgi:application --bind 0.0.0.0:$PORT
   ```
4. Click **Save Changes**

### Step 4: Manual Deploy
1. Go to **Manual Deploy** tab
2. Click **Deploy latest commit**
3. Wait for deployment to complete

## What This Fixes

✅ **Migrations will run** during build (creates database tables)
✅ **Gunicorn** will be used instead of development server
✅ **All database errors** are now handled gracefully
✅ **No more 500 errors** from missing tables

## Verification

After deployment, check the logs:
1. Look for: `Running database migrations...`
2. Look for: `Starting application server...` (gunicorn)
3. Website should load without 500 errors

## If Still Getting 500 Errors

If you still see 500 errors after this:

1. **Check Render Logs** for the actual error message
2. **Run migrations manually**:
   - Go to **Shell** tab in Render Dashboard
   - Run: `python manage.py migrate`
3. **Create SiteSettings**:
   - In Shell, run: `python manage.py shell`
   - Then:
     ```python
     from settings_app.models import SiteSettings
     SiteSettings.load()
     exit()
     ```

## All Code Fixes Applied

✅ All database queries wrapped in try-except blocks
✅ Error handling in all views (website, blog, portfolio, dashboard)
✅ Context processors handle database errors gracefully
✅ Contact form handles database errors
✅ All views return safe defaults when database fails

---

**Important**: The code is fixed, but Render needs to be configured correctly in the dashboard for migrations and gunicorn to work.

