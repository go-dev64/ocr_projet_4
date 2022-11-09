from ocr_projet_4.views.view_player import ViewPlayer
from ocr_projet_4.modeles.player import Player
from ocr_projet_4.DataBase.control_data import Data


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

    def create_player(self):
        name = self.get_player_name()
        first_name = self.get_player_first_name()
        date = self.get_date_of_birth()
        gender = self.get_gender()
        name = Player(
            name=name,
            first_name=first_name,
            date_of_birth=date,
            gender=gender)
        name.rang = None
        serialized_name = name.serialized_player()
        Data().db.table("table_of_players").insert(serialized_name)
        return name

