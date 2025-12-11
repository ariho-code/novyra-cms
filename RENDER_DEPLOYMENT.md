# Deploying Novyra CMS to Render

## Prerequisites
1. A GitHub account
2. Your code pushed to a GitHub repository
3. A Render account (sign up at https://render.com)

## Step-by-Step Deployment Guide

### 1. Prepare Your Repository
- Make sure all your code is committed and pushed to GitHub
- Ensure `requirements.txt`, `Procfile`, and `render.yaml` are in the root directory

### 2. Create a Render Account
1. Go to https://render.com
2. Sign up or log in
3. Connect your GitHub account

### 3. Create a PostgreSQL Database
1. In Render dashboard, click "New +"
2. Select "PostgreSQL"
3. Configure:
   - **Name**: `novyra-db` (or any name you prefer)
   - **Database**: `novyra_cms`
   - **User**: `novyra_user` (or any username)
   - **Region**: Choose closest to your users
   - **Plan**: Free (for testing) or Starter ($7/month for production)
4. Click "Create Database"
5. **Important**: Copy the "Internal Database URL" - you'll need this

### 4. Create a Web Service
1. In Render dashboard, click "New +"
2. Select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `novyra-cms`
   - **Environment**: `Python 3`
   - **Region**: Same as your database
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (if code is in root)
   - **Build Command**: 
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command**: 
     ```
     gunicorn novyra_cms.wsgi:application
     ```
   - **Plan**: Free (for testing) or Starter ($7/month for production)

### 5. Set Environment Variables
In your Web Service settings, add these environment variables:

**Required:**
- `SECRET_KEY`: Generate a new secret key (you can use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `DEBUG`: `False` (for production)
- `ALLOWED_HOSTS`: `your-app-name.onrender.com,*.onrender.com`
- `DATABASE_URL`: Paste the Internal Database URL from step 3

**Optional (but recommended):**
- `PYTHON_VERSION`: `3.11.0`

### 6. Deploy
1. Click "Create Web Service"
2. Render will start building and deploying your app
3. Wait for the build to complete (usually 5-10 minutes)
4. Once deployed, your app will be available at `https://your-app-name.onrender.com`

### 7. Create Superuser
After deployment, you need to create a superuser:
1. Go to your Render dashboard
2. Click on your Web Service
3. Go to "Shell" tab
4. Run:
   ```
   python manage.py createsuperuser
   ```
5. Follow the prompts to create your admin account

### 8. Initialize CMS Content
1. In the Shell, run:
   ```
   python manage.py shell
   ```
2. Then run:
   ```python
   exec(open('initialize_cms_content.py').read())
   ```

### 9. Upload Logo
1. Log into your CMS at `https://your-app-name.onrender.com/cms/`
2. Go to Settings
3. Upload your logo

## Important Notes

### Static Files
- Static files are served via WhiteNoise (configured in settings.py)
- Run `python manage.py collectstatic` during build (already in build command)

### Media Files
- For production, consider using AWS S3 or Cloudinary for media storage
- Render's filesystem is ephemeral - uploaded files will be lost on redeploy
- To fix this, you'll need to configure cloud storage (S3, Cloudinary, etc.)

### Database Migrations
- Migrations run automatically during build
- If you need to run migrations manually, use the Shell tab

### Environment Variables
- Never commit `SECRET_KEY` or `DATABASE_URL` to Git
- Use Render's environment variables feature

## Troubleshooting

### Build Fails
- Check build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Database Connection Issues
- Verify `DATABASE_URL` is set correctly
- Check database is running and accessible
- Ensure database credentials are correct

### Static Files Not Loading
- Verify `collectstatic` ran during build
- Check `STATIC_ROOT` and `STATIC_URL` in settings
- Ensure WhiteNoise middleware is in `MIDDLEWARE`

### 500 Errors
- Check application logs in Render dashboard
- Verify `DEBUG=False` and check error logs
- Ensure all environment variables are set

## Next Steps
1. Set up a custom domain (optional)
2. Configure email settings for contact forms
3. Set up automated backups for database
4. Configure cloud storage for media files (S3, Cloudinary, etc.)
5. Set up monitoring and alerts

## Support
- Render Documentation: https://render.com/docs
- Django Deployment Checklist: https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

