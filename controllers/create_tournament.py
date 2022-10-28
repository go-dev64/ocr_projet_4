from ocr_projet_4.modeles.tournament import Tournament
from ocr_projet_4.views.view_tournament import ViewTournament
from ocr_projet_4.views.view_player import ViewPlayer
from ocr_projet_4.test import list_players, list_tournament

list_of_tournament = []


class CreateTournament(list):
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_player = ViewPlayer()
        self.tournament_info = {}

    def get_information_of_tournament(self):
        self.tournament_info["name"] = self.get_name_tournament()
        self.tournament_info["place"] = self.get_place_tournament()
        self.tournament_info["date"] = self.get_date_tournament()
        self.tournament_info["time_control"] = self.get_time_control()
        self.tournament_info["description"] = self.get_tournament_description()

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

    def get_tournament_description(self):
        description = self.view_tournament.user_choice_of_description_of_tournament()
        return description

    def create_new_tournament(self):
        self.get_information_of_tournament()
        new_tournament = Tournament(name=self.tournament_info["name"],
                                    place=self.tournament_info["place"],
                                    date=self.tournament_info["date"],
                                    time_controle=self.tournament_info["time_control"],
                                    description=self.tournament_info["description"]
                                    )

        new_tournament.add_players(list_players)
        self.append(new_tournament)


go = CreateTournament()
go.create_new_tournament()
go.create_new_tournament()
print(go)
print("toto")
