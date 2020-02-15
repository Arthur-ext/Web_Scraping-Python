from bs4 import BeautifulSoup
from selenium import webdriver
import re

class Scraping(object):
    def __init__(self, base_uri):
        self.__base_uri = base_uri
        self.__links = {},
        self.__content = self.__getBaseSource()

    @property
    def links(self):
        return self.__links

    @property
    def content(self):
        return self.__content

    def __removeSymbols(self, string):
        return re.sub(r'[^\w]', '', string)

    def getPageSource(self):
        with webdriver.Chrome(executable_path=r'/usr/bin/chromedriver') as driver:
            driver.get(self.__base_uri)
            return driver.page_source

    def __getBaseSource(self):
        return self.getPageSource()
