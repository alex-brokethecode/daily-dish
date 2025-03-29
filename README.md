# daily-dish
A project for a restaurant

# Deployment Guide: Django Project on PythonAnywhere

## 1. Create a PythonAnywhere Account

- Visit [PythonAnywhere](https://www.pythonanywhere.com/) and create a new account. Choose the plan that best suits your needs.

## 2. Open a Bash Console

- Once logged in, navigate to the "Consoles" tab.
- Click "Bash" to open a new Bash console.

## 3. Clone Your Project Repository

- Use `git clone <your_repository_url>` to clone your project repository.
- **If you have multiple branches:**
    - Fetch all remote branches: `git fetch origin`
    - Switch to your desired branch: `git switch <branch_name>`
    - Pull the latest changes: `git pull origin <branch_name>`

## 4. Create a Virtual Environment

- Create a virtual environment for your project:
    ```bash
    mkvirtualenv --python=python3.x <your_virtualenv_name>
    ```
    (Replace `python3.x` with the appropriate Python version, e.g., `python3.9`, and `<your_virtualenv_name>` with a descriptive name.)
- Activate the virtual environment: `workon <your_virtualenv_name>`

## 5. Install Project Dependencies

- Navigate to your project directory: `cd <your_project_name>`
- Install the project's dependencies: `pip install -r requirements.txt`

## 6. Create a Web App

- Navigate to the "Web" tab on PythonAnywhere.
- Click "Add a new web app".
- Select "Manual configuration".
- Choose the appropriate Python version.
- Enter your project directory as the "Source code" path (e.g., `/home/<your_username>/<your_project_name>`).
- **Copy the project directory name** (you'll need it for WSGI configuration).

## 7. Configure WSGI File

- Find the "WSGI configuration file" path on the "Web" tab.
- Click on the path to open the WSGI file in the editor.
- Replace the existing content with the following:

    ```python
    import os
    import sys

    path = '/home/<your_username>/<your_project_name>'  # Replace with your project path
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = '<your_project_name>.settings'  # Replace with your project's settings module

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```

    - Replace `<your_username>` and `<your_project_name>` with your actual values.

## 8. Configure Django Settings

- Open your project's `settings.py` file.
- Add your PythonAnywhere domain to `ALLOWED_HOSTS`:

    ```python
    ALLOWED_HOSTS = ['<your_username>.pythonanywhere.com']  # Replace with your domain
    ```

    * For production, consider setting `DEBUG = False` and configuring `SECRET_KEY` securely.

## 9. Run Database Migrations

- In your Bash console (with the virtual environment activated), run database migrations:

    ```bash
    python manage.py migrate
    ```

## 10. Configure Static Files

- Add the following line to your `settings.py` file:

    ```python
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```

- Run the `collectstatic` command to gather static files:

    ```bash
    python manage.py collectstatic
    ```

- On the "Web" tab, scroll down to the "Static files" section.
- Add the following mappings:

    - **`/static/`**: `/home/<your_username>/<your_project_name>/staticfiles/`
    - **`/media/`**: `/home/<your_username>/<your_project_name>/media/`

    - Replace `<your_username>` and `<your_project_name>` with your actual values.

## 11. Reload Your Web App

- On the "Web" tab, click the "Reload <your_username>.pythonanywhere.com" button to apply the changes.
- Visit your deployed site again to ensure that everything is working correctly.



