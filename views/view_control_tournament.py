class ViewControlTournament:

    def view_select_tournament(self, tournament_list):
        print("Sélection du tournoi")
        number = 0
        for tournament in tournament_list:
            number += 1
            print(f"{number} - {tournament}")

        tournament_selected = int(input("Indiquer votre choix:"))
        return tournament_selected

    def view_create_first_round(self):
        print(" Génerer le Round 1")
        round_1 = input("y/n")
        if round_1 == "y":
            return True
        else:
            return False


