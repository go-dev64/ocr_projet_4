from views.view_player import ViewPlayer
from modeles.player import Player
from controllers.control_data import Data, data_players_list
from views.view_checker import ViewChecker


class ControlPlayer:

    def __init__(self):
        self.view_player = ViewPlayer()
        self.view_checker = ViewChecker()
        self.data = Data()
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

    def change_rang_of_player(self):
        player = self.select_player_in_database()
        new_rang = self.view_player.change_player_rang(player)
        player.edit_grading(new_grading=new_rang)
        self.update_table_player_list_in_database(player=player)

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
            rang=player_info["rang"]
        )
        player.number_point = player_info["number_point"]
        player.id_player = player_info["id_player"]
        return player

    def create_new_player(self):
        player_info = self.get_info_player()
        player = self.instance_player(player_info=player_info)
        return player

    def select_player_in_database(self):
        player_selected = self.view_player.user_select_player(
            players_list=data_players_list
        )
        player = data_players_list[player_selected]
        return player

    def player_from_db(self, player, tournament):
        player_from_db = player
        if player_from_db in tournament.players_list:
            self.view_player.player_already_selected(
                player=player_from_db,
                list_where_player_exist= tournament
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

    def add_new_player_by_user(self):
        new_player = self.create_new_player()
        result = self.check_if_player_in_list(
            player=new_player,
            the_list=data_players_list
        )
        if result[0]:
            self.save_player(player=new_player)
            return new_player
        else:
            return None, result[1]

    def add_new_player_in_tournament(self, tournament):
        new_player = self.add_new_player_by_user()
        if new_player[0] is None:
            choice = self.view_player.valid_player_exist()
            if choice == 0:
                player_from_db = self.player_from_db(
                    player=new_player[1],
                    tournament=tournament
                )
                return player_from_db
            else:
                return None
        else:
            return new_player

    """ def add_new_player_in_tournament(self, tournament):
        new_player = self.create_new_player()
        result = self.check_if_player_in_list(
            player=new_player,
            the_list=data_players_list
        )
        if not result[0]:
            choice = self.view_player.valid_player_exist()
            if choice == 0:
                player_from_db = self.player_from_db(
                    player=result[1],
                    tournament=tournament
                )
                return player_from_db
            else:
                return None
        else:
            self.save_player(player=new_player)
            return new_player"""

    def save_player(self, player):
        self.add_player_in_instance_player_list(player=player)
        self.add_player_in_database(player=player)

    def add_player_in_database(self, player):
        serialized_name = player.serialized_player()
        id_player = self.data.table_of_player.insert(serialized_name)
        self.data.table_of_player.update({"id_player": id_player}, self.data.where("id_player") == id_player)

    @staticmethod
    def add_player_in_instance_player_list(player):
        data_players_list.append(player)

    def update_table_player_list_in_database(self, player):
        serialized_player = player.serialized_player()
        self.data.table_of_player.update(
            serialized_player, self.data.where("id_player") == player.id_player)

    def reload_all_player_in_data_players_list(self):
        for player in self.data.table_of_player.all():
            data_players_list.append(self.instance_player(
                player_info=player
            )
            )

    def return_player_from_data_player_list(self, player_serialized):
        for player in data_players_list:
            if player.id_player == player_serialized["id_player"]:
                return player

    def return_players_instance_list(self, serialized_player_list):
        """Convert a serialised player list in a instance player list"""
        players_list = []
        for serialized_player in serialized_player_list:
            player = self.return_player_from_data_player_list(
                player_serialized=serialized_player
            )
            players_list.append(player)
        return players_list

    def print_player_list_sort_by_rang(self, players_list):
        """sort list by rang"""
        players_list = sorted(
            players_list,
            key=lambda player: player.rang
        )
        position = 0
        for the_player in players_list:
            position += 1
            print(f"{position} - {the_player}")
        choice = self.view_player.user_continu()
        return choice

    def print_player_list_sort_by_name(self, players_list):
        """sort list by name"""
        players_list = sorted(
            players_list,
            key=lambda player: player.name
        )
        position = 0
        for the_player in players_list:
            position += 1
            print(f"{position} - {the_player}")
        choice = self.view_player.user_continu()
        return choice

    def add_player_by_player_menu(self):
        new_player = self.add_new_player_by_user()
        if new_player[0] is None:
            self.view_player.confirm_player_registration(
                player=new_player,
                player_list="la base de données!"
            )

    def menu_player(self):
        choice = 0
        while choice != 1:
            list_of_action = ["Afficher la liste de tous joueurs de la base de donnée",
                              "Afficher la liste de tous joueurs d'un tournoi",
                              "Enregistrer un nouveau joueur",
                              "Modifier le classement d'un joueur",
                              "Retour Menu Principal"
                              ]
            action_selected = self.view_player.view_menu_player(
                list_of_action=list_of_action
            )
            match action_selected:
                case 1:
                    self.print_player_list_sort_by_rang(
                        players_list=data_players_list
                    )
                    if self.view_player.user_continu():
                        continue
                    else:
                        break

                case 2:
                    self.print_player_list_sort_by_name(
                        players_list=data_players_list
                    )
                    if self.view_player.user_continu():
                        continue
                    else:
                        break
                case 3:
                    self.add_player_by_player_menu()
                    if self.view_player.user_continu():
                        continue
                    else:
                        break
                case 4:
                    self.change_rang_of_player()
                    if self.view_player.user_continu():
                        continue
                    else:
                        break
                case 5:
                    break

