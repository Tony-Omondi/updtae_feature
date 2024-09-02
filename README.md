# RestarauntProject
This is a Restaurant Project for SCITT Class

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/bobby-850/RestarauntProject.git
    cd RestarauntProject
    ```

2. **Activate the virtual environment**:
    ```bash
    venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations** to set up the database:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

The application should now be running at `http://127.0.0.1:8000/`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


