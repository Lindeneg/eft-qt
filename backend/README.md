Backend for EFT-QT
===============

Please note, right now this version has **no authentication** and should only ever be used locally. 

This is the backend for EFT Quest Items and functions as a simple API to be used by the frontend.

It can handle GET requests to fetch data and POST requests to update data.

For the latter purpose ../scraper/scraper.py can be utilized.

Usage
===============
```shell
# In a new virtual enviroment

$ (env) python -m pip install -r requirements.txt

$ (env) cd src && python manage.py runserver
```