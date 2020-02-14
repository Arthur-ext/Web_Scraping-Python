from bs4 import BeautifulSoup
from selenium import webdriver
import re

class Scraping(object):
    def __init__(self, base_uri):
        self.__base_uri = base_uri
        self.__links = {}

    @property
    def links(self):
        return self.__links

    def __removeSymbols(self, string):
        return re.sub(r'[^\w]', '', string)

    def _getPageSource(self):
        with webdriver.Chrome(executable_path=r'/usr/bin/chromedriver') as driver:
            driver.get()(self.__base_uri)
            self.__content = BeautifulSoup(driver.page_source, 'html.parser')
    