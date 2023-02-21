from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
from helper_league_information.information import * 

#Thanks to: https://youtu.be/C0WjwBtwS9Y

#Connect to Yahoo API via consumer key and secret
sc = OAuth2(None, None, from_file='oauth2.json')

#Access Game Objects
game = yfa.Game(sc,'nfl')

#Access league information (INCLUDING EARLIER GAMES)
#leagues = game.league_ids()
#print(leagues)

#Grab league information and team information
league = game.to_league('414.l.66822')

#display stat information
#View_League_Scoring_Stats(league)

#Grab roster information using teamkey
# team_key = league.team_key()
# team = league.to_team(team_key)
# View_Team_Roster(league,team,"De Harem")

#Testing to grab other players from other teams
League_Team_Keys = Team_Key_Finder(league)
League_Team_Names = Team_Name_Finder(league)




#Grab player ID test
#Team_Name_Finder(league)

# for i in range(0,10):
#     players = Player_ID_Finder_By_Roster(league,League_Team_Keys[i])
#         #test statistics functionality
#     for j in range(0,15):
#         #Stats_This_Season(league,players[i])
#         print(Stats_To_Points(league,players[j]))

for i in range(31001,100000):
    print(Stats_To_Points(league,i))

#Testing to display all team's roster in the league
#for i in range(0,10): #harcoded currently
   # View_Team_Roster(league,League_Team_Keys[i],League_Team_Names[i])


#team2 = league.to_team("414.l.66822.t.1")
#View_Team_Roster(team2)
            
#Testing for Free Agent Tracker
#Free_Agent_by_Position(league,"RB")