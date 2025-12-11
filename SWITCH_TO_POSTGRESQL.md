# 🔄 Switching Back to PostgreSQL

Currently, the CMS is using **SQLite** for quick testing. To switch to **PostgreSQL** for production:

## Step 1: Install PostgreSQL

### Option A: Download and Install
1. Download PostgreSQL from: https://www.postgresql.org/download/windows/
2. Install it (remember the password you set)
3. Create a database:
   ```sql
   CREATE DATABASE novyra_cms;
   ```

### Option B: Use Docker (if you install Docker Desktop)
```bash
docker run --name novyra-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=novyra_cms -p 5432:5432 -d postgres:15
```

## Step 2: Update Settings

Edit `novyra_cms/settings.py`:

**Comment out SQLite:**
```python
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
```

**Uncomment PostgreSQL:**
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config('DB_NAME', default='novyra_cms'),
        "USER": config('DB_USER', default='postgres'),
        "PASSWORD": config('DB_PASSWORD', default='postgres'),
        "HOST": config('DB_HOST', default='localhost'),
        "PORT": config('DB_PORT', default='5432'),
    }
}
```

## Step 3: Create .env File

Create a `.env` file in the project root:
```env
SECRET_KEY=django-insecure-5r)!7&2sm4x2@ocens1g#h+3e9ng(iy6z%ov^(^qzmfz)uv62#
DEBUG=True
DB_NAME=novyra_cms
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

## Step 4: Run Migrations

```bash
python manage.py migrate
```

## Step 5: Create Superuser (if needed)

```bash
python manage.py createsuperuser
```

Or use the script:
```bash
python create_superuser.py
```

## Step 6: Initialize Settings

```bash
python manage.py shell
```

Then:
```python
from settings_app.models import SiteSettings
SiteSettings.load()
exit()
```

## ✅ Done!

Your CMS is now running on PostgreSQL!

---

**Note:** SQLite is fine for development/testing, but PostgreSQL is recommended for production due to better performance, concurrent access, and advanced features.

