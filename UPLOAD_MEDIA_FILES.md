# Upload Media Files to Render

## Problem
When you import your database backup, the image paths are stored in the database, but the actual image files need to be uploaded to Render.

## Solution: Upload Media Files

### Option 1: Upload via CMS (Recommended)

After importing your data:

1. **Login to CMS**: `https://novyra-cms.onrender.com/cms/accounts/login/`

2. **Go to Site Settings**: `/cms/settings/`
   - Upload your logo
   - Upload favicon
   - Add all images

3. **Go to each section and re-upload images**:
   - Homepage Sections → Upload background images
   - Services → Upload service images
   - Portfolio → Upload portfolio images
   - Blog → Upload blog post images
   - Team → Upload team member photos
   - Testimonials → Upload client photos

### Option 2: Use Render Persistent Disk (If Available)

If you have persistent disk storage on Render:

1. The `media/` folder will persist across deploys
2. Upload files via CMS and they'll stay

### Option 3: Use Cloud Storage (Best for Production)

For production, use cloud storage like:
- AWS S3
- Cloudinary
- DigitalOcean Spaces

## Current Setup

Media files are configured to be served from `/media/` URL.

**Important**: On Render free tier, the `media/` folder is **ephemeral** - it gets wiped on each deploy. You need to:

1. **Re-upload images after each deploy**, OR
2. **Use cloud storage** for production

## Quick Fix: Re-upload After Import

1. Import your data: `/import-data/`
2. Login to CMS
3. Go through each section and re-upload images
4. Images will work until next deploy

## Logo File

The logo file should be:
- `static/novyralogo.jpg` (for fallback)
- Or uploaded via Site Settings in CMS

If you have `novyralogo.png`, rename it to `novyralogo.jpg` or update the template.

