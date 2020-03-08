"""
Author : Christian Lindeneg
         https://github.com/Lindeneg
Contact: christian@lindeneg.org
Licence: CC BY-NC-SA 3.0

Updates the backend with data gathered from scraper.py

The data comes from the unofficial Tarkov gamepedia available under the CC BY-NC-SA 3.0 license
https://escapefromtarkov.gamepedia.com
"""

from typing import Union, MutableSequence, Sequence, Tuple, List, MutableMapping, Optional, Dict, Any
import sys

from lxml import html
from lxml.html import HtmlElement
from requests import get, post, Response, RequestException, ConnectionError
from bs4 import BeautifulSoup

try:
    from .constants import Constants as const
except ImportError:
    from constants import Constants as const


class Scraper:
    """
    Scraping and posting class
    """
    def __init__(self) -> None:
        self.items: Sequence[const.ITEM_TYPE] = []

    def update_items(self) -> None:
        content: HtmlElement = GetContent()
        self.items = SortContent(content)
    
    def update_backend(
        self,
        host: str = "http://127.0.0.1",
        port: Union[int, str] = "8000",
        param: str ="api/create",
        headers: Dict[str, Union[str, Any]] = {}
    ) -> None:
        if len(self.items) <= 0:
            return
        for i in range(len(self.items)):
            self.items[i]["img_info"] = str(self.items[i]["img_info"])
            self.items[i]["notes"] = str(self.items[i]["notes"])
            try:
                res: Response = post(url=f"{host}:{port}/{param}/", headers=headers, data=self.items[i])
                if res.status_code == 200 or res.status_code == 201:
                    print("Successful post of ", self.items[i]["name"])
                else:
                    print("Unsuccessful post of {i}: {r}".format(i=self.items[i]['name'], r=res.content)) #type: ignore[str-bytes-safe]
            except:
                print("\nFailed to establish connection to backend. Make sure you're using the correct port and make sure the backend is running.")
                print(f"Host: {host}\nPort: {port}")
                sys.exit()
        print("\nAll Done.")


def GetContent() -> HtmlElement:
    """
    Get html content from the Tarkov wiki Loot page
    """
    req: Response = get(f"{const.WIKI_URL}/{const.LOOT_PARAMETER}")
    if req.status_code == 200:
        return html.fromstring(req.content)
    print(f"Failed to establish connection with error code {req.status_code}\nContent\n{req.content}") #type: ignore[str-bytes-safe]
    sys.exit()


def SortContent(HTMLContent: HtmlElement) -> MutableSequence[const.ITEM_TYPE]:
    """
    Sorts the html content into an item type
    """
    items: MutableSequence[const.ITEM_TYPE] = []
    # start from second n in xpath - first n is the table header
    n: int = 2
    while True:
        data: Union[None, MutableSequence[bytes]] = [html.tostring(item) for item in HTMLContent.xpath(const.XPATH(str(n)))]
        if data and len(data) >= 1:
            soup: BeautifulSoup = BeautifulSoup(data[0], 'lxml')
            itemData: MutableSequence[str] = RemoveEmptyItems(soup.text.split("\n"))
            # first two entries are always name and item type, thus we start from the third entry
            notes: MutableSequence[str] = CheckForAdditionelSplits(itemData[2:])
            imgPath, imgHeight, imgWidth = GetIMGInfo(soup, 'src'), GetIMGInfo(soup, 'height'), GetIMGInfo(soup, 'width')
            if imgPath is not False:
                items.append({
                    'name': itemData[0],
                    'url': f'{const.WIKI_URL}/{itemData[0].replace(" ", "_")}',
                    'item_type': itemData[1],
                    'notes': SortNotes(notes),
                    'img_info': {
                        'path': imgPath,
                        'height': imgHeight,
                        'width': imgWidth
                    }
                })
        else:
            # In the case data is None or has a length less than 1
            # it likely means that all n's in xpath has been exhausted and we're all done
            # or xpath has been changed which would render this scraper useless until updated
            break
        n += 1
    return items


def CheckForAdditionelSplits(notes: MutableSequence[str]) -> MutableSequence[str]:
    """
    Checks if two seperate words are not seperated, example:
    ['Barter ItemCrafting item']
    should be
    ['Barter Item', 'Crafting item']
    """
    sortedList = []
    for note in notes:
        for i in range(len(note)-1):
            if note[i] in const.LEGAL_SYMBOLS and note[i+1] in const.LEGAL_SYMBOLS and note[i].islower() and note[i+1].isupper():
                sortedList.extend([note[:i+1], note[i+1:]])
    if not sortedList:
        return notes
    return CheckForAdditionelSplits(sortedList)


def SortNotes(notes: MutableSequence[str]) -> const.NOTE_TYPE:
    """
    Sorts a sequence of strings descriping the item into an note type
    """
    sortedNotes: const.NOTE_TYPE = {
        const.BARTER: False,
        const.CRAFTING: False,
        const.QUESTS: {},
        const.HIDEOUT: {}
    }
    note: str
    for note in notes:
        if note.lower() == const.BARTER.replace('_', ' '):
            sortedNotes[const.BARTER] = True
        if note.lower() == const.CRAFTING.replace('_', ' '):
            sortedNotes[const.CRAFTING] = True
        if note.lower() == const.QUESTS:
            i: int = notes.index(note) + 1
            while i < len(notes):
                if notes[i].lower() == const.HIDEOUT:
                    break
                sortedNotes[const.QUESTS][str(i)] = notes[i]
                i += 1
        if note.lower() == const.HIDEOUT:
            j: int = notes.index(note) + 1
            while j < len(notes):
                sortedNotes[const.HIDEOUT][str(j)] = notes[j]
                j += 1
    sortedNotes[const.QUESTS] = SortQH(sortedNotes[const.QUESTS])
    sortedNotes[const.HIDEOUT] = SortQH(sortedNotes[const.HIDEOUT])
    return sortedNotes


def SortQH(items: MutableMapping[int, str]) -> MutableMapping[int, str]:
    """
    Sorts invalid values in quest and hideout dictionaries
    """
    mItems: MutableMapping[int, str] = {}
    for k, v in items.items():
        bV = v.upper()
        if bV != const.BARTER.upper() and bV != const.BARTER.replace("_", " ").upper() \
            and bV != const.CRAFTING.upper() and bV != const.CRAFTING.replace("_", " ").upper():
            mItems[k] = v
    return mItems


def GetIMGInfo(soup: BeautifulSoup, info: str) -> Union[str, None, bool]:
    """
    Tries to extract image information
    """
    try:
        IMGInfo = soup.img[info]
    except KeyError:
        IMGInfo = None
    except TypeError:
        IMGInfo = False
    return IMGInfo


def RemoveEmptyItems(dirtyList: MutableSequence[str]) -> MutableSequence[str]:
    """
    Removes empty entries
    """
    cleanList = []
    for item in dirtyList:
        if not item == "":
            cleanList.append(item)
    return cleanList
