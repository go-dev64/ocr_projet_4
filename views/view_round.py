from views.view_checker import ViewChecker


class ViewRound:
    def __init__(self):
        self.checker = ViewChecker()

    @staticmethod
    def display_match(match_list, round):
        print(f"Voici la liste des match du prochain Round: Le {round}:")
        match_number = 0
        for match in match_list:
            match_number += 1
            print(f"Macth Numéro {match_number}: {match}")

    def select_match(self, match_list):
        match_list = match_list
        print("Sélectionner un match:")
        match_number = 0
        for match in match_list:
            match_number += 1
            print(f"Macth Numéro {match_number}: {match}")
        check = self.checker.check_num_choice(
            list_choice=match_list
        )
        match_selected = check - 1
        print(f"Vous avez sélectionner le match:\n"
              f"{match_list[match_selected]}")
        return match_selected

    def confirm_play_next_match(self):
        list_of_choice = ["Y", "N"]
        print(f"Voulez-vous entrer le résultat d'un autre match ?: Y / N")
        check = self.checker.check_string(
            list_choice=list_of_choice
        )
        if check == "Y":
            return True
        else:
            return False

    def view_start_of_round(self, name_of_round):
        name_of_round = name_of_round
        list_of_choice = ["Y", "N"]
        print(f"Voulez-vous commencer le {name_of_round} ?: Y / N")
        check = self.checker.check_string(
            list_choice=list_of_choice
        )
        if check == "Y":
            print(f"\nLe {name_of_round} est lancé!")
            return True
        else:
            return False

    @staticmethod
    def view_end_of_round(name_of_round, winner_players_list):
        print(f"Fin du {name_of_round}!")
        print("Les vainqueurs sont:")
        for player in winner_players_list:
            print(player)
