# Todo List

## Author

xxHAKRxx

## Description

A simple todo list app where you can make tasks for yourself to complete. This is the first Django project I've created that actually has a database integrated into it and is not just a static website. Unfortunately, due to Heroku paywalling people for creating an account, I have nowhere to host this thing, so you'll just have to run a localhost server in Git in order to view it. If you don't know how to do that:

1. Make sure you have Git installed if you're doing this on Windows (Git comes pre-installed on Linux).
2. Clone the repo into any directory you want.
   * ```git clone github_link```
3. Go into the newly cloned repo, create a python virtual environment, then activate it.
   * ```(winpty) python -m venv .venv```
   * ```. .venv/Scripts/activate```
4. Install all of the packages found in a text file called requirements.txt.
   * ```python -m pip install -r requirements.txt```
5. Apply migrations to the project (It will work without them, but there will be problems).
   * ```(winpty) python manage.py migrate```
6. Create a superuser so you can log yourself in.
   * ```(winpty) python manage.py createsuperuser```
7. Run the localhost server and log yourself in.
   * ```(winpty) python manage.py runserver```
8. You're officially in the site!

## Outside Resources Used

Bootstrap for CSS styling: https://getbootstrap.com/docs/5.2/examples/sticky-footer-navbar/

## Known Problems, Issues, And/Or Errors in the Program

Header was hidden behind the navbar for some reason, had to add a style modifier to increase the margin and make it appear
