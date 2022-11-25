from views.view_player import ViewPlayer
from modeles.player import Player
from controllers.control_data import Data, players_list


class ControlPlayer:

    def __init__(self):
        self.view_player = ViewPlayer()
        self.player_info = {}

    def get_player_name(self):
        name = self.view_player.input_player_name()
        return name

    def get_player_first_name(self):
        first_name = self.view_player.input_player_first_name()
        return first_name

    def get_date_of_birth(self):
        date = self.view_player.input_date_of_birth()
        return date

    def get_gender(self):
        gender = self.view_player.input_gender()
        return gender

    def get_player_rang(self):
        rang = self.view_player.input_player_rang()
        return rang

    def add_player_in_database(self, player):
        serialized_name = player.serialized_player()
        Data().table_of_player.insert(serialized_name)

    def deserialize_player(self, serialized_player):
        name = Player(
            name=serialized_player['name'],
            first_name=serialized_player['first_name'],
            date_of_birth=serialized_player['date_of_birth'],
            gender=serialized_player['gender'],
            rang=serialized_player['rang'],
            )
        return name

    def add_player_in_object_player_list(self, player):
        players_list.append(player)

    def create_player(self):
        name = self.get_player_name()
        first_name = self.get_player_first_name()
        date = self.get_date_of_birth()
        gender = self.get_gender()
        rang = self.get_player_rang()
        name = Player(
            name=name,
            first_name=first_name,
            date_of_birth=date,
            gender=gender,
            rang=rang
        )
        #name.rang = None
        self.add_player_in_object_player_list(player=name)
        return name

    def serialised_object_player_list(self):
        for player in players_list:
            self.add_player_in_database(player=player)

    def deserialized_all_player_in_database(self):
        for player in Data().table_of_player.all():
            players_list.append(
                self.add_player_in_object_player_list(
                    player=player
                )
            )





