import conn
from src.models import model

from src.scraping.scraping import Scraping
from src.scraping.teams import GetTeams

BASE_URI = r'https://www.basketball-reference.com/'

# initialize connection
CONN = conn.client

# start all models
team_model = model.Team(CONN)


def getTeam():

    gteam = GetTeams(BASE_URI, team_model)
    
    gteam.fillAllTeamsPerConference('E')
    gteam.fillAllTeamsPerConference('W')
    # return gitem

def getSeason():pass

if __name__ == "__main__":
    getTeam()