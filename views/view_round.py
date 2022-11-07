from ocr_projet_4.controllers.control_checker import ControlChecker


class ViewRound:
    def __init__(self):
        self.checker = ControlChecker()

    def display_match(self, match_list, round):
        print(f"Liste des match du {round}:")
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
        match_selected = input("Entrer le numéro du match:\n")

        check = self.checker.check_num_choice(
            this_input=match_selected,
            list_choice=match_list)

        if check:
            match_selected = int(match_selected) - 1
            print(f"Vous avez sélectionner le match: {match_list[match_selected]}")
            return match_selected

        else:
            self.select_match(match_list)

    def view_start_of_round(self, name_of_round):
        name_of_round = name_of_round
        list_of_choice = ["Y", "N", "E"]
        print(f"Voulez-vous lancez le {name_of_round} ?: Y / N")
        the_input = input("Votre choix:").upper()
        check_round = self.checker.check_string(
            this_input=the_input,
            list_choice=list_of_choice
        )
        if check_round:
            print(f"\nLe {name_of_round} est lancé!")
            match round:
                case "Y":
                    return True
                case "N":
                    return False
                case "E":
                    return False
        else:
            self.view_start_of_round(name_of_round)

    def view_end_of_round(self, name_of_round, player_list):
        print(f"Fin du {name_of_round}!")
        print("Les vainqueurs sont:")
        for player in player_list:
            print(player)



"""go = ViewRound()
go.select_match(match_list=["match1", "match2", "match3"])
go.view_start_of_round(name_of_round="toto")
"""