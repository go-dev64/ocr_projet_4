from ocr_projet_4.controllers.control_checker import ControlChecker


class ViewControlTournament:

    def __init__(self):
        self.checker = ControlChecker()

    def view_select_tournament(self, tournament_list):
        print("Sélection du tournoi")
        number = 0
        for tournament in tournament_list:
            number += 1
            print(f"{number} - {tournament}")
        check = self.checker.check_num_choice(
            list_choice=tournament_list
        )
        tournament_selected = check - 1
        print(f"Vous avez sélectionner le tournoi:\n"
              f"{tournament_list[tournament_selected]}")
        return tournament_selected

    @staticmethod
    def view_end_tournament(tournament):
        print(f"Le {tournament} est terminé!\n"
              "Résultat du tournoi:")
        for player in tournament.players_list:
            print(
                f"{tournament.players_list.index(player)+ 1 } - "
                f"{player} avec {player.number_point} points")

    def view_create_new_round(self, name_of_round):
        name_of_round = name_of_round
        list_of_choice = ["Y", "N", "E"]
        print(f"Génerer le {name_of_round} ?:")
        check = self.checker.check_string(
            list_choice=list_of_choice
        )
        if check == "Y":
            print(f"Creation du {name_of_round}!")
            return True
        else:
            return False
