from ocr_projet_4.modeles.round import Round


class Tournament:
    def __init__(self, name, place, date, time_controle, description):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_round = 4
        self.tour = []
        self.players = []
        self.list_loser = []
        self.time_control = time_controle
        self.description = description

    def add_players(self, player):
        """add player to tournament"""
        self.players.extend(player)

    def add_tour(self):
        for tour in range(1, self.number_of_round):
            tour = Round(tour)
            self.tour.append(round)

    def add_tournament_description(self, description):
        self.description = description

    def __str__(self):
        return self.name + " de " + self.place

    def __repr__(self):
        return self.name + " de " + self.place
