class Player:
    def __init__(self, name, team, nationality, assists, goals):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
    
    def __str__(self):
        return self.name, self.team, self.assists, self.goals
