from views.view_player import ViewPlayer
from modeles.player import Player
from controllers.control_generic import Generic
from controllers.control_data import Data, data_players_list, data_tournaments_list


class ControlPlayer:

    def __init__(self):
        self.view_player = ViewPlayer()
        self.generic = Generic()
        self.data = Data()
        self.data_players_list = data_players_list
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

    def get_id_player(self):
        id_player = len(self.data.table_of_player) + 1
        return id_player

    def get_info_player(self):
        player_info = {"name": self.get_player_name(),
                       "first_name": self.get_player_first_name(),
                       "date_of_birth": self.get_date_of_birth(),
                       "gender": self.get_gender(),
                       "rang": self.get_player_rang(),
                       "number_point": 0,
                       "id_player": self.get_id_player()
                       }
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
            self.update_player_in_database(player=element)

    def change_rang_of_player(self):
        players_list_sorted = sorted(self.data_players_list, key=lambda player: player.rang)
        player_selected = self.generic.select_element_in_list(
            list_of_elements=players_list_sorted,
            type_of_element="joueur",
            sort_by="rang"
        )
        new_rang = self.view_player.change_player_rang(player_selected)
        if new_rang is not None:
            player_selected.edit_grading(new_grading=new_rang)
            self.move_player_on_new_rang(player=player_selected, players_list=players_list_sorted)

    def check_if_player_is_tournament_players_list(self, player, tournament):
        player_from_db = player
        if player_from_db in tournament.players_list:
            self.view_player.player_already_selected(
                player=player_from_db,
                list_where_player_exist=tournament
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
            player=new_player,
            the_list=data_players_list
        )
        if result[0]:
            self.save_player(player=new_player)
            self.generic.view_generic.confirm_element_registration(
                element=new_player,
                elements_list=name_of_list
            )
            return True, new_player
        else:
            self.view_player.player_already_selected(
                player=new_player,
                list_where_player_exist=name_of_list
            )
            return result

    def add_new_player_in_tournament(self, tournament):
        new_player = self.add_new_player_by_user(name_of_list="la base de donnée")
        if not new_player[0]:
            choice = self.view_player.valid_player_exist()
            if choice == 0:
                player_from_db = self.check_if_player_in_list(
                    player=new_player[1],
                    the_list=tournament
                )
                return player_from_db
            else:
                return None
        else:
            return new_player[1]

    def save_player(self, player):
        player.rang = int(len(data_players_list))
        data_players_list.append(player)
        self.save_new_player_in_database(player=player)

    def save_new_player_in_database(self, player):
        serialized_name = player.serialized_player()
        id_player = self.data.table_of_player.insert(serialized_name)
        self.data.table_of_player.update(
            {"id_player": id_player},
            self.data.where("id_player") == id_player
        )

    def update_player_in_database(self, player):
        serialized_player = player.serialized_player()
        self.data.table_of_player.update(
            serialized_player,
            self.data.where("id_player") == player.id_player
        )

    def instancing_all_player_in_data_players_list(self):
        for player in self.data.table_of_player.all():
            data_players_list.append(
                self.instance_player(player_info=player)
            )

    def find_player_in_data_player_list(self, player_serialized):
        for player in data_players_list:
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

    def display_players_list(self, players_list, name_of_menu):
        while True:
            list_of_action = ["Trier les joueurs par classement",
                              "Trier les joueurs par ordre alphabétique",
                              "Retour au menu précédent"
                              ]
            action_selected = self.generic.action_selected_in_menu_by_user(
                actions_list=list_of_action,
                name_of_menu=name_of_menu
            )
            match action_selected:
                case 1:
                    list_sorted_by_rang = sorted(players_list, key=lambda player: player.rang)
                    self.generic.view_generic.display_elements_of_list(
                        elements_list=list_sorted_by_rang,
                        sort_by="rang"
                    )
                    if self.generic.view_generic.back_to_menu(name="Menu Joueur"):
                        break
                    else:
                        continue
                case 2:
                    list_sorted_by_name = sorted(players_list, key=lambda player: player.name)
                    self.generic.view_generic.display_elements_of_list(
                        elements_list=list_sorted_by_name,
                        sort_by="name"
                    )
                    if self.generic.view_generic.back_to_menu(name="Menu Joueur"):
                        break
                    else:
                        continue
                case 3:
                    break

    def menu_player(self):
        choice = 0
        while choice != 1:
            list_of_action = ["Afficher la liste de tous joueurs de la base de donnée",
                              "Afficher la liste de tous joueurs d'un tournoi",
                              "Enregistrer un nouveau joueur",
                              "Modifier le classement d'un joueur",
                              "Retour Menu Principal"
                              ]
            action_selected = self.generic.action_selected_in_menu_by_user(
                actions_list=list_of_action,
                name_of_menu="Menu Joueur"
            )
            match action_selected:
                case 1:
                    self.display_players_list(
                        players_list=data_players_list,
                        name_of_menu="Menu Joueur / Liste des Joueur dans la base de données"
                    )
                case 2:
                    tournament = self.generic.select_element_in_list(
                        list_of_elements=data_tournaments_list,
                        type_of_element="tournoi",
                        sort_by="name"
                    )
                    self.display_players_list(
                        players_list=tournament.players_list,
                        name_of_menu=f"Menu Joueur / Liste des Joueur du {tournament}"
                    )
                case 3:
                    self.add_new_player_by_user(name_of_list="la base de donnée")

                case 4:
                    self.change_rang_of_player()
                case 5:
                    break
