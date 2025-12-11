# Novyra CMS

A modern, feature-rich Content Management System built with Django and PostgreSQL for Novyra Marketing Agency.

## Features

- 📝 **Blog Management** - Create, edit, and manage blog posts with rich text editor
- 💼 **Portfolio Management** - Showcase your work with portfolio items and galleries
- 👥 **User Management** - Manage users with different roles (Administrator, Editor, Author)
- ⚙️ **Settings** - Configure site settings, SEO, social media links, and security options
- 📊 **Dashboard** - Beautiful dashboard with statistics and recent activity
- 🎨 **Modern UI** - Responsive design with smooth animations and mobile-friendly interface
- 🔒 **Secure** - Built-in authentication and security features

## Requirements

- Python 3.8+
- PostgreSQL 12+
- pip

## Installation

1. **Clone the repository**
   ```bash
   cd "novyra cms"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL Database**
   
   Create a PostgreSQL database:
   ```sql
   CREATE DATABASE novyra_cms;
   CREATE USER novyra_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE novyra_cms TO novyra_user;
   ```

4. **Configure Environment Variables**
   
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DB_NAME=novyra_cms
   DB_USER=novyra_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

9. **Access the CMS**
   - Admin Panel: http://127.0.0.1:8000/admin/
   - Dashboard: http://127.0.0.1:8000/dashboard/
   - Login: http://127.0.0.1:8000/accounts/login/

## Project Structure

```
novyra_cms/
├── blog/              # Blog app
├── portfolio/          # Portfolio app
├── accounts/           # User management app
├── settings_app/       # Site settings app
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
└── novyra_cms/         # Main project settings
```

## Usage

### Creating Blog Posts

1. Navigate to **Blog Posts** in the sidebar
2. Click **Add New Post**
3. Fill in the form with title, content, categories, and featured image
4. Choose status (Draft, Published, or Pending Review)
5. Click **Save Post**

### Managing Portfolio

1. Navigate to **Portfolio** in the sidebar
2. Click **Add New Item**
3. Add project details, images, and categories
4. Mark as featured if needed
5. Save the item

### User Management

1. Navigate to **Users** in the sidebar
2. Click **Add New User** to create a new user
3. Edit users to change roles and permissions
4. Users can have roles: Administrator, Editor, or Author

### Settings

1. Navigate to **Settings** in the sidebar
2. Configure:
   - **General**: Site title, tagline, description
   - **SEO**: Meta tags, keywords
   - **Social Media**: Links to social profiles
   - **Security**: Two-factor authentication, login limits

## Technologies Used

- **Backend**: Django 5.0.1
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Rich Text Editor**: CKEditor
- **Forms**: Django Crispy Forms
- **Animations**: AOS (Animate On Scroll)
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter, Poppins)

## Mobile Responsive

The CMS is fully responsive and optimized for:
- Desktop (1920px+)
- Tablet (768px - 1024px)
- Mobile (320px - 767px)

## Security Features

- User authentication and authorization
- CSRF protection
- SQL injection prevention
- XSS protection
- Secure password hashing
- Session management

## Development

To run in development mode:

```bash
python manage.py runserver
```

To create a new migration:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Production Deployment

1. Set `DEBUG=False` in settings
2. Configure proper `ALLOWED_HOSTS`
3. Set up proper database credentials
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Set up static file serving (Nginx, Apache)
6. Configure SSL/HTTPS

## License

This project is proprietary software for Novyra Marketing Agency.

## Support

For issues or questions, please contact the development team.

