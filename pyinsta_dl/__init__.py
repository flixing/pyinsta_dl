# -*- coding: utf-8 -*-
import urllib2, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import stat


class PyInsta_DL(object):
    def __init__(self):

        self.userAgent = 'Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) \
        AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
        self.phantomjs = '/usr/local/phantomjs/phantomjs'
        DesiredCapabilities.PHANTOMJS[
            'phantomjs.page.customHeaders.User-Agent'] = self.userAgent
        self.driver = webdriver.PhantomJS(executable_path=self.phantomjs, \
                                          service_args=['--ignore-ssl-errors=true'])

    def get(self, url):
        self.url = url
        soup = BeautifulSoup(urllib2.urlopen(self.url).read(), "html.parser")
        for meta in soup.findAll('meta'):
            if meta.get("property") == "og:video" and meta.get("content") != '':
                return meta.get("content")
            elif meta.get("property") == "og:image" and meta.get("content") != '':
                return meta.get("content")

    def get_all(self, url):
        self.url = url
        self.driver.get(self.url)
        time.sleep(5)
        [self.scroll() for i in range(self.count_scrolls()) ]
        return self._get_all_urls

    def count_scrolls(self):
        _default_number = 12
        publicatios = self.driver.find_element_by_class_name('_bkw5z')
        number = int(publicatios.text.replace('.', ''))
        if number > 12:
            more = self.driver.find_element_by_class_name('_1ooyk')
            more.click()
            return (number / _default_number) + 1

        else:
            return 1

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    @property
    def _get_all_urls(self):
        images = self.driver.find_elements_by_class_name('_icyx7')
        links = []
        for i in images:
            links.append(i.get_attribute('src'))
        self.driver.close()
        return links


DEFAULT_DOWNLOAD = PyInsta_DL()


def get(url):
    return DEFAULT_DOWNLOAD.get(url)


def get_all(url_profile):
    return DEFAULT_DOWNLOAD.get_all(url_profile)
