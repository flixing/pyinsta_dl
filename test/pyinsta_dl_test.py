from unittest import TestCase
from pyinsta_dl import PyInsta_DL


class TestDownload(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.pyinsta_dl = PyInsta_DL()

    def test_get(self):
        self.url = 'https://www.instagram.com/p/BIIKGvsAzAn'
        self.assertRegexpMatches(self.pyinsta_dl.get(self.url), '/e35/13767522_1081189608614616_2133021102_n.jpg')

    def test_get_all(self):
        list ="13696551_1623515937939386_811374844_n.jpg|13712101_787260854743768_1852237364_n.jpg|13696608_1143451995721101_1226272566_n.jpg|13734513_886387691467426_906122099_n.jpg|13696588_512438322289152_203961896_n.jpg|13767522_1081189608614616_2133021102_n.jpg|13743601_171908029889021_1884058410_n.jpg|13694420_1857890144438796_1473352010_n.jpg|13714243_1586335104999875_1156221155_n.jpg|13722276_586371668209669_1075291188_n.jpg"

        self.url = 'https://www.instagram.com/milreceitas/'
        self.assertRegexpMatches(''.join(self.pyinsta_dl.get_all(self.url)), list)