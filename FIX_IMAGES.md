# Fix Images Display Issue

## The Problem
After importing data from `local_data_backup.json`, the database has image paths, but the actual image files aren't on Render.

## Solution

### Step 1: Import Your Data
1. Go to: `https://novyra-cms.onrender.com/import-data/`
2. Upload `local_data_backup.json`
3. Wait for import to complete

### Step 2: Upload Images via CMS

After import, login to CMS and re-upload images:

1. **Site Settings** (`/cms/settings/`)
   - Upload Logo
   - Upload Favicon

2. **Homepage Sections** (`/cms/website/homepage-sections/`)
   - Edit each section
   - Upload background images

3. **Services** (`/cms/website/service-pages/`)
   - Edit each service
   - Upload hero background images

4. **Portfolio** (`/cms/portfolio/`)
   - Edit each portfolio item
   - Upload featured image
   - Upload gallery images

5. **Blog** (`/cms/blog/`)
   - Edit each blog post
   - Upload featured image

6. **Team** (`/cms/website/team/`)
   - Edit each team member
   - Upload photo

7. **Testimonials** (`/cms/website/testimonials/`)
   - Edit each testimonial
   - Upload client photo

### Step 3: Verify Logo

The logo file should be in `static/novyralogo.jpg`. If you have `novyralogo.png`:
- Rename it to `novyralogo.jpg`, OR
- Upload via Site Settings in CMS

## Why This Happens

Render's free tier uses **ephemeral storage** - the `media/` folder gets wiped on each deploy. The database keeps the file paths, but the actual files are gone.

## Permanent Solution

For production, use cloud storage:
- AWS S3
- Cloudinary  
- DigitalOcean Spaces

This way, images persist across deploys.

## Quick Test

After uploading images:
1. Check homepage - logo should appear
2. Check services - images should show
3. Check portfolio - images should display
4. All images from database should now work!

