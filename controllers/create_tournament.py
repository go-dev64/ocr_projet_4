from controllers.control_data import Data, data_tournaments_list, data_players_list
from controllers.control_player import ControlPlayer, ViewGeneric
from modeles.tournament import Tournament
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer


class CreateTournament:
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_player = ViewPlayer()
        self.control_player = ControlPlayer()
        self.view_generic = ViewGeneric()
        self.data = Data()
        self.tournaments_list = data_tournaments_list
        self.list_of_type_of_time = ["Bullet", "Blitz", "Coup Rapid"]
        self.tournament_info = {}

    def get_information_of_tournament(self):
        info_tournament = self.view_tournament.get_info_tournament()
        self.tournament_info["name"] = info_tournament["name"]
        self.tournament_info["place"] = info_tournament["place"]
        self.tournament_info["date"] = info_tournament["date"]
        self.tournament_info["time_control"] = info_tournament["time_control"]
        self.tournament_info["description"] = info_tournament["description"]

    def instance_tournament(self, tournament_info):
        the_tournament = Tournament(
            name=tournament_info["name"],
            place=tournament_info["place"],
            date=tournament_info["date"],
            time_control=tournament_info["time_control"],
            description=tournament_info["description"],
        )
        return the_tournament

    def valid_registration_in_players_list(self, tournament, player):
        player.number_point = 0
        tournament.add_players(player=player)
        self.control_player.generic.view_generic.confirm_element_registration(
            message=f"{player} est inscrit au {tournament.name}",
            title="Confirmation inscription joueur"
        )

    def get_tournament_in_progress(self):
        in_progress_tournament = []
        for tournament in self.tournaments_list:
            if tournament.status != "Terminé":
                in_progress_tournament.append(tournament)
        return in_progress_tournament

    def get_free_players(self):
        in_progress_tournament = self.get_tournament_in_progress()
        free_players = data_players_list
        for tournament in in_progress_tournament:
            for player in tournament.players_list:
                if player in free_players:
                    index = free_players.index(player)
                    free_players.pop(index)
        return free_players

    def add_players_tournament(self, tournament):
        """add new players or players from
        a database player list to the tournament"""
        free_players_list = self.get_free_players()
        while len(tournament.players_list) <= tournament.number_of_player - 1:
            choice = self.view_tournament.user_choice_of_player()
            if choice == 0:
                """user want select player in database players list"""
                index_player_db = self.view_generic.user_select_element_in_list(
                            elements_list=free_players_list,
                            confirmation_text="Voulez-vous revenir au menu precedent",
                            title="Liste des joueurs disponible",
                        )
                player = free_players_list[index_player_db]
                player_from_db = (
                    self.control_player.check_if_player_is_tournament_players_list(
                        player=player,
                        tournament=tournament,
                    )
                )
                if player_from_db is not None:
                    self.valid_registration_in_players_list(
                        tournament=tournament, player=player_from_db
                    )
                    free_players_list.pop(index_player_db)
            elif choice == 1:
                """user want create new player"""
                new_player = self.control_player.add_new_player_in_tournament(
                    tournament=tournament
                )
                if new_player is not None:
                    self.valid_registration_in_players_list(
                        tournament=tournament, player=new_player
                    )
                else:
                    continue

    def create_new_tournament(self):
        self.get_information_of_tournament()
        tournament = self.instance_tournament(tournament_info=self.tournament_info)
        self.add_players_tournament(tournament=tournament)
        self.data.add_tournament_in_database(tournament=tournament)
        data_tournaments_list.append(tournament)
        self.view_tournament.confirm_creation_tournament(tournament=tournament)
        return tournament

    def launch_new_tournament(self, new_tournament):
        #self.view_tournament.confirm_creation_tournament(tournament=new_tournament)
        choice = self.view_tournament.confirm_launch_new_tournament(
            tournament=new_tournament
        )
        return choice
