from os import path
from string import ascii_letters, digits
from typing import Final, Union, MutableMapping, Mapping, Callable, Any


class Constants:
    NOTE_TYPE = MutableMapping[str, Any]
    ITEM_TYPE = MutableMapping[str, Union[str, NOTE_TYPE, Mapping[str, Union[str, None, bool]]]]
    XPATH: Callable[[str], str] = lambda n: f'/html/body/div[2]/div[3]/div[1]/div[4]/div[4]/div/table[1]/tbody/tr[{n}]'
    WIKI_URL: Final[str] = 'https://escapefromtarkov.gamepedia.com'
    LOOT_PARAMETER: Final[str] = 'Loot'
    LEGAL_SYMBOLS: Final[str] = ascii_letters + digits + ' '
    BARTER: Final[str] = 'barter_item'
    CRAFTING: Final[str] = 'crafting_item'
    HIDEOUT: Final[str] = 'hideout'
    QUESTS: Final[str] = 'quests'
    QUEST: Final[str] = 'quest '
