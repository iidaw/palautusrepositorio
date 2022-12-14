class Player:
    def __init__(self, name, team, nationality, assists, goals):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    def __lt__(self, other):
        return self.assists + self.goals < other.assists + other.goals
    
    def __str__(self):
        return f"{self.name} {self.team} {self.assists} + {self.goals} = {self.goals + self.assists}"

