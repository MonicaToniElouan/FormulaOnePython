from Presentation import *
from Persistance import DBBroker
from Domain.Team import *

agent = DBBroker.DBBroker()
team = Team(1, "TeamName", "TeamCountry", "CreationDate")
print(team.TeamID)