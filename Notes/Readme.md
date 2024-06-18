# Flask Notes App

## Setup Instructions

1. Clone the repository:
   
    git clone https://github.com/yourusername/flask_notes_app.git
    cd flask_notes_app
    
2. Set up a virtual environment:
   
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
3. Install dependencies:
   
    pip install -r requirements.txt
    
4. Initialize the database:
   
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    
5. Run the application:
   
    flask run
    
## Project Structure

- app.py: Main application file.
- models.py: Database models.
- auth.py: Authentication routes.
- main.py: Main application routes.
- forms.py: WTForms forms.
- templates/: HTML templates.
- static/: Static files (CSS).
- migrations/: Database migrations.

## Features

- User registration and login.
- CRUD operations for notes.
- Basic CSS styling.
- Error handling for common issues.