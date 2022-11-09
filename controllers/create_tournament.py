from ocr_projet_4.modeles.tournament import Tournament
from ocr_projet_4.views.view_tournament import ViewTournament
from ocr_projet_4.views.view_player import ViewPlayer
from ocr_projet_4.test import list_players, list__tournament
from ocr_projet_4.controllers.control_player import ControlPlayer
from tinydb import TinyDB, Query

list_of_tournament = list__tournament


class CreateTournament:
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_player = ViewPlayer()
        self.control_player = ControlPlayer()
        self.list_of_type_of_time = ["Bullet", "Blitz", "Coup Rapid"]
        self.name = ""
        self.tournament_info = {}

    def get_information_of_tournament(self):
        self.tournament_info["name"] = self.name
        self.tournament_info["place"] = self.get_place_tournament()
        self.tournament_info["date"] = self.get_date_tournament()
        self.tournament_info["time_control"] = self.get_time_control(
            list_type_of_time=self.list_of_type_of_time
        )
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

    def get_time_control(self, list_type_of_time):
        time_control = self.view_tournament.user_choice_of_control_time(
            list_type_of_time
        )
        return time_control

    def get_tournament_description(self):
        description = self.view_tournament. \
            user_choice_of_description_of_tournament()
        return description

    def select_old_player(self, player_list):
        player_selected = self.view_tournament.user_select_player(
            players_list=player_list
        )
        player = list_players[player_selected]
        return player

    def add_old_player(self, player_list, tournament):
        player = self.select_old_player(player_list=player_list)
        if player in tournament.players_list:
            self.view_tournament.player_already_selected(
                player=player
            )
            self.add_old_player(
                player_list=player_list,
                tournament=tournament
            )
        else:
            return player

    def add_players_tournament(self, tournament):
        while len(tournament.players_list) <= tournament.number_of_player:
            choice = self.view_tournament.user_choice_of_player()
            match choice:
                case 0:
                    """user want select old player"""
                    player = self.add_old_player(
                        player_list=list_players,
                        tournament=tournament
                    )
                    tournament.add_players(player=player)
                case 1:
                    """user want create new player"""
                    new_player = self.control_player.create_player()
                    tournament.add_players(player=new_player)

    def create_new_tournament(self):
        self.name = self.get_name_tournament()
        self.get_information_of_tournament()

        self.name = Tournament(
            name=self.name,
            place=self.tournament_info["place"],
            date=self.tournament_info["date"],
            time_control=self.tournament_info["time_control"],
            description=self.tournament_info["description"]
        )
        self.add_players_tournament(self.name)
        list__tournament.append(self.name)


go = CreateTournament()
go.create_new_tournament()
