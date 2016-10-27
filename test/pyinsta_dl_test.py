from unittest import TestCase
from pyinsta_dl import PyInsta_DL


class TestDownload(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.pyinsta_dl = PyInsta_DL()

    def test_get(self):
        self.url = 'https://www.instagram.com/p/BL_wcRcjS_C'
        self.assertRegexpMatches(self.pyinsta_dl.get(self.url), '/14719344_188429321607052_4168051712482869248_n.jpg')