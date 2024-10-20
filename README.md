Overview This Django project includes:

User Module

--User registration, login, and logout using Django's authentication system. Management of users (add, edit, and delete functionality).

Company Module

--Upload CSV files with a specific format (sample CSV provided). View a summary of the uploaded file data.

Data Filtration Module

--Filter data using Django REST Framework to get counts of the desired data.

Prerequisites

Make sure you have the following installed on your machine:

Python 3.8 or higher Django 3.2 or higher Django REST Framework 3.12 or higher SQLite (default) or any other preferred database pip (Python package installer)

Setup Instructions

Clone the Repository git clone cd

Create and Activate a Virtual Environment python -m venv env source env/bin/activate , On Windows use env\Scripts\activate

Apply Migrations python manage.py migrate

Run the Development Server python manage.py runserver

The project should now be running at http://127.0.0.1:8000/.

Usage

-- User Module -- 1.Navigate to /login/ to log in. 2.To register a new user, go to /register/. 3.After logging in, access the user management pages to: -Add a user. -Edit a user. -Delete a user.

-- Company Module -- 1.Go to the Company section to upload a CSV file. 2.Ensure that the CSV file follows the correct format. A sample format is provided in the project as sample.csv. The headers should match the following: -company_id -name -domain -year founded -industry -size range -locality -country -linkedin url -current employee estimate -total employee estimate

3.After uploading, you will see a summary of the file.

-- Data Filtration Module -- 1.Navigate to the Data Filtration section. 2.You can filter data using the REST API to find the count of desired data fields. The available endpoints can be accessed via /api/data/.
