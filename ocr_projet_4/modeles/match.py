import random


class Match:
    def __init__(self, name, player1, player2):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.player_with_black_piece = ""
        self.result_player1 = ""
        self.result_player2 = ""
        self.data = []

    def get_color(self):
        number = random.randint(0, 1)
        match number:
            case 1:
                pass
                self.player_with_black_piece = self.player1
            case 2:
                self.player_with_black_piece = self.player2
                pass

    def result_of_match(self, result):
        match result:
            case 1:
                "winner is player1"
                self.result_player1 = f"{self.player1} win"
                self.result_player2 = f"{self.player2} lose"
            case 2:
                "winner is player2"
                self.result_player2 = f"{self.player2} win"
                self.result_player1 = f"{self.player1} lose"
            case 3:
                "draw"
                self.result_player1 = "draw"
                self.result_player2 = "draw"

    def give_player_point(self, result):
        match result:
            case 1:
                self.player1.number_of_point += 1
            case 2:
                self.player2.number_of_point += 1
            case 3:
                self.player1.number_of_point += 0.5
                self.player2.number_of_point += 0.5

    def save_match(self):
        list_player1 = [self.player1, self.result_player1]
        list_player2 = [self.player2, self.result_player2]
        self.data = (list_player1, list_player2)

    def __repr__(self):
        return f"{self.player1} VS {self.player2}"

    def __str__(self):
        return f"{self.player1} VS {self.player2}"


