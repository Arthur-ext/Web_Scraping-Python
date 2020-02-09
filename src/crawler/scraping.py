from bs4 import BeautifulSoup
from selenium.webdriver import Chrome

class Scraping(object):

    def __init__(self, content, url, season):
        self.__content = content
        self.__url = url
        self.__season = season

    def getTable(self):
        print(self.__content)
    
    
    