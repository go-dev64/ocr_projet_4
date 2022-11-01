class ViewRound:

    def display_match(self, match_list):
        match_number = 0
        for match in match_list:
            match_number += 1
            print(f"Macth Numéro {match_number}: {match}")

    def select_match(self, match_list):
        print("Sélectionner un match:")
        match_number = 0
        for match in match_list:
            match_number += 1
            print(f"Macth Numéro {match_number}: {match}")
        match_selected = int(input("Entrer le numéro du match:\n")) - 1
        print(f"Vous avez sélectionner le match: {match_list[match_selected]}")
        return match_selected

    def view_start_of_round(self, name_of_round):
        print(f"Voulez-vous lancez le {name_of_round}?: Y/N")
        start = input("Votre choix:").upper()
        if start == "Y":
            return start

    def view_end_of_round(self, name_of_round):
        print(f"Fin du {name_of_round}?: Y/N")
        end = input("Votre choix:").upper()
        if end == "Y":
            return end




