# Restore Your Original Website Data

## ✅ Your Local Data is Safe!

Your local database (`db.sqlite3`) contains all your original website data. I've created tools to export and restore it!

## 🚀 Step-by-Step: Restore Your Data

### Step 1: Export Data from Local Database

On your local computer, run:

```powershell
python export_data.py
```

This creates a file called `local_data_backup.json` with ALL your data:
- ✅ Site settings
- ✅ Homepage sections
- ✅ Services
- ✅ Blog posts
- ✅ Portfolio items
- ✅ Users
- ✅ Everything else!

### Step 2: Initialize Database on Render

Go to your browser and visit:
```
https://novyra-cms.onrender.com/init-database/
```

Click **"Initialize Database"** button.

### Step 3: Create Admin User (if needed)

If you don't have a user yet, visit:
```
https://novyra-cms.onrender.com/create-admin/
```

Create your admin account.

### Step 4: Import Your Data

Visit:
```
https://novyra-cms.onrender.com/import-data/
```

1. Click **"Choose File"**
2. Select the `local_data_backup.json` file from your local computer
3. Click **"Import Data"**

**That's it!** All your original data will be restored!

## 📋 What Gets Restored

- ✅ All site settings (logo, contact info, social media)
- ✅ All homepage sections (Hero, Features, Services, etc.)
- ✅ All service pages
- ✅ All blog posts
- ✅ All portfolio items
- ✅ All users and profiles
- ✅ About page content
- ✅ Footer content
- ✅ Everything else!

## 🔄 Alternative: Manual Export

If `export_data.py` doesn't work, try:

```powershell
$env:PYTHONIOENCODING="utf-8"
python manage.py dumpdata --exclude contenttypes --exclude auth.Permission --exclude sessions --indent 2 > local_data_backup.json
```

## ⚠️ Important Notes

1. **Export first** - Always export from local before importing to Render
2. **Initialize first** - Make sure database is initialized on Render before importing
3. **File size** - If the JSON file is very large (>10MB), the import might take a minute
4. **Media files** - Images and files need to be uploaded separately through CMS after import

## 🎯 After Import

1. Login to CMS: `https://novyra-cms.onrender.com/cms/accounts/login/`
2. Check that all your content is there
3. Upload any missing images through the CMS

## ✅ Success!

Once imported, your website will have all its original content back!

---

**Quick Links:**
- Export: Run `python export_data.py` locally
- Initialize: `/init-database/`
- Import: `/import-data/`
- Login: `/cms/accounts/login/`

