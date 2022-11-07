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

        tournament_selected = int(input("Indiquer votre choix:"))
        return tournament_selected

    def view_create_new_round(self, name_of_round):
        name_of_round = name_of_round
        list_of_choice = ["Y", "N", "E"]
        print(f" Génerer le {name_of_round} ?: Y / N")
        round = input("Indiquer votre  choix:\n").upper()
        check_round = self.checker.check_string(
            this_input=round,
            list_choice=list_of_choice
        )
        if check_round:
            print(f"Creation du {name_of_round}!")
            match round:
                case "Y":
                    return True
                case "N":
                    return False
                case "E":
                    return False
        else:
            self.view_create_new_round(name_of_round)

    def view_end_tournament(self, tournament):
        print(f"Le {tournament} est terminé!\n"
              "Résultat du touroi:")
        for player in tournament.players_list:
            print(f"{tournament.players_list.index(player)+ 1 } - {player} avec {player.number_point} points")





"""go = ViewControlTournament()
go.view_create_new_round(name_of_round="toto")"""
