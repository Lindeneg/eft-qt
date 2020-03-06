"""
Author : Christian Lindeneg
         https://github.com/Lindeneg
Contact: christian@lindeneg.org
Licence: CC BY-NC-SA 3.0

This scraper gathers terse information about loot items in Escape From Tarkov.
The data comes from the unofficial Tarkov gamepedia, which is available under the CC BY-NC-SA 3.0 license
https://escapefromtarkov.gamepedia.com
"""

from typing import Union, MutableSequence, Sequence, Tuple, List

from lxml import html   # type: ignore[import]
from lxml.html import HtmlElement   # type: ignore[import]
from requests import get, Response, RequestException   # type: ignore[import]
from bs4 import BeautifulSoup  # type: ignore[import]

try:
    from constants import Constants as const
except ModuleNotFoundError:
    from .constants import Constants as const  # type: ignore[no-redef, import]


class EFTItemScraper:
    @staticmethod
    def GetItems() -> Sequence[const.ITEM_TYPE]:
        content: HtmlElement = GetContent()
        return SortContent(content)


def GetContent() -> HtmlElement:
    """
    Get html content from the Tarkov wiki Loot page
    """
    e: RequestException
    try:
        req: Response = get(f"{const.WIKI_URL}/{const.LOOT_PARAMETER}")
    except RequestException as e:
        exit()
    if req.status_code == 200:
        return html.fromstring(req.content)
    raise Exception("EXCEPTION")


def SortContent(HTMLContent: HtmlElement) -> MutableSequence[const.ITEM_TYPE]:
    """
    Sorts the html content into an ITEM_TYPE for each item, with the following structure:
    {
        'name': str,
        'url': str',
        'item_type': str,
        'notes': NOTE_TYPE,
        'img_info': {
            'path': str,
            'height': str,
            'width': str
        }
    }
    """
    items: MutableSequence[const.ITEM_TYPE] = []
    n: int = 2  # start from second n in xpath - first n is the table header
    while True:
        data: Union[None, MutableSequence[bytes]] = [html.tostring(item) for item in HTMLContent.xpath(const.XPATH(str(n)))]
        if data and len(data) >= 1:
            soup: BeautifulSoup = BeautifulSoup(data[0], 'lxml')
            itemData: MutableSequence[str] = RemoveEmptyItems(soup.text.split("\n"))
            notes: MutableSequence[str] = CheckForAdditionelSplits(itemData[2:])  # first two entries are always name and item type, thus we start from the third entry
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
    Sorts a sequence of strings descriping the item into an note type, with this structure:
    {
        'barter_item': bool, 
        'crafting_item': bool, 
        'quests': List[Tuple[str]], 
        'hideout': List[str]
    }
    """
    sortedNotes: const.NOTE_TYPE = {
        const.BARTER: False,
        const.CRAFTING: False,
        const.QUESTS: [],
        const.HIDEOUT: []
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
                sortedNotes[const.QUESTS].append(notes[i])
                i += 1
        if note.lower() == const.HIDEOUT:
            j: int = notes.index(note) + 1
            while j < len(notes):
                sortedNotes[const.HIDEOUT].append(notes[j])
                j += 1
    sortedNotes[const.QUESTS] = SortQuests(sortedNotes[const.QUESTS])
    return sortedNotes


def SortQuests(quests: Sequence[str]) -> List[Tuple[str, str]]:
    """
    Finds all quests the given item is involved in 
    Saves the quest description as well as the quest name itself
    """
    mQuests = []
    quest: str
    for quest in quests:
        mQuests.append((quest, quest.split(const.QUEST)[-1].replace(" ", "_")))
    return mQuests


def GetIMGInfo(soup: BeautifulSoup, info: str) -> Union[str, None, bool]:
    try:
        IMGInfo = soup.img[info]
    except KeyError:
        IMGInfo = None
    except TypeError:
        return False
    return IMGInfo


def RemoveEmptyItems(dirtyList: MutableSequence[str]) -> MutableSequence[str]:
    cleanList = []
    for item in dirtyList:
        if not item == "":
            cleanList.append(item)
    return cleanList
