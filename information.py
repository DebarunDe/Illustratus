import yahoo_fantasy_api as yfa
import numpy as np
from dataclasses import dataclass

#FUNCTION: View_Team_Roster
#Inputs: team_id-> team identification number from Yahoo Fantasy API
#Outputs: None
#Description: Takes the team id variable from the league, makes the roster id variable, and parses the resulting
#string to by separated by a newline character when it reaches the player_id part
#_____________________________________________________________________________________________
def View_Team_Roster(league_id,team_id,team_name):
    #Grab Roster for testing purposes
    league = league_id
    team = league.to_team(team_id)
    ros_id = team.roster()
    
    #Parse data to nice format
    for line in ros_id:
            print(line)


    print("\n")
    print("\n")       

#FUNCTION: View_League_Scoring_Stats
#Inputs: league_id-> league identification number from Yahoo Fantasy API
#Outputs: None
#Description: Takes the league id variable from the league, makes the stat id variable, and parses the resulting string 
#_____________________________________________________________________________________________
def View_League_Scoring_Stats(league_id):
    #Grab stat scoring ruling
    stat_id = league_id.stat_categories()

    #Parse data to nice format
    for line in stat_id:
        print(line)
           
    print("\n")
    print("\n")

#FUNCTION: Free_Agent_by_Position
#Inputs: league_id-> league identification number from Yahoo Fantasy API
#        position-> position of free agency that we want to see
#Outputs: None
#Description: Takes the league id variable from the league, makes the free agent id variable, and parses the resulting string 
#_____________________________________________________________________________________________
def Free_Agent_by_Position(league_id,position):
    #Grab free agent by position
    Free_Agent = league_id.free_agents(position)

    #Parse data to nice format
    for line in Free_Agent:
        print(line)
    
    print("\n")
    print("\n")

#FUNCTION: Team_Key_Finder
#Inputs: league_id-> league identification number from Yahoo Fantasy API
#        position-> position of free agency that we want to see
#Outputs: teamkey-> Team_Key value of member
#         teamName-> Team_Name value of member
#Description: Takes the league id variable from the league, and finds the team keys of all participants in the league
#_____________________________________________________________________________________________
def Team_Key_Finder(league_id):
    #return variable init // need to modify per league team settings, hardcoding to 10 teams for now
    team_info_key = []

    #Grab the text information
    league_id_team_keys = league_id.standings()
    
    for line in league_id_team_keys:
        # put text information into tuple to send back
        team_key = line['team_key'].split(':')[0]
        team_info_key.append(team_key)
        
    return team_info_key


#FUNCTION: Team_Name_Finder
#Inputs: league_id-> league identification number from Yahoo Fantasy API
#        position-> position of free agency that we want to see
#Outputs: teamkey-> Team_Key value of member
#         teamName-> Team_Name value of member
#Description: Takes the league id variable from the league, and finds the team names of all participants in the league
#_____________________________________________________________________________________________
def Team_Name_Finder(league_id):
    #return variable init // need to modify per league team settings, hardcoding to 10 teams for now
    team_info_name = []
    #Grab the text information
    league_id_team_keys = league_id.standings()
    for line in league_id_team_keys:
        # put text information into tuple to send back
        team_name = line['name'].split(':')[0]
        team_info_name.append(team_name)
        
    return team_info_name

#FUNCTION: Player_ID_Finder_By_Roster
#Inputs: league_id-> league identification number from Yahoo Fantasy API
#        team_id -> Team identification number from Yahoo Fantasy API
#Outputs: Player_ID_Roster-> all Player IDs in roster
#        
#Description: Takes the league id variable from the league, and finds the team names of all participants in the league
#_____________________________________________________________________________________________
def Player_ID_Finder_By_Roster(league_id,team_id):
    #return variable init // need to modify per league team settings, 
    Player_ID_Roster = []  

    #Grab the roster
    league = league_id
    team = league.to_team(team_id)
    ros_id = team.roster()

    for line in ros_id:
        # put text information into list to send back
        Player_ID_Roster.append(line['player_id'])
        
    return Player_ID_Roster

#FUNCTION: Player_ID_Finder_By_Roster
#Inputs: league_id-> league identification number from Yahoo Fantasy API
#        team_id -> Team identification number from Yahoo Fantasy API
#Outputs: Player_ID_Roster-> all Player IDs in roster
#        
#Description: Takes the league id variable from the league, and finds the team names of all participants in the league
#_____________________________________________________________________________________________
def Stats_Average_Season(league_id,player_id):
    #grab player stats
    player_stat_season = league_id.player_stats(player_id,'average_season')
    return player_stat_season

#FUNCTION: Player_ID_Finder_By_Roster
#Inputs: league_id-> league identification number from Yahoo Fantasy API
#        team_id -> Team identification number from Yahoo Fantasy API
#Outputs: Player_ID_Roster-> all Player IDs in roster
#        
#Description: Takes the league id variable from the league, and finds the team names of all participants in the league
#_____________________________________________________________________________________________
def Stats_This_Season(league_id,player_id):
    #grab player stats
    player_stat_season = league_id.player_stats(player_id,'season')
    print(player_stat_season)
    return player_stat_season

#FUNCTION: Player_ID_Finder_By_Roster
#Inputs: league_id-> league identification number from Yahoo Fantasy API
#        player_id -> player identification number from Yahoo Fantasy API
#        player_stats -> Statistics of player's season
#Outputs: Player_Points -> Player fantasy point total from the season in question
#        
#Description: Takes the league id variable from the league, and finds the team names of all participants in the league
#_____________________________________________________________________________________________
def Stats_To_Points(league_id,player_id):
    player_stats = league_id.player_stats(player_id,'season')
    #grab player stats
   
    for line in player_stats: 
        if(line['position_type'] == 'O'):
            Points = line['Pass Yds']/25 + line['Pass TD']*4 - line['Int']*1 + line['Rush Yds']*0.1 + line['Rush TD']*6 + line['Rec']*1 + line['Rec Yds']*0.1 + line['Rec TD']*6 + line['Ret TD']*6 + line['2-PT']*2 - line['Fum Lost']*2
        elif(line['position_type'] == 'K'):
            Points = line['PAT Made']*1 + line['FG 0-19']*2 + line['FG 20-29']*2 + line['FG 30-39']*3 + line['FG 40-49']*4 + line['FG 50+']*5 
        else:
            Points = 170 + line['Sack']*1 + line['Int']*2 + line['Fum Rec']*2 + line['TD']*6 + line['Blk Kick']*1 + line['Ret TD']*6 - line['Pts Allow 1-6']*3 - line['Pts Allow 7-13']*3 - line['Pts Allow 14-20']*3 - line['Pts Allow 21-27']*3 - line['Pts Allow 28-34']*3 - line['Pts Allow 35+']*3 + line['Safe']*2
        name = line['name']

    
    return {name:Points}


