import random


class Match:

    def __init__(self, name, player1, player2):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.player_with_black_piece = ""
        self.result_player1 = 0
        self.result_player2 = 0

    def get_color(self):
        number = random.randint(0, 1)
        match number:
            case 1:
                pass
                self.player_with_black_piece = self.player1
            case 2:
                self.player_with_black_piece = self.player2
                pass

    def __repr__(self):
        return (f"{self.player1}" + "VS" + f"{self.player2}",
                "Joueur en noir: " + f"{self.player_with_black_piece}")

    def __str__(self):
        return (f"{self.player1}" + "VS" + f"{self.player2}",
                "Joueur en noir: " + f"{self.player_with_black_piece}")


