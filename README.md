EFT Quest Items
===============

A simple learning project to intergrate React and Django as frontend and backend, respectively.

The idea is that you can easily, in raid, search for an item and see if its involved in quests, upgrades or crafting.

The project is still in it's infancy and although it does work, it can be improved on almost every aspect.

I've failed a lot and I've learned a lot - so I'll keep failing, so I can keep learning! It has certainly been fun. 

Usage
===============

### Requires [Python 3](https://www.python.org/downloads/) and [npm](https://www.npmjs.com/get-npm)

```shell
$ git clone https://github.com/Lindeneg/eft-qt.git && cd eft-qt/backend

# In a new virtual enviroment

$ (env) python -m pip install -r requirements.txt

$ (env) cd src && python manage.py migrate

$ (env) python manage.py runserver
```

```shell
# In a new shell

$ cd scraper

# In a new virtual enviroment

$ (env) python -m pip install -r requirements.txt

$ (env) python -c "from scraper import Scraper; scraper=Scraper(); scraper.update_items(); scraper.update_backend();"

# Deactivate virtual enviroment

$ (env) deactivate

$ cd ../frontend && npm install

$ npm start
```