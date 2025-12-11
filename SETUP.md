# Quick Setup Guide

## PostgreSQL Setup (Windows)

### Option 1: Install PostgreSQL Locally

1. **Download PostgreSQL**
   - Visit: https://www.postgresql.org/download/windows/
   - Download and install PostgreSQL 12 or higher
   - During installation, remember the password you set for the `postgres` user

2. **Create Database**
   - Open pgAdmin or use psql command line
   - Create a new database named `novyra_cms`
   ```sql
   CREATE DATABASE novyra_cms;
   ```

3. **Configure .env file**
   - Copy `.env.example` to `.env`
   - Update with your PostgreSQL credentials:
   ```env
   DB_NAME=novyra_cms
   DB_USER=postgres
   DB_PASSWORD=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

### Option 2: Use Docker (Recommended)

1. **Install Docker Desktop** (if not installed)
   - Download from: https://www.docker.com/products/docker-desktop

2. **Run PostgreSQL in Docker**
   ```bash
   docker run --name novyra-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=novyra_cms -p 5432:5432 -d postgres:15
   ```

3. **Configure .env file**
   ```env
   DB_NAME=novyra_cms
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_PORT=5432
   ```

## After PostgreSQL is Running

1. **Create .env file** (if not exists)
   ```bash
   copy .env.example .env
   ```
   Then edit `.env` with your database credentials.

2. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

4. **Create Initial Site Settings**
   ```bash
   python manage.py shell
   ```
   Then in the shell:
   ```python
   from settings_app.models import SiteSettings
   SiteSettings.load()
   exit()
   ```

5. **Run Server**
   ```bash
   python manage.py runserver
   ```

6. **Access CMS**
   - Login: http://127.0.0.1:8000/accounts/login/
   - Dashboard: http://127.0.0.1:8000/dashboard/
   - Admin: http://127.0.0.1:8000/admin/

## Troubleshooting

### PostgreSQL Connection Error

If you get connection errors:

1. **Check if PostgreSQL is running**
   - Windows: Check Services (services.msc) for "postgresql" service
   - Or check Task Manager for postgres processes

2. **Verify connection settings**
   - Check `.env` file has correct credentials
   - Verify PostgreSQL is listening on port 5432
   - Check firewall settings

3. **Test connection**
   ```bash
   psql -U postgres -h localhost -d novyra_cms
   ```

### Migration Issues

If migrations fail:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files Issues

```bash
python manage.py collectstatic --noinput
```

