from round import Round


class Tournament:
    """type_of_tournament = ["Bullet", "Blitz", "Rapid"]"""
    def __init__(self, name, place, date):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_round = 4
        self.tour = []
        self.players = []
        self.time_control = ""
        self.description = ""

    def select_type_of_tournament(self, control_time):
        """select control-time"""
        self.time_control = control_time

    def add_players(self, player):
        """add player to tournament"""
        self.players.append(player)

    def add_tour(self):
        for tour in range(1, self.number_of_round):
            round = Round(tour)
            self.tour.append(round)

    def add_tournament_description(self, description):
        self.description = description

