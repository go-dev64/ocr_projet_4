from ocr_projet_4.controllers.control_checker import ControlChecker


class ViewPlayer:

    def __init__(self):
        self.checker = ControlChecker()

    def input_player_name(self):
        name = input("Entrer le nom du Joueur:\n")
        return name

    def input_player_first_name(self):
        first_name = input("Entrer le prénom du Joueur:\n")
        return first_name

    def input_date_of_birth(self):
        date = self.checker.check_date()
        return date

    def input_gender(self, gender_list):
        gender_list = gender_list
        print("Sélectionner un genre:")
        gender_number = 0
        for gender in gender_list:
            gender_number += 1
            print(f"{gender_number}: {gender}")
        check = self.checker.check_num_choice(
            list_choice=gender_list
        )
        gender_selected = check - 1
        print(f"Vous avez sélectionner le match:\n"
              f"{gender_list[gender_selected]}")
        return gender_selected

    def display_player_rang(self, player_name, player_rang):
        print(f"{player_name} est actuellement au rang "
              f"N°{player_rang} du classement.")

    def change_player_rang(self, player_name, player_rang):
        new_rang = None
        list_of_choice = ["Y", "N"]
        self.display_player_rang(
            player_name=player_name,
            player_rang=player_rang
        )
        print(f"Vous modifier le rang du joueur :\n"
              f"{player_name}?")
        check = self.checker.check_string(
                list_choice=list_of_choice
        )
        if check == "Y":
            print(f"Entrer le nouveau rang au classement"
                  f" du joueur:{player_name}:")
            try:
                rang = int(input("Rang:"))
            except ValueError:
                print("Oooops, Entrer Invalide. Entrer un Nombre!")
            else:
                new_rang = rang
            return new_rang
        else:
            return None



