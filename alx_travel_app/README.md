# ALX Travel App

This is a Django-based backend application for managing travel listings and bookings. It was built as part of the ALX Backend specialization project.

## Features

* User authentication
* Listing creation and management
* Booking system with relationships to users and listings
* API endpoints for CRUD operations
* Database seeding with sample data using Faker

## Tech Stack

* Python 3
* Django
* Django REST Framework
* MySQL
* Faker (for generating seed data)

## Project Structure

```
alx_travel_app_0x00/
└── alx_travel_app/
    ├── alx_travel_app/          # Main Django project
    ├── listings/                # App for listings and bookings
    │   ├── models.py            # Listing and Booking models
    │   ├── serializers.py       # Serializers for API responses
    │   ├── views.py             # API views
    │   ├── urls.py              # API routes
    │   └── management/
    │       └── commands/
    │           └── seed.py      # Custom management command to populate data
    ├── manage.py
    └── requirements.txt
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/alx_travel_app_0x00.git
cd alx_travel_app_0x00
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `faker` isn't recognized, install it explicitly using:

```bash
python -m pip install faker
```

### 4. Configure the Database

Update your `settings.py` to include the correct MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Seed the Database

```bash
python manage.py seed
```

This creates sample listings (and optionally users) using Faker.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Notes

* Passwords must be set using `.set_password()` when creating users programmatically.
* The `host_id` for a listing must refer to a valid user. The seed script creates a default host user.

## License

This project is for educational purposes under the ALX program.