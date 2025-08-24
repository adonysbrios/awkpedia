# Awkpedia

Awkpedia is a collaboratively-edited, open-content encyclopedia built using the Django web framework.

<img width="1366" height="768" alt="Screenshot (180)" src="https://github.com/user-attachments/assets/ebe026c0-2de6-4461-8fc0-fbc6e86b8812" />
<img width="1366" height="768" alt="Screenshot (179)" src="https://github.com/user-attachments/assets/6adbf691-35a1-4dd9-a9b1-278ba901db86" />
<img width="1366" height="768" alt="Screenshot (181)" src="https://github.com/user-attachments/assets/d2a62e82-04b3-4d91-95e0-968bdc9a4b55" />

# Installation

## Prerequisites

•   **Python:**  Make sure you have Python 3.7+ installed. You can check your Python version by running `python --version` or `python3 --version` in your terminal.

•   **pip:**  Python's package installer.  It usually comes bundled with Python. Verify it's installed by running `pip --version` or `pip3 --version`.

•   **Virtual Environment (Recommended):**  Using a virtual environment is highly recommended to isolate project dependencies.

## Setup Instructions

**1. Create a Virtual Environment (Recommended):**

```
python -m venv venv
# or
python3 -m venv venv 
```

2. Activate the Virtual Environment:

  •  Linux/macOS:

    
```
source venv/bin/activate
```

  •  Windows:

    
```
venv\Scripts\activate
```

3. Install Dependencies:

  Navigate to the directory containing the requirements.txt file (typically the root of your project) and run:

  
```
pip install -r requirements.txt
# or
pip3 install -r requirements.txt 
```

  This command installs all the packages listed in your requirements.txt file, including Django and any other project dependencies.

4. Apply Migrations:

  Navigate to the root of your Django project (the directory containing manage.py) and run:

  
```
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
python manage.py createsuperuser
# or
python3 manage.py createsuperuser
```

  Follow the prompts to enter a username, email address, and password.

▌Deployment (Development Environment)

1. Run the Development Server:

  
```
python manage.py runserver
# or
python3 manage.py runserver
```
