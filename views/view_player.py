from views.view_checker import ViewChecker


class ViewPlayer:

    def __init__(self):
        self.checker = ViewChecker()

    @staticmethod
    def input_player_name():
        name = input("Entrer le nom du Joueur:\n").capitalize()
        return name

    @staticmethod
    def input_player_first_name():
        first_name = input("Entrer le prénom du Joueur:\n").capitalize()
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

    def change_player_rang(self, player):
        new_rang = None
        list_of_choice = ["Y", "N"]
        self.display_player_rang(
            player_name=player.name,
            player_rang=player.rang
        )
        print(f"Vous modifier le rang du joueur: "
              f"{player.name}")
        check = self.checker.check_string(
                list_choice=list_of_choice
        )
        if check == "Y":
            result_ok = 0
            while result_ok != 1:
                try:
                    rang = int(input(f"Entrer le nouveau rang au classement"
                                     f" de {player.name}:"))
                except ValueError:
                    print("Oooops, Entrer Invalide. Entrer un Nombre!")
                else:
                    result_ok += 1
                    new_rang = rang
            print(f"\nNouveau Rang de {player.name}: {new_rang}")
            return new_rang

        else:
            return None

    @staticmethod
    def input_player_rang():
        print(f"Renseigner le classement du Joueur:\n")
        result_ok = 0
        while result_ok != 1:
            try:
                rang = int(input(f"Entrer le rang au classement"))
            except ValueError:
                print("Oooops, Entrer Invalide. Entrer un Nombre!")
            else:
                result_ok += 1
                return rang

    def user_select_element(self, list_of_elements, type_of_element):
        list_of_elements = list_of_elements
        print(f"Sélectionner un {type_of_element}:")
        choice_element = 0
        for element in list_of_elements:
            choice_element += 1
            print(f"{choice_element} - {element}")
        check = self.checker.check_num_choice(
            list_choice=list_of_elements
        )
        element_selected = check - 1
        print(f"Vous avez sélectionner:\n"
              f"{list_of_elements[element_selected]}")
        return element_selected

    @staticmethod
    def player_already_selected(player, list_where_player_exist):
        print(f"\n{player} est deja inscrit dans {list_where_player_exist}!")

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

    def confirm_player_registration(self, player, player_list):
        print(f"{player} inscrit dans {player_list}")

    def view_menu_player(self, list_of_action):
        print("Menu joueur")
        list_of_action = list_of_action
        for action in list_of_action:
            print(f"{int(list_of_action.index(action) + 1)} - {action}")

        action_selected = self.checker.check_num_choice(
            list_choice=list_of_action
        )
        return action_selected

    def back_to_menu(self):
        list_of_choice = ["Y", "N"]
        print("Voulez-vous retourner au Menu précédent ?")
        check = self.checker.check_string(
            list_choice=list_of_choice
        )
        if check == "Y":
            return True
        else:
            return False
