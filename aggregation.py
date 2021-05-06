# perform aggregation between 3 classes.
# implement a School class containing a list of Team objects, and a Team class comprising of a list of Player objects.
# Player class should have three properties that will be set using an initializer:
# ID
# name
# teamName
# Team class will have two properties that will be set using an initializer:
# name
# players, a list with player class objects in it.
# It will have two methods:
# addPlayer(), which will add new player objects in the players list.
# getNumberOfPlayers(), which will return the total number of players in the players list.
# The School class will contain two properties that will be set using an initializer:
# teams, a list of team class objects
# name
# It will have two methods:
# addTeam, which will add new team objects in the teams list.
# getTotalPlayersInSchool() method counts the total players in all of the teams in the School and returns the count!


class Player:

    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName


class Team:

    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)


class School:

    def __init__(self, name):
        self.teams = []
        self.name = name

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        count = 0
        for team in self.teams:
            count += team.getNumberOfPlayers()
        return count


p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.addPlayer(p1)
red_team.addPlayer(p2)
print('red team players:', red_team.getNumberOfPlayers())

blue_team = Team("Blue Team")
blue_team.addPlayer(p2)
blue_team.addPlayer(p3)
print('blue team players:', blue_team.getNumberOfPlayers())

mySchool = School("My School")
mySchool.addTeam(red_team)
mySchool.addTeam(blue_team)

print("Total players in mySchool:", mySchool.getTotalPlayersInSchool())
