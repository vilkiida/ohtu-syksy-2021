class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player):
        if player == self.player1:
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1
    def handle_score_equal_points(self):
        if self.player1_points == 0:
            return "Love-All"
        elif self.player1_points == 1:
            return "Fifteen-All"
        elif self.player1_points == 2:
            return "Thirty-All"
        elif self.player1_points == 3:
            return "Forty-All"
        return "Deuce"
    
    def handle_score_points_over_4(self):
        difference = self.player1_points - self.player2_points
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        return "Win for player2"
    
    def handle_score(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"
    
    def handle_score_points_under_4(self):
        player1_score = self.handle_score(self.player1_points)
        player2_score = self.handle_score(self.player2_points)
        return player1_score + "-" + player2_score

    def get_score(self):
        if self.player1_points == self.player2_points:
            return self.handle_score_equal_points()
        elif self.player1_points >= 4 or self.player2_points >= 4:
            return self.handle_score_points_over_4()
        else:
            return self.handle_score_points_under_4()

