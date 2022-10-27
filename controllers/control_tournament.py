from ..modeles.tournament import Tournament
from ..views.view_tournament import ViewTournament
from ..views.view_player import ViewPlayer


class ControlTournament:

    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_player = ViewPlayer()
        self.tournament_info = {}

    def get_information_of_tournament(self):
        self.tournament_info["name"]= self.get_name_tournament()
        self.tournament_info["place"] = self.get_place_tournament()
        self.tournament_info["date"] = self.get_date_tournament()
        self.tournament_info["time_control"] = self.get_time_control()

    def get_name_tournament(self):
        name = self.view_tournament.user_choice_of_name_of_tournament()
        return name

    def get_place_tournament(self):
        place = self.view_tournament.user_choice_of_place_of_tournament()
        return place

    def get_date_tournament(self):
        date = self.view_tournament.user_choice_of_date_of_tournament()
        return date

    def get_time_control(self):
        time_control = self.view_tournament.user_choice_of_control_time()
        return time_control




    def run(self):

        self.get_information_of_tournament()



