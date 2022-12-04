from views.view_checker import ViewChecker


class ViewPlayer:

    def __init__(self):
        self.checker = ViewChecker()

    @staticmethod
    def input_player_name():
        name = input("Entrer le nom du Joueur:\n")
        return name

    @staticmethod
    def input_player_first_name():
        first_name = input("Entrer le prénom du Joueur:\n")
        return first_name

    def input_date_of_birth(self):
        date = self.checker.check_date()
        return date

    def input_gender(self):
        gender_list = ["Femme", "Homme"]
        print("Sélectionner un genre:")
        gender_number = 0
        for gender in gender_list:
            gender_number += 1
            print(f"{gender_number}: {gender}")
        check = self.checker.check_num_choice(
            list_choice=gender_list
        )
        gender_selected = check - 1
        print(f"Vous avez sélectionner le genre:\n"
              f"{gender_list[gender_selected]}")
        return gender_list[gender_selected]

    @staticmethod
    def display_player_rang(player_name, player_rang):
        print(f"{player_name} est actuellement au rang "
              f"N°{player_rang} du classement.")

    def change_player_rang(self, player_name, player_rang):
        new_rang = None
        list_of_choice = ["Y", "N"]
        self.display_player_rang(
            player_name=player_name,
            player_rang=player_rang
        )
        print(f"Vous modifier le rang du joueur: "
              f"{player_name}")
        check = self.checker.check_string(
                list_choice=list_of_choice
        )
        if check == "Y":
            result_ok = 0
            while result_ok != 1:
                try:
                    rang = int(input(f"Entrer le nouveau rang au classement"
                                     f" de {player_name}:"))
                except ValueError:
                    print("Oooops, Entrer Invalide. Entrer un Nombre!")
                else:
                    result_ok += 1
                    new_rang = rang
            print(f"\nNouveau Rang de {player_name}: {new_rang}")
            return new_rang

        else:
            return None

    @staticmethod
    def input_player_rang():
        print("Renseigner le classement du Joueur / de la Joueuse\n")
        result_ok = 0
        while result_ok != 1:
            try:
                rang = int(input(f"Entrer le rang au classement"))
            except ValueError:
                print("Oooops, Entrer Invalide. Entrer un Nombre!")
            else:
                result_ok += 1
                return rang

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

    def valid_player_exist(self):
        print("Joueur deja existant dans la base de données.\n")
        list_of_action = ["Sélectionner le joueur/joueuse existant-e",
                          "Recommencer la saisie"]
        print("Voulez-vous:")
        choice = 0
        for action in list_of_action:
            choice += 1
            print(f"{choice}: {action}")
        check = self.checker.check_num_choice(
            list_choice=list_of_action
        )
        action_selected = check - 1
        return action_selected

    @staticmethod
    def player_already_selected(player):
        print(f"\n{player} est deja inscrit à ce tournoi!")
