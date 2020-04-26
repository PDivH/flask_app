1. The flask app must be structured with a <MAIN> folder and a <subfolder>.

2. The primary __init__.py must be in the <subfolder>. Empty __init__.py files in sub-subfolders make it behave like a package

3. The "pipenv shell" environment and ALL extensions must be installed in the <MAIN> folder

4. To run the app, either:
   4.1 in terminal: set FLASK_APP=run.py and set FLASK_ENV=development. Use "flask run" to run the app/server (easier to use). This is for DEVELOPMENT
   4.2 in terminal: set FLASK_APP=<subfolder> and set FLASK_ENV=development. Use "python run.py" to run the app/server. This also works for DEVELOPMENT, 
        but eventually for PRODUCTION on server, as the "flask run" development server must not be used for PRODUCTION.
    So you can use either the "python run.py" or "flask run" options in development, but ony "python run.py" in production.
    For production however, you will specify to run the app from the Gunicorn (or uWSGI) configuration

5. Install python-dotenv and create .flaskenv file. Inside the file:
        FLASK_APP=run.py (development) or set FLASK_APP=<subfolder> (also works for development, but eventually production)
        FLASK_ENV=development OR production
    now you don't have to manually set FLASK_APP=<>  and FLASK_ENV=<> in terminal, just start with "flask run"

6. Create .env file and inside:
    SQLALCHEMY_DATABASE_URI=<>
    SECRET_KEY=<>
    SQLALCHEMY_TRACK_MODIFICATIONS=<>
    and others