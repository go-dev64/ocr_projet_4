class Tournament:
    type_of_tournament = ["Bullet", "Blitz", "Rapid"]

    def __init__(self, name, place, date):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_round = 4
        self.tour = []
        self.players = []
        self.time_control = ""
        self.description = ""

    def select_type_of_tournament(self):
        pass

    def add_players(self):
        pass

    def add_tour(self):
        pass

    def add_description(self):
        pass

