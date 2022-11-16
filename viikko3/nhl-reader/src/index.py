import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == "FIN":
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals']
            )
    

            players.append(player)

    print("Oliot:")

    for player in players:
        print(f"{player.name} team {player.team} assists {player.assists} goals {player.goals}")
        #print(player.name, player.team, player.assists, player.goals)


if __name__ == "__main__":
    main()