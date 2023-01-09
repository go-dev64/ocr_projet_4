from views.view_checker import ViewChecker
from views.screen import Screen
from views.input import GetInfo


class ViewPlayer:
    def __init__(self):
        self.checker = ViewChecker()

    @staticmethod
    def display_player_rang(player_name, player_rang):
        print(
            f"{player_name} est actuellement au rang " f"N°{player_rang} du classement."
        )

    def change_player_rang(self, player, player_list):
        new_rang = GetInfo(pos_x=30, pos_y=5).get_new_rang_player(
            player=player,
            list_player=player_list
        )
        return new_rang

    @staticmethod
    def player_already_selected(player, list_where_player_exist):
        Screen().message(
            message=f"Le joueur {player} est deja inscrit dans {list_where_player_exist}!",
            title=" Message Erreur ! "
        )
