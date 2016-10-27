# -*- coding: utf-8 -*-
"""
Sample Usage:

>>> import pyinsta_dl
>>> url = pyinsta_dl.get('https://www.instagram.com/p/BL_wcRcjS_C/')
>>> print(url)
https://instagram.fgru3-2.fna.fbcdn.net/t51.2885-15/e35/14719344_188429321607052_4168051712482869248_n.jpg?ig_cache_key=MTM2OTAyNTg2MDg1NDQyNzU4Ng%3D%3D.2

"""

import urllib2
from bs4 import BeautifulSoup

__version__ = (0, 0, 1)

class PyInsta_DL(object):

    def get(self, url):

        soup = BeautifulSoup(urllib2.urlopen(url).read() , "html.parser")
        for meta in soup.findAll('meta'):
            if meta.get("property") == "og:image" and meta.get("content") != None:
                return meta.get("content")
            elif meta.get("property") == "og:video" and meta.get("content") != None:
                return meta.get("content")
        return None

DEFAULT_DOWNLOAD = PyInsta_DL()


def get(url):
    return DEFAULT_DOWNLOAD.get(url)
