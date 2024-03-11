# File: task9.py
# Author: Jasmin Fränti
# Description: Task 9 of exercise 4 
# Hockey player stats

import json
import os
     
def get_data(file):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    json_file_path = os.path.join(script_dir, file)
    
    with open(json_file_path) as data_file:
        data = data_file.read()
        parsed_json = json.loads(data)
        
    return parsed_json
        
def search_player(name, file):
    data = get_data(file)
        
    for player in data:
        if player["name"] == name:
                player_name = player["name"]
                team = player["team"]
                goals = player['goals']
                assists = player['assists']
                formatted_string = f"\n{player_name:20} {team:3} {goals:>2} + {assists:>2} = {goals + assists:>2}\n"
                print(formatted_string)
                break
            
def list_teams(file):
    data = get_data(file)
    teams = []
    
    for player in data:
        teams.append(player["team"])
        
    teams = set(teams)
    teams = list(teams)
    teams.sort()
    
    for team in teams:
        print(team)
        
def list_countries(file):
    data = get_data(file)
    countries = []
    
    for player in data:
        countries.append(player["nationality"])
        
    countries = set(countries)
    countries = list(countries)
    countries.sort()
    
    for item in countries:
        print(item)

def list_players_in_team(team, file):
    data = get_data(file)
    players = []
    
    for player in data:
        if player["team"] == team:
            player["points"] = player["goals"] + player["assists"]
            players.append(player)
            
    sorted_players = sorted(players, key=lambda d: d['points'], reverse=True)
    
    for player in sorted_players:
        player_name = player["name"]
        goals = player["goals"]
        assists = player["assists"]
        print(f"{player_name:20} {team:3} {goals:>2} + {assists:>2} = {goals + assists:>2}")
        
def list_players_by_country(country, file):
    data = get_data(file)
    players = []
    
    for player in data:
        if player["nationality"] == country:
            player["points"] = player["goals"] + player["assists"]
            players.append(player)
            
    sorted_players = sorted(players, key=lambda d: d['points'], reverse=True)
    
    for player in sorted_players:
        player_name = player["name"]
        goals = player["goals"]
        assists = player["assists"]
        team = player["team"]
        print(f"{player_name:20} {team:3} {goals:>2} + {assists:>2} = {goals + assists:>2}")

def list_by_most_points(num_of_players, file):
    data = get_data(file)
    players = []
    
    for player in data:
        player["points"] = player["goals"] + player["assists"]
        players.append(player)
    
    sorted_players = sorted(players, key=lambda d: (d['points'], d['goals']), reverse=True)
    
    for player in sorted_players[:int(num_of_players)]:
        player_name = player["name"]
        goals = player["goals"]
        assists = player["assists"]
        team = player["team"]
        print(f"{player_name:20} {team:3} {goals:>2} + {assists:>2} = {goals + assists:>2}")
    
def list_by_most_goals(num_of_players, file):
    data = get_data(file)
    players = []
    
    for player in data:
        players.append(player)
    
    sorted_players = sorted(players, key=lambda d: (d['goals'], -d['games']), reverse=True)
    
    for player in sorted_players[:int(num_of_players)]:
        player_name = player["name"]
        goals = player["goals"]
        assists = player["assists"]
        team = player["team"]
        print(f"{player_name:20} {team:3} {goals:>2} + {assists:>2} = {goals + assists:>2}")
        
while True:
    file = input("Select a file: ")
    help1 = "Command:\n0: Quit\n1: Search player stats\n2: List teams\n3: List countries\n"
    help2 = "4: Players in team\n5: Players by country\n6: Most points\n7: Most goals\n"
    
    command = input(help1 + help2)
    
    if command == "0":
        break
    elif command == "1":
        name = input("Searh player by name: ")
        search_player(name, file)
    elif command == "2":
        list_teams(file)
    elif command == "3":
        list_countries(file)
    elif command == "4":
        team = input("List all players in a team: ")
        list_players_in_team(team, file)
    elif command == "5":
        country = input("List all players in a country: ")
        list_players_by_country(country, file)
    elif command == "6":
        num_of_players = input("How many players will be listed? ")
        list_by_most_points(num_of_players, file)
    elif command == "7":
        num_of_players = input("How many players will be listed? ")
        list_by_most_goals(num_of_players, file)