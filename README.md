## Medicine Dosage Tracker
Med Tracker is a Django REST framework application designed to manage medicines and their dosages for users. The application includes 
functionalities for user registration, login, logout, and access control to ensure users can only view and manage their own medicines and dosages.

## Features

### User Registration: Create a new user account.
### User Login: Authenticate and obtain JWT tokens.
### User Logout: Securely log out by invalidating the refresh token.
### Medicine Management: Create, view, update, and delete medicines.
### Dosage Management: Create, view, update, and delete dosages linked to medicines.
### Access Control: Ensure users can only access and manage their own medicines and dosages.

## Installation

## step:1

Clone the repository:
git clone https://github.com/yourusername/Medicine_Dose_tracker.git
cd med_dose_tracker

## step:2
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## step:3
Install dependencies:
pip install django djangorestframework djangorestframework-simplejwt

## step:4
Apply migrations:
python manage.py migrate

## step:5
Create a superuser:
python manage.py createsuperuser

## step:6
Run the development server:
python manage.py runserver

## API ENDPOINTS

### Register: POST api/register/
### Login: POST api/login/
### Logout: POST api/logout/

## Medicines:

### GET /api/medicines/ - List all medicines of the authenticated user.
### POST /api/medicines/ - Create a new medicine.
### GET /api/medicines/<medicine_id>/ - Retrieve a specific medicine.
### PUT /api/medicines/<medicine_id>/ - Update a specific medicine.
### DELETE /api/medicines/<medicine_id>/ - Delete a specific medicine.

## Dosages:

### GET /api/medicines/<medicine_id>/dosages/ - List all dosages of  specific medicine of the authenticated user.
### POST /api/medicines/<medicine_id>/dosages/ - Create a new dosage for a specific medicine.
### GET /api/medicines/<medicine_id>/dosages/<dosage_id>- Retrieve a specific dosage.
### PUT /api/medicines/<medicine_id>/dosages/<dosage_id> - Update a specific dosage.
### DELETE /api/medicines/<medicine_id>/dosages/<dosage_id> - Delete a specific dosage.


