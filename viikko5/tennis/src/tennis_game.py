class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0

        self.tied_score = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All"
        }

        self.temp_scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def tie(self):
        if self.score1 in self.tied_score:
            return self.tied_score[self.score1]

        return "Deuce"

    def score_more_than_four(self):
        minus_result = self.score1 - self. score2

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def score_less_than_four(self):
        score = self.update_points(self.score1) + "-" + self.update_points(self.score2)
        return score

    def update_points(self, temp_score):
        points = self.temp_scores[temp_score]
        return points

    def won_point(self, player_name):
        if player_name == "player1":
            self.score1 += 1
        else:
            self.score2 += 1

    def get_score(self):
        if self.score1 == self.score2:
            tie = self.tie()
            return tie
    
        elif self.score1 >= 4 or self.score2 >= 4:
            score_more_than_four = self.score_more_than_four()
            return score_more_than_four
            
        else:
            score_less_than_four = self.score_less_than_four()
            return score_less_than_four
