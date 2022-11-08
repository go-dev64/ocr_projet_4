from datetime import datetime
from ocr_projet_4.modeles.match import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.list_of_match = []
        self.match_in_progress = self.list_of_match.copy()
        self.in_game_player_list = []
        self.players_list = []
        self.date_of_start = "date_of_start"
        self.hour_of_start = "hour_of_start"
        self.date_of_end = "date_of_end"
        self.hour_of_end = "hour_of_end"

    def create_match(self, name, player_1, player_2):
        name = Match(
            name=name,
            player1=player_1,
            player2=player_2
        )
        name.get_color()
        self.list_of_match.append(name)

    def start_of_round(self):
        """give the date and hour of starting round"""
        self.date_of_start = self.get_time_now()[0]
        self.hour_of_start = self.get_time_now()[1]

    def end_of_round(self):
        """give the date and hour of ending round"""
        self.date_of_end = self.get_time_now()[0]
        self.hour_of_end = self.get_time_now()[1]

    @staticmethod
    def get_time_now():
        date = datetime.today().strftime("%d/%m/%y")
        hour = datetime.today().isoformat(timespec="seconds")
        return date, hour

    def add_winner(self, winner):
        self.in_game_player_list.extend(winner)

    def take_out_the_finished_match(self, match):
        index_match = self.match_in_progress.index(match)
        self.match_in_progress.pop(index_match)

    def __str__(self):
        return f"{self.name} ,{self.list_of_match}"

    def __repr__(self):
        return f"{self.name},{self.list_of_match}"

