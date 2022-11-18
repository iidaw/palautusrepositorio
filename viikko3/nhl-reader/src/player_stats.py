class PlayerStats:
    def __init__(self, stat):
        self.players = stat.get_players()

    

    def top_scorers_by_nationality(self, nationality):
        self.players.sort(reverse=True)

        player_list = []

        for player in self.players:
            if player.nationality == nationality:
                player_list.append(player)

        return player_list