import unittest

from lxml import html
from scraper import CheckForAdditionelSplits, SortNotes, SortQH, RemoveEmptyItems, SortContent


class TestCheckForAdditionelSplits(unittest.TestCase):
    def testSeperateTwoDifferentWordsNotSeperated(self):
        case = ['Lorem IncidDolor sit']
        expectedCase = ['Lorem Incid', 'Dolor sit']
        testCase = CheckForAdditionelSplits(case)
        self.assertEqual(testCase, expectedCase)

    def testSeperateFourDifferentWordsNotSeperated(self):
        case = ['Lorem IncidDolor sit', 'Excepteur sintOccaecat']
        expectedCase = ['Lorem Incid', 'Dolor sit', 'Excepteur sint', 'Occaecat']
        testCase = CheckForAdditionelSplits(case)
        self.assertEqual(testCase, expectedCase)
    
    def testValidCase(self):
        case = ['Lorem Incid', 'Dolor sit']
        expectedCase = ['Lorem Incid', 'Dolor sit']
        testCase = CheckForAdditionelSplits(case)
        self.assertEqual(testCase, expectedCase)


class TestSortQH(unittest.TestCase):
    def testRemoveStringLiteralsInsideString(self):
        case = {1: "Lorem ipsum dolor sit amet \"Incididunt\" - Labore"}
        expectedCase = {1: 'Lorem ipsum dolor sit amet Incididunt - Labore'}
        testCase = SortQH(case)
        self.assertEqual(testCase, expectedCase)

    def testRemoveStringLiteralInsideString(self):
        case = {1: "Lorem ipsum dolor sit amet Incid'sidunt - Labore"}
        expectedCase = {1: "Lorem ipsum dolor sit amet Incidsidunt - Labore"}
        testCase = SortQH(case)
        self.assertEqual(testCase, expectedCase)

    def testValidCase(self):
        case = {1: "Lorem ipsum dolor sit amet Incidsidunt - Labore"}
        expectedCase = {1: "Lorem ipsum dolor sit amet Incidsidunt - Labore"}
        testCase = CheckForAdditionelSplits(case)
        self.assertEqual(testCase, expectedCase)


class TestSortNotes(unittest.TestCase):
    def testAllFalse(self):
        case = []
        expectedCase = {'barter_item': False, 'crafting_item': False, 'quests': {}, 'hideout': {}}
        testCase = SortNotes(case)
        self.assertEqual(testCase, expectedCase)

    def testCraftingTrueAllFalse(self):
        case = ['Lorem ipsum', 'Excepteur sint', 'Crafting item', 'Ut enim ad']
        expectedCase = {'barter_item': False, 'crafting_item': True, 'quests': {}, 'hideout': {}}
        testCase = SortNotes(case)
        self.assertEqual(testCase, expectedCase)

    def testBarterTrueAllFalse(self):
        case = ['Lorem ipsum', 'Barter Item', 'Excepteur sint', 'Ut enim ad']
        expectedCase = {'barter_item': True, 'crafting_item': False, 'quests': {}, 'hideout': {}}
        testCase = SortNotes(case)
        self.assertEqual(testCase, expectedCase)

    def testQuestTrueAllFalse(self):
        case = ['Ut enim ad', 'Quests', 'Eu ultrices vitae auctor eu augue', 'Excepteur sint']
        expectedCase = {'barter_item': False, 'crafting_item': False, 'quests': {'2': 'Eu ultrices vitae auctor eu augue', '3': 'Excepteur sint'}, 'hideout': {}}
        testCase = SortNotes(case)
        self.assertEqual(testCase, expectedCase)

    def testHideoutTrueAllFalse(self):
        case = ['Ut enim ad', 'Hideout', 'Eu ultrices vitae auctor eu augue']
        expectedCase = {'barter_item': False, 'crafting_item': False, 'quests': {}, 'hideout': {'2': 'Eu ultrices vitae auctor eu augue'}}
        testCase = SortNotes(case)
        self.assertEqual(testCase, expectedCase)

    def testAllTrue(self):
        case = ['Crafting item', 'Barter Item', 'Quests', 'Lorem ipsum dolor sit amet', 'Hideout', 'Eu ultrices vitae']
        expectedCase = {'barter_item': True, 'crafting_item': True, 'quests': {'3': 'Lorem ipsum dolor sit amet'}, 'hideout': {'5': 'Eu ultrices vitae'}}
        testCase = SortNotes(case)
        self.assertEqual(testCase, expectedCase)


class TestRemoveEmptyItems(unittest.TestCase):
    def testListFiveItemsContainingNoEmptyItems(self):
        case = ['Lorem ipsum', 'Dolor sit amet', 'Eu ultrices vitae', 'Nibh sit amet', 'Amet volutpat']
        expectedCase = ['Lorem ipsum', 'Dolor sit amet', 'Eu ultrices vitae', 'Nibh sit amet', 'Amet volutpat']
        testCase = RemoveEmptyItems(case)
        self.assertEqual(testCase, expectedCase)

    def testListFiveItemsContainingFiveEmptyItems(self):
        case = ['', '', '', '', '']
        expectedCase = []
        testCase = RemoveEmptyItems(case)
        self.assertEqual(testCase, expectedCase)

    def testListFiveItemsContainingTwoEmptyItems(self):
        case = ['Lorem ipsum', '', 'Eu ultrices vitae', '', 'Amet volutpat']
        expectedCase = ['Lorem ipsum', 'Eu ultrices vitae', 'Amet volutpat']
        testCase = RemoveEmptyItems(case)
        self.assertEqual(testCase, expectedCase)


class TestSortContent(unittest.TestCase):
    def testSortContent(self):
        case = b'<html><body><div><div><div></div><div></div><div></div><div></div><div></div><div></div></div></div><div><div></div><div></div><div><div><div><div><table><tbody><tr><td></td></tr></tbody></table></div></div><div></div><div><div></div></div><div><div></div><div></div><div></div><div><div><table><tbody><tr><th>Icon</th>\n<th>Name</th><th>Type</th>\n<th>Notes</th></tr><tr>\n<th><a href="/Folder_with_intelligence" title="Folder with intelligence"><img alt="FolderWithIntelligence Icon.png" src="https://gamepedia.cursecdn.com/escapefromtarkov_gamepedia/8/85/FolderWithIntelligence_Icon.png?version=4e8c8f0dbe5cef4bdd4d6ac97077b644" decoding="async" width="127" height="64" /></a>\n</th>\n<th><a href="/Folder_with_intelligence" title="Folder with intelligence">Folder with intelligence</a>\n</th>\n<td>Info item\n</td>\n<td><b><a href="/Barter_trades" title="Barter trades">Barter Item</a></b><br />\n<p><b>Hideout</b>\n</p>\n<ul><li>1 needs to be found for the <a href="/Hideout#Modules_.28available.29" title="Hideout">intelligence center level 1</a></li>\n<li>3 need to be found for the <a href="/Hideout#Modules_.28available.29" title="Hideout">intelligence center level 2</a></li></ul>\n</td></tr>'
        expectedCase = [{'name': 'Folder with intelligence', 'url': 'https://escapefromtarkov.gamepedia.com/Folder_with_intelligence', 'item_type': 'Info item', 'notes': {'barter_item': True, 'crafting_item': False, 'quests': {}, 'hideout': {'2': '1 needs to be found for the intelligence center level 1', '3': '3 need to be found for the intelligence center level 2'}}, 'img_info': {'path': 'https://gamepedia.cursecdn.com/escapefromtarkov_gamepedia/8/85/FolderWithIntelligence_Icon.png?version=4e8c8f0dbe5cef4bdd4d6ac97077b644', 'height': '64', 'width': '127'}}]
        testCase = SortContent(html.fromstring(case))
        self.assertEqual(testCase, expectedCase)
        

if __name__ == "__main__":
    unittest.main()