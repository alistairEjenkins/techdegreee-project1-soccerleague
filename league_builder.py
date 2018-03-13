import csv, random

teams = ['Sharks', 'Dragons', 'Raptors']
team_records = {}
player_records = []

def add_player_records():

    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            player_records.append(row)
    del player_records[0]

def divide_players_by_experience():

    exp_play = []
    nexp_play = []
    for player in player_records:
        if player[2] == 'YES':
            exp_play.append(player)
        else:
            nexp_play.append(player)

    return exp_play, nexp_play

'''
def pick_player(experience, picks, team_list):
    
    for i in range(picks):
        choice = random.choice(experience)
        team_list.append(choice)
        experience.remove(choice)
        
    return (team_list)
'''

def create_teams():

    e, n = divide_players_by_experience()


    for team in teams:

        team_members = []
        for i in range(3):
            x = random.choice(e)
            team_members.append(x)
            e.remove(x)
        for i in range(3):
            x = random.choice(n)
            team_members.append(x)
            n.remove(x)

        team_records[team] = team_members

    for k,v in team_records.items():
        print(k)
        print(v)

def write_teams_to_file():

    pass

def main():

    add_player_records()
    create_teams()
    write_teams_to_file()
if __name__ == '__main__':
    main()