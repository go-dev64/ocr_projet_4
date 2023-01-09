from views.view_player import ViewPlayer
from modeles.player import Player
from controllers.control_generic import Generic
from views.view_generic import ViewGeneric
from views.input import GetInfo
from views.display_menu import MenuDisplay,  Confirmation, Screen
from controllers.control_data import Data, data_players_list


class ControlPlayer:
    def __init__(self):
        self.view_player = ViewPlayer()
        self.view_generic = ViewGeneric()
        self.generic = Generic()
        self.data = Data()
        self.data_players_list = data_players_list
        self.player_info = {}

    def get_id_player(self):
        id_player = len(self.data.table_of_player) + 1
        return id_player

    def get_info_player(self):
        get_player = GetInfo(pos_x=30, pos_y=5)
        player_info = get_player.get_info_player()
        player_info["number_point"] = 0
        player_info["id_player"] = self.get_id_player()
        player_info["rang"] = None
        return player_info

    @staticmethod
    def instance_player(player_info):
        player = Player(
            name=player_info["name"],
            first_name=player_info["first_name"],
            date_of_birth=player_info["date_of_birth"],
            gender=player_info["gender"],
        )
        player.rang = player_info["rang"]
        player.number_point = player_info["number_point"]
        player.id_player = player_info["id_player"]
        return player

    def create_new_player(self):
        player_info = self.get_info_player()
        player = self.instance_player(player_info=player_info)
        return player

    def move_player_on_new_rang(self, player, players_list):
        players_list.pop(players_list.index(player))
        players_list.insert(player.rang - 1, player)
        for element in players_list:
            element.rang = 1 + players_list.index(element)
            self.data.update_player_in_database(player=element)

    def change_rang_of_player(self, player_selected):
        players_list_sorted = sorted(
            self.data_players_list, key=lambda player: player.rang
        )
        new_rang = self.view_player.change_player_rang(player_selected, players_list_sorted)
        confirm = self.view_generic.confirm_choice(message=f"Valider le nouveau classement de {player_selected}?",
                                                   title=f"Nouveau classement de {player_selected}: {new_rang}"
                                                   )
        if confirm:
            player_selected.edit_grading(new_grading=new_rang)
            self.move_player_on_new_rang(
                player=player_selected, players_list=players_list_sorted
            )

    def check_if_player_is_tournament_players_list(self, player, tournament):
        player_from_db = player
        if player_from_db in tournament.players_list:
            self.view_player.player_already_selected(
                player=player_from_db, list_where_player_exist=tournament
            )
            return None
        else:
            return player_from_db

    @staticmethod
    def check_if_player_in_list(player, the_list):
        for element in the_list:
            if element.name == player.name:
                if element.first_name == player.first_name:
                    if element.date_of_birth == player.date_of_birth:
                        if element.gender == player.gender:
                            return False, element

        return True, player

    def add_new_player_by_user(self, name_of_list):
        new_player = self.create_new_player()
        result = self.check_if_player_in_list(
            player=new_player, the_list=self.data_players_list
        )
        if result[0]:
            self.save_player(player=new_player)
            self.view_generic.confirm_element_registration(
                message=f"Création du {new_player}.",
                title="Confirmation creation joueur"
            )
            return True, new_player
        else:
            self.view_player.player_already_selected(
                player=new_player, list_where_player_exist=name_of_list
            )
            return result

    def add_new_player_in_tournament(self, tournament):
        new_player = self.add_new_player_by_user(name_of_list="la base de donnée")
        if not new_player[0]:
            choice = self.view_generic.confirm_choice(message="Sélectionner le joueur existant?",
                                                      title=f"{new_player} est deja inscrit dans la base de données!")
            if choice == 0:
                player_from_db = self.check_if_player_in_list(
                    player=new_player[1], the_list=tournament
                )
                return player_from_db
            else:
                return None
        else:
            return new_player[1]

    def save_player(self, player):
        player.rang = len(self.data_players_list) + 1
        self.data_players_list.append(player)
        self.data.save_new_player_in_database(player=player)

    def instancing_all_player_in_data_players_list(self):
        for player in self.data.table_of_player.all():
            data_players_list.append(self.instance_player(player_info=player))

    def find_player_in_data_player_list(self, player_serialized):
        """
        find player in data player list
        :param player_serialized:
        :return: instance of player from data player list
        """
        for player in self.data_players_list:
            if player.id_player == player_serialized["id_player"]:
                return player

    def get_players_instance_list(self, serialized_player_list):
        """Convert a serialised player list in instance player list"""
        players_list = []
        for serialized_player in serialized_player_list:
            player = self.find_player_in_data_player_list(
                player_serialized=serialized_player
            )
            players_list.append(player)
        return players_list

    def display_players_list(self, players_list):
        """
        display players list by name or rang
        :param players_list: data players list
        :return: function of display list sorted
        """
        while True:
            list_of_action = [
                "Trier les joueurs par classement",
                "Trier les joueurs par ordre alphabétique",
                "Retourner au Menu précédent"
            ]
            action_main_menu = MenuDisplay(
                elements_list=list_of_action,
                confirm_text="Voulez-vous retourner au menu précédent?",
                title="Menu Joueur"
            )
            action_main_menu.menu_selector()
            action_selected = action_main_menu.index_selected

            if action_selected == 0:
                """display player by rang"""
                action_main_menu = MenuDisplay(
                    elements_list=sorted(players_list, key=lambda player: player.rang),
                    confirm_text="Voulez-vous retourner au menu précédent?",
                    title="Classement des joueur de la base de données"
                )
                action_main_menu.display_list()

            elif action_selected == 1:
                """display player by name"""
                action_main_menu = MenuDisplay(
                    elements_list=sorted(players_list, key=lambda player: player.name),
                    confirm_text="Voulez-vous retourner au menu précédent?",
                    title="Liste des joueurs dans la base de données triés par ordre alphabtique"
                )
                action_main_menu.display_list()

            else:
                choice = Confirmation(text="Voulez-vous retourner au menu précédent?").select_option()
                if choice:
                    break
