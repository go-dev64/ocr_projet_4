from datetime import datetime
from ocr_projet_4.modeles.match import Match


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

    def get_time_now(self):
        date = datetime.today().strftime("%d/%m/%y")
        hour = datetime.today().isoformat(timespec="seconds")
        return date, hour

    def sort_player_list_by_rang(self):
        """sort list by rang, only in first round"""
        self.players_list = sorted(
            self.players_list,
            key=lambda player: player.rang
        )

    def sort_player_list_by_point(self):
        """ sort list by point """
        self.players_list = sorted(
            self.players_list,
            key=lambda player: player.number_point
        )

    def add_winner(self, winner):
        self.in_game_player_list.extend(winner)

    def get_match_of_round(self):
        len_list_divide_per_2 = int(len(self.players_list) / 2)
        for i in range(1, len_list_divide_per_2 + 1):
            print(i)
            i = Match(
                name=i,
                player1=self.players_list[i - 1],
                player2=self.players_list[len_list_divide_per_2 + i - 1]
            )
            i.get_color()
            self.list_of_match.append(i)
            print(i)

    def take_out_the_finished_match(self, match):
        index_match = self.list_of_match.index(match)
        pop = self.list_of_match.pop(index_match)
        self.append(pop)

    def __str__(self):
        return f"{self.name} ",  f"{self.list_of_match}"

    def __repr__(self):
        return f"{self.name}",  f"{self.list_of_match}"

