EFT Quest Item Scraper
===============

Fetches EFT quest items and associated information. 

The data comes from the unofficial Tarkov gamepedia available under the CC BY-NC-SA 3.0 license
https://escapefromtarkov.gamepedia.com

Usage
===============
```shell
# In a new virtual enviroment

$ (env) python -m pip install -r requirements.txt

# Open Python shell

$ (env) python
```
```python
>>> from scraper import Scraper

>>> scraper = Scraper()

>>> scraper.items
[]

>>> scraper.update_items()

>>> scraper.items
[ ...
    {
        "name": str,
        "url": str,
        "type_info": str,
        "notes": {
            "barter_item": bool,
            "crafting_item": bool,
            "quests": Dict[str, str],
            "hideout": Dict[str, str]
        },
        "img_info": {
            "path": Union[str, bool, None],
            "width": Union[str, bool, None],
            "height": Union[str, bool, None]
        }
    } 
... ]


# If the backend is running

>>> scraper.update_backend()

```