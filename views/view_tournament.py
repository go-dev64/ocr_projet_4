from views.view_checker import ViewChecker


class ViewTournament:

    def __init__(self):
        self.checker = ViewChecker()

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
        print("Choix des joueurs,Voulez-vous:\n")
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

    def confirm_player_registration(self, player, tournament):
        print(f"{player} inscrit au {tournament}")

    def confirm_creation_tournament(self, tournament):
        print(f"Création de Tournoi: {tournament}")

    def confirm_launch_new_tournament(self, tournament):
        print(f"Voulez vous commencer le tournoi: {tournament} ?")
        list_choice = ["Yes", "No"]
        choice = self.checker.check_string(list_choice=list_choice)
        return choice
