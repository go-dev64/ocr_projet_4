from modeles.tournament import Tournament
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer
from controllers.control_player import ControlPlayer
from controllers.control_data import Data


class CreateTournament:
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_player = ViewPlayer()
        self.control_player = ControlPlayer()
        self.database = Data()
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

    def valid_registration_in_players_list(self, tournament, player):
        tournament.add_players(player=player)
        self.view_tournament.confirm_player_registration(
            player=player,
            tournament=tournament
        )

    def add_players_tournament(self, tournament):
        """add new players or players from
        a database player list to the tournament"""
        while len(tournament.players_list) <= tournament.number_of_player:
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

    def save_tournament_in_database(self, tournament):
        serialized_tournament = tournament.serialized_tournament()
        self.database.table_of_tournament.insert(serialized_tournament)

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
        self.add_players_tournament(tournament=self.name)
        self.save_tournament_in_database(tournament=self.name)


go = Tournament(name="test",
                place="toto",
                date=11-11-2022,
                time_control="Bullet",
                description="test")

toto = CreateTournament()
ControlPlayer().deserialized_all_player_in_database()
toto.add_players_tournament(tournament=go)
