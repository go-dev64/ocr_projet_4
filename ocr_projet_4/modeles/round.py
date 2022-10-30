from datetime import datetime
from ocr_projet_4.modeles.match import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.list_of_match = []
        self.players_list = []
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

    def leave_loser_player(self, loser_player):
        self.players_list.pop(loser_player)

    def get_match_of_round(self):
        y = int(len(self.players_list) / 2)
        for i in range(1, y + 1):
            i = Match(
                name=i,
                player1=self.players_list[i - 1],
                player2=self.players_list[y + i - 1]
            )

    def __str__(self):
        return f"{self.name}", f"{self.list_of_match}"

    def __repr__(self):
        return f"{self.name}", f"{self.list_of_match}"

