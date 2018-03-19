# File : league_builder.py
# Treehouse Techdegree Python Web Development
# Assignment 1 - Soccer League
import csv, random


team_info = {'Sharks' : ['15.00', '9/1' ], 'Dragons' : ['12.00', '8/28'], 'Raptors' : ['14.30', '27/8'] }
team_roster = {}
player_records = []

def create_player_records():

    # create a list of lists storing individual player details
    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            player_records.append(row)
    # deleting column header text from list
    del player_records[0]


def create_teams():

    exp_players, nexp_players = divide_players_by_experience()

    # calculating the number of experienced and non-experienced players required for each team
    exp_players_needed = players_needed(exp_players)
    nexp_players_needed = players_needed(nexp_players)

    # adding experienced and non-experienced players to team rosters
    for team in team_info.keys():

        exp_players_in_team = pick_players(exp_players,exp_players_needed)
        nexp_player_in_team = pick_players(nexp_players,nexp_players_needed)
        team_roster[team] = exp_players_in_team + nexp_player_in_team


def divide_players_by_experience():

    # dividing players into lists of experienced and non experienced
    exp_play = []
    nexp_play = []

    for player in player_records:
        if player[2] == 'YES':
            exp_play.append(player)
        else:
            nexp_play.append(player)

    return exp_play, nexp_play


def players_needed(players):

    return len(players) // len(team_info)


def pick_players(players, players_needed):

    team_members = []
    for i in range(players_needed):
        player = random.choice(players)
        team_members.append(player)
        players.remove(player)

    return team_members


def write_teams_to_file():

    file = open('teams.txt','w')
    for team,players in team_roster.items():
        file.write('{}\n'.format(team))
        for player in players:
            file.write('{}\n'.format(', '.join(player)))

    file.close()

def invitation_letter():

    for team,players in team_roster.items():
        for player in players:
            file = open('{}'.format("_".join(player[0].split(' ') )), 'w')
            file.write('''
Dear {},
    I am writing to welcome {} as a member of the {} soccer team. 

Our first practice will be held at the big field {} on {}. Please 
contact me if {} is unable to attend or running late, and ensure
they have their soccer boots with them.

If you have any other queries, please give me a call or drop me
an e-mail.

Thank you for all your support,
Go {}!

Alistair (coach)

bestcoachinworld@gmail.com
T : 555-1934

        '''.format(player[3], player[0],team,team_info[team][0],team_info[team][1],player[0],team))
            file.close()

def main():

    create_player_records()
    create_teams()
    write_teams_to_file()
    invitation_letter()

if __name__ == '__main__':
    main()