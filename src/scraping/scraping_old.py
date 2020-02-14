from bs4 import BeautifulSoup
from selenium import webdriver
import re

class Scraping(object):
    def __init__(self, base_uri):
        self.__base_uri = base_uri
        self.__content = object
        self.__links = {}

    @property
    def links(self):
        return self.__links

    def __removeSymbols(self, string):
        return re.sub(r'[^\w]', '', string)

    def __splitSeasonYear(self, string):
        return string.split("-")[1]

    def request(self):
        with webdriver.Chrome(executable_path=r"/usr/bin/chromedriver") as driver:
            driver.get(self.__base_uri)
            self.__content = BeautifulSoup(driver.page_source, "html.parser")

    def findUris(self):
        main_nav = self.__content.find(name="li", id="header_leagues")
        return main_nav

   
    def getUris(self):
        leagues = self.findUris()
        leagues_content = leagues.findAll(name="div", class_="list")
        
        for i in leagues_content:
            found_season = i.find(name="span").getText()
            split_season = self.__splitSeasonYear(found_season)
            season = self.__removeSymbols(split_season)
            for j in i.findAll(name="a"):
                if j.getText() == "Summary":
                    self.__links.update({ season: j['href'] })
