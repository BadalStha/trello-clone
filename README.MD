# Task Manager System

A Django-based Task Manager application using PostgreSQL as the database backend.

## Prerequisites

Before you begin, ensure you have the following installed:

* Python 3.8+
* PostgreSQL
* pip (Python package manager)
* Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/BadalStha/trello-clone.git
cd <project_directory>
```

---

## 2. Configure the Virtual Environment

### Create a Virtual Environment

```bash
python -m venv env
```

### Activate the Environment

#### Windows

```bash
env\Scripts\activate
```

#### macOS / Linux

```bash
source env/bin/activate
```

---

## 3. Install Required Dependencies

Install Django and PostgreSQL driver:

```bash
pip install django psycopg2-binary
```

Alternatively, if a requirements file is provided:

```bash
pip install -r requirements.txt
```

---

## 4. Configure PostgreSQL Database

Ensure that:

* PostgreSQL server is running.
* A database has been created for the application.

Update the `DATABASES` configuration inside `taskmanager/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_postgres_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_database_ip',
        'PORT': '5432',
    }
}
```

Replace the placeholder values with your actual PostgreSQL credentials.

---

## 5. Execute Database Migrations

Generate migration files:

```bash
python manage.py makemigrations boards
```

Apply migrations to the database:

```bash
python manage.py migrate
```

---

## 6. Create an Administrator Account

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your administrator username, email, and password.

---

## 7. Run the Development Server

Start the local Django server:

```bash
python manage.py runserver
```

---

## Access the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

### Django Admin Panel

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials created earlier.

---

## Technology Stack

* Django
* PostgreSQL
* Python

---

## Troubleshooting

### PostgreSQL Connection Issues

Verify:

* PostgreSQL service is running.
* Database credentials are correct.
* Database exists.
* Port `5432` is accessible.

### Migration Errors

Try:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Virtual Environment Not Activating

Ensure you are running the correct activation command for your operating system and shell.

---

## License

This project is intended for educational and development purposes.
