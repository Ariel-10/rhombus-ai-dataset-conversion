# Rhombus AI - Dataset Conversion
## Overview
Rhombus AI - Dataset Conversion is a web application designed to process and display data, focusing on data type inference and conversion for datasets using Python, Pandas, Django, and React. This application allows users to upload datasets in CSV or Excel format, automatically infers and optimizes data types, and displays the processed data's metadata.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Node.js and npm (Node package manager)

### Setup and Installation

#### Backend (Django)

1. Clone the repository to your local machine:
   ```bash
    git clone hhttps://github.com/Ariel-10/rhombus-ai-dataset-conversion.git
   ```
2. Navigate to the backend directory:
    ```bash
      cd backendDjango
    ```
3. Create a virtual environment:
   ```bash
     python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
       ```bash
         .\venv\Scripts\activate
       ```
   - On macOS and Linux:
       ```bash
         source venv/bin/activate
       ```
5. Install the required Python packages:
    ```bash
       pip install -r requirements.txt
     ```
6. Migrate the database:
    ```bash
       python manage.py migrate
     ```
7. Start the Django server:
    ```bash
       python manage.py runserver
     ```
#### Frontend (React)
1. Navigate to the frontend directory from the project root:
   ```bash
       cd frontend-react
     ```
2. Install the required npm packages:
   ```bash
       npm install
     ```
3. Start the React development server:
   ```bash
       npm start
     ```
The application should now be running, with the frontend accessible at http://localhost:3000 and the backend at http://localhost:8000.
## Additional Notes
- The project is set up to allow CORS for development purposes. Remember to configure CORS settings appropriately for production.
- The Django backend uses SQLite for simplicity. For production, consider using a more robust database system.



