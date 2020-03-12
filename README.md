EFT Quest Items
===============

A simple learning project to humbly learn and intergrate React/Django as frontend and backend, respectively.

The project is still in it's infancy and although it does work, it can be improved on almost every aspect.

As of now, only "loot" items are webscraped. Weapons, armour and so on is not (it will be included however)

I've failed a lot and I've learned a lot - so I'll keep failing, so I can keep learning! It has certainly been fun. 

Usage
===============

### Requires [Python 3.8](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/en/)

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

Pictures
======
[![Front Page](https://i.ibb.co/mFYwF10/front.png "EFT-QT Front")](https://i.ibb.co/mFYwF10/front.png)

[![Item Page 1](https://i.ibb.co/nzX8pZT/item.png "EFT-QT Item Page")](https://i.ibb.co/nzX8pZT/item.png)

[![Search Page](https://i.ibb.co/tH46kt2/search.png "EFT-QT Search")](https://i.ibb.co/tH46kt2/search.png)

