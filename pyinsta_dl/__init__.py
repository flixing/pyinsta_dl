# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

class PyInsta_DL(object):

    def get(self, url):
        self.url = url
        soup = BeautifulSoup(urllib2.urlopen(self.url).read() , "html.parser")
        for meta in soup.findAll('meta'):
            if meta.get("property") == "og:image" and meta.get("content") != '':
                return meta.get("content")
            elif meta.get("property") == "og:video" and meta.get("content") != '':
                return meta.get("content")
        return None

DEFAULT_DOWNLOAD = PyInsta_DL()

def get(url):
    return DEFAULT_DOWNLOAD.get(url)
