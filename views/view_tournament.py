from controllers.control_checker import ControlChecker


class ViewTournament:

    def __init__(self):
        self.checker = ControlChecker()

    @staticmethod
    def user_choice_of_name_of_tournament():
        print("Entrer le nom du tournoi: ")
        name = input("Nom du tournoi:")
        return name

    @staticmethod
    def user_choice_of_place_of_tournament():
        print("Renseigner le lieu du tournoi")
        place = input("lieu du Tournoi:")
        return place

    def user_choice_of_date_of_tournament(self):
        date = self.checker.check_date()
        return date

    def user_choice_of_control_time(self, list_type_of_time):
        list_of_type_of_match = list_type_of_time
        print(" Sélectionner le type Controle de temps:\n")
        type_number = 0
        for match_type in list_of_type_of_match:
            type_number += 1
            print(f"{type_number} - {match_type}")
        check = self.checker.check_num_choice(
            list_choice=list_of_type_of_match
        )
        type_match_selected = check - 1
        print(f"Vous avez choisi comme controle de temps:"
              f"{list_of_type_of_match[type_match_selected]}")
        return list_of_type_of_match[type_match_selected]

    @staticmethod
    def user_choice_of_description_of_tournament():
        print("Renseigner une description du tournoi:")
        descritption = input("Description: ")
        return descritption

    def user_choice_of_player(self):
        """define if user select old player or create new player
        args : list [

        """
        list_choice = ["Sélectionner un joueur ou une joueuse dans notre base de donnée",
                       "Entrer un nouveau joueur/joueuse"]
        print("Choix des joueurs:\n"
              "Voulez-vous:\n")
        choice_number = 0
        for choice in list_choice:
            choice_number += 1
            print(f"{choice_number} - {choice}")
        check = self.checker.check_num_choice(
            list_choice=list_choice
        )
        choice_selected = check - 1
        print(f"Vous avez sélectionner :\n"
              f"{list_choice[choice_selected]}")
        return choice_selected

    def user_select_player(self, players_list):
        players_list = players_list
        print("Sélectionner un joueur:")
        choice_player = 0
        for player in players_list:
            choice_player += 1
            print(f"{choice_player} - {player}")
        check = self.checker.check_num_choice(
            list_choice=players_list
        )
        player_selected = check - 1
        print(f"Vous avez sélectionner:\n"
              f"{players_list[player_selected]}")
        return player_selected

    @staticmethod
    def player_already_selected(player):
        print(f"\n{player} est deja inscrit à ce tournoi!")
