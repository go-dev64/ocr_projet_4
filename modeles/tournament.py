
from ocr_projet_4.modeles.match import Match


class Tournament:
    def __init__(self, name, place, date, time_control, description):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_round = 4
        self.number_of_player = 8
        self.round_list = []
        self.players_list = []
        self.time_control = time_control
        self.description = description

    def add_players(self, player):
        """add player to tournament"""
        self.players_list.extend(player)

    def add_tournament_description(self, description):
        self.description = description

    def add_round(self, round):
        self.round_list.append(round)

    def sort_player_list_by_rang(self):
        """sort list by rang, only in first round"""
        self.players_list = sorted(
            self.players_list,
            key=lambda player: player.rang
        )

    def sort_player_list_by_point(self):
        """sort by rang if equality of point"""
        self.sort_player_list_by_rang()
        """ sort list by point """
        self.players_list = sorted(
            self.players_list,
            key=lambda player: player.number_point,
            reverse=True
        )

    def __str__(self):
        return self.name + " de " + self.place

    def __repr__(self):
        return self.name + " de " + self.place
