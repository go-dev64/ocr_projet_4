from datetime import datetime
from modeles.match import Match


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

    def serialized_round(self):
        serialized_round = {
            "name": self.name,
            "list_of_match": self.convert_match_list_for_serialise(
                the_list=self.list_of_match
            ),
            "match_in_progress": self.convert_match_list_for_serialise(
                the_list=self.match_in_progress
            ),
            "in_game_player_list": self.convert_players_list_for_serialise(
                the_list=self.in_game_player_list
            ),
            "players_list": self.convert_players_list_for_serialise(
                the_list=self.players_list
            ),
            "date_of_start": self.date_of_start,
            "hour_of_start": self.hour_of_start,
            "date_of_end": self.date_of_end,
            "hour_of_end": self.hour_of_end
        }
        return serialized_round

    @staticmethod
    def convert_match_list_for_serialise(the_list):
        list_of_match = []
        for match in the_list:
            list_of_match.append(match.serialized_match())
        return list_of_match

    @staticmethod
    def convert_players_list_for_serialise(the_list):
        list_of_player = []
        for player in the_list:
            list_of_player .append(player.serialized_player())
        return list_of_player

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
        now = datetime.now()
        date = datetime.today().strftime("%d/%m/%y")
        hour = now.strftime("%H:%M:%S")
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
