from bs4 import BeautifulSoup
from src.scraping.scraping import Scraping

class GetTeams(Scraping):
    def __init__(self, base_uri, team_model):
        super().__init__(base_uri)
        self.__team_model = team_model
    
    def fillAllTeamsPerConference(self, conference):
        rows = self._getConferenceTeamRows(conference)
                
        for row in rows:
            team = self.getTeam(row, conference)
            self.__team_model.save(team)

    def getTeam(self, team_row, conference):
        team_data = {
            "conference": "",
            "name": "",
            "tag": "",
            "executive": "",
            "coach": "",
            "arena": "",
            "season": ""
        }
        team = {"updates": 0, "team_data": team_data}
        
        team_data.update({"conference": self.__conferenceName(conference)})

        anchor = team_row.find(name="a")
        team_name = anchor['title']
        team_tag = anchor.text

        team_data.update({"name": team_name, "tag": team_tag})
        
        pg_src = self.getPageSource(anchor['href'])
        team_page = BeautifulSoup(pg_src, "html.parser")
        team_info = self._getTeamInfo(team_page)
        team_data.update(team_info)
        return team
    
    def __getInfoData(self, info, search):
        p_list = info.findAll(name="p")

        for item in p_list:
            strong = item.find(name='strong')
            if strong == None: continue
            if self._removeSymbols(strong.text) == search:
                return item.text
        return None

    def _getTeamInfo(self, team_page):
        data = {}
        info = team_page.find(name="div", id="info")
        season = info.find(name="h1").find(name="span")
        data.update({"season": season.text})
        
        executive = self.__getInfoData(info, "Executive").split(':')[1]
        coach = self.__getInfoData(info, "Coach").split(':')[1]
        arena = self.__getInfoData(info, "Arena").split(':')[1].split('\n')[1]
        
        data.update({'executive': executive.strip()})
        data.update({'coach': coach.strip()})
        data.update({'arena': arena.strip()})
        return data
            
    def _getConferenceTeamRows(self, conference):
        soup = BeautifulSoup(self.content, 'html.parser')
        div = soup.find(name='div', id='all_confs_standings_%s' % conference)
        
        tbody = div.find(name='tbody')
        all_tr = tbody.findAll(name='tr')

        return all_tr

    def __conferenceName(self, conference):
        if "E" == str.upper(conference):
            return "Eastern"
        elif "W" == str.upper(conference):
            return "Western"
    