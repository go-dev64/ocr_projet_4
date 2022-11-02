from datetime import datetime


class Round(list):
    def __init__(self, name, players_list):
        self.name = name
        self.list_of_match = []
        self.in_game_player_list = []
        self.players_list = players_list
        self.date_of_start = "date_of_start"
        self.hour_of_start = "hour_of_start"
        self.date_of_end = "date_of_end"
        self.hour_of_end = "hour_of_end"

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
        index_match = self.list_of_match.index(match)
        pop = self.list_of_match.pop(index_match)
        self.append(pop)

    def __str__(self):
        return f"{self.name} ",  f"{self.list_of_match}"

    def __repr__(self):
        return f"{self.name}",  f"{self.list_of_match}"

