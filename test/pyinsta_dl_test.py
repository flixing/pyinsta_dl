from unittest import TestCase
from pyinsta_dl import PyInsta_DL


class TestDownload(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.pyinsta_dl = PyInsta_DL()

    def test_get(self):
        self.url = 'https://www.instagram.com/p/BL_wcRcjS_C'
        self.assertEqual(self.pyinsta_dl.get(self.url), 'https://instagram.fgru3-2.fna.fbcdn.net/'\
                't51.2885-15/e35/14719344_188429321607052_4168051712482869248_n.jpg?ig_cache_key='\
                'MTM2OTAyNTg2MDg1NDQyNzU4Ng%3D%3D.2'  or 'https://scontent.cdninstagram.com/t51.2885-15/'\
                'e35/14719344_188429321607052_4168051712482869248_n.jpg?'\
                'ig_cache_key=MTM2OTAyNTg2MDg1NDQyNzU4Ng%3D%3D.2')