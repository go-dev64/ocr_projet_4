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
        self.status = "en cours"
        self.id_tournament = None

    def serialized_tournament(self):
        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number_of_round": self.number_of_round,
            "number_of_player": self.number_of_player,
            "round_list": self.convert_round_list_for_serialise(
                the_list=self.round_list
            ),
            "players_list": self.convert_players_list_for_serialise(
                the_list=self.players_list
            ),
            "time_control": self.time_control,
            "description": self.description,
            "status": self.status,
            "id_tournament": self.id_tournament,
        }
        return serialized_tournament

    @staticmethod
    def convert_round_list_for_serialise(the_list):
        list_of_round = []
        for round in the_list:
            list_of_round.append(round.serialized_round())
        return list_of_round

    @staticmethod
    def convert_players_list_for_serialise(the_list):
        list_of_player = []
        for player in the_list:
            list_of_player.append(player.serialized_player())
        return list_of_player

    def add_players(self, player):
        """add player to tournament"""
        self.players_list.append(player)

    def add_tournament_description(self, description):
        self.description = description

    def add_round(self, round):
        self.round_list.append(round)

    def sort_player_list_by_rang(self):
        """sort list by rang, only in first round"""
        self.players_list = sorted(self.players_list, key=lambda player: player.rang)

    def sort_player_list_by_point(self):
        """sort by rang if equality of point"""
        self.sort_player_list_by_rang()
        """ sort list by point """
        self.players_list = sorted(
            self.players_list, key=lambda player: player.number_point, reverse=True
        )

    def change_status(self):
        self.status = "Terminé"

    def __str__(self):
        return self.name + " de " + self.place

    def __repr__(self):
        return self.name + " de " + self.place
