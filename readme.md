# Installation

## Prerequisites

•   **Python:**  Make sure you have Python 3.7+ installed. You can check your Python version by running `python --version` or `python3 --version` in your terminal.
•   **pip:**  Python's package installer.  It usually comes bundled with Python. Verify it's installed by running `pip --version` or `pip3 --version`.
•   **Virtual Environment (Recommended):**  Using a virtual environment is highly recommended to isolate project dependencies.

## Setup Instructions

**1. Create a Virtual Environment (Recommended):**

```
bash
  python -m venv venv
  # or
  python3 -m venv venv

 
```

2. Activate the Virtual Environment:

  •  Linux/macOS:

    
```
bash
    source venv/bin/activate

```

  •  Windows:

    
```

bash
    venv\Scripts\activate

```

3. Install Dependencies:

  Navigate to the directory containing the requirements.txt file (typically the root of your project) and run:

  
```

 
bash
  pip install -r requirements.txt
  # or
  pip3 install -r requirements.txt

 
```

  This command installs all the packages listed in your requirements.txt file, including Django and any other project dependencies.

4. Apply Migrations:

  Navigate to the root of your Django project (the directory containing manage.py) and run:

  
```
bash

  python manage.py makemigrations
  # or
  python3 manage.py makemigrations

  python manage.py migrate
  # or
  python3 manage.py migrate

 
```

  This command applies any pending database migrations, creating the necessary tables in your database.

5. Create a Superuser:

  To access the Django admin interface, you need to create a superuser:

  
```

 
bash
  python manage.py createsuperuser
  # or
  python3 manage.py createsuperuser

 
```

  Follow the prompts to enter a username, email address, and password.

▌Deployment (Development Environment)

1. Run the Development Server:

  
```

 
bash
  python manage.py runserver
  # or
  python3 manage.py runserver
