import random


class Match:
    def __init__(self, name, player1, player2):
        self.name = name
        self.finished_match = False
        self.player1 = player1
        self.player2 = player2
        self.player_with_black_piece = ""
        self.result_player1 = ""
        self.result_player2 = ""
        self.match_result = []

    def serialized_match(self):
        serialized_match = {
            "name": self.name,
            "finished_match": self.finished_match,
            "player1": self.player1.serialized_player(),
            "player2": self.player2.serialized_player(),
            "player_with_black_piece": self.player_with_black_piece.serialized_player(),
            "result_player1": self.result_player1,
            "result_player2": self.result_player2,
            "match_result": self.serialized_result_match()
        }
        return serialized_match

    def get_color(self):
        number = random.randint(0, 1)
        match number:
            case 0:
                self.player_with_black_piece = self.player1
            case 1:
                self.player_with_black_piece = self.player2

    def result_of_match(self, result):
        """save result"""
        match result:
            case 0:
                "winner is player1"
                self.result_player1 = f"{self.player1} win"
                self.result_player2 = f"{self.player2} lose"
            case 1:
                "winner is player2"
                self.result_player2 = f"{self.player2} win"
                self.result_player1 = f"{self.player1} lose"
            case 2:
                "draw"
                self.result_player1 = "draw"
                self.result_player2 = "draw"

    def give_player_point(self, result):
        """add point to player"""
        match result:
            case 1:
                self.player1.number_point += 1
            case 2:
                self.player2.number_point += 1
            case 3:
                self.player1.number_point += 0.5
                self.player2.number_point += 0.5

    def save_result_of_match(self):
        list_player1 = [self.player1, self.result_player1]
        list_player2 = [self.player2, self.result_player2]
        self.match_result = (list_player1, list_player2)

    def serialized_result_match(self):
        match_result = {"player1": self.player1.serialized_player(),
                        "result_player1": self.result_player1,
                        "player2": self.player2.serialized_player(),
                        "result_player2": self.result_player2
                        }
        return match_result

    def status_match_is_finish(self):
        self.finished_match = True

    def __repr__(self):
        return f"{self.player1} VS {self.player2}"

    def __str__(self):
        return f"{self.player1} VS {self.player2}"
