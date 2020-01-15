from bs4 import BeautifulSoup
from selenium import webdriver
import re

class Scraping(object):
    def __init__(self, base_uri):
        self.__base_uri = base_uri

    def request(self):
        with webdriver.Chrome(executable_path=r"/usr/bin/chromedriver") as driver:
            driver.get(self.__base_uri)
            self.__content = BeautifulSoup(driver.page_source, "html.parser")

    def findUris(self):
        main_nav = self.__content.find(name="li", id="header_leagues")
        return main_nav

    def __removeSymbols(self, string):
        return re.sub(r'[^\w]', '', string)

    def __splitSeasonYear(self):pass

    def getUris(self):
        leagues = self.findUris()
        leagues_content = leagues.findAll(name="div", class_="list")
        
        links = {}
        for i in leagues_content:
            season = i.find(name="span").getText()
            season = self.__removeSymbols(season)
            for j in i.findAll(name="a"):
                if j.getText() == "Summary":
                    links.update({ season: j['href'] })
        self.__links = links

    @property
    def links(self):
        return self.__links