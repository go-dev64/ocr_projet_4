from controllers.control_data import Data, data_tournaments_list
from controllers.control_player import ControlPlayer
from modeles.tournament import Tournament
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer




class CreateTournament:
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_player = ViewPlayer()
        self.control_player = ControlPlayer()
        self.data = Data()
        self.list_of_type_of_time = ["Bullet", "Blitz", "Coup Rapid"]
        self.tournament_info = {}

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

    def get_information_of_tournament(self):
        self.tournament_info["name"] = self.get_name_tournament()
        self.tournament_info["place"] = self.get_place_tournament()
        self.tournament_info["date"] = self.get_date_tournament()
        self.tournament_info["time_control"] = self.get_time_control(
            list_type_of_time=self.list_of_type_of_time
        )
        self.tournament_info["description"] = self.get_tournament_description()

    def instance_tournament(self, tournament_info):
        the_tournament = Tournament(
            name=tournament_info["name"],
            place=tournament_info["place"],
            date=tournament_info["date"],
            time_control=tournament_info["time_control"],
            description=tournament_info["description"]
        )
        return the_tournament

    def valid_registration_in_players_list(self, tournament, player):
        tournament.add_players(player=player)
        self.view_tournament.confirm_player_registration(
            player=player,
            tournament=tournament
        )

    def add_players_tournament(self, tournament):
        """add new players or players from
        a database player list to the tournament"""
        while len(tournament.players_list) <= tournament.number_of_player - 1:
            choice = self.view_tournament.user_choice_of_player()
            match choice:
                case 0:
                    """user want select player in database players list"""
                    player_from_db = self.control_player.player_from_db(
                        player=self.control_player.select_player_in_database(),
                        tournament=tournament)
                    if player_from_db is not None:
                        self.valid_registration_in_players_list(
                            tournament=tournament,
                            player=player_from_db
                        )
                case 1:
                    """user want create new player"""
                    new_player = self.control_player.add_new_player_by_user(
                        tournament=tournament
                    )
                    if new_player is not None:
                        self.valid_registration_in_players_list(
                            tournament=tournament,
                            player=new_player
                        )

    """def add_tournament_in_database(self, tournament):
        serialized_tournament = tournament.serialized_tournament()
        id_tournament = self.data.table_of_tournament.insert(serialized_tournament)
        self.data.table_of_player.update(
            {"id_tournament": id_tournament},
            self.data.where("id_tournament") == id_tournament
        )"""

    def create_new_tournament(self):
        self.get_information_of_tournament()
        tournament = self.instance_tournament(tournament_info=self.tournament_info)
        self.add_players_tournament(tournament=tournament)
        self.data.add_tournament_in_database(tournament=tournament)
        data_tournaments_list.append(tournament)
        self.view_tournament.confirm_creation_tournament(tournament=tournament)
        return tournament

    def launch_new_tournament(self, new_tournament):
        choice = self.view_tournament.confirm_creation_tournament(
            tournament=new_tournament
        )
        return choice
