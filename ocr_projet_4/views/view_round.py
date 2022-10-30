class ViewRound:

    def select_match(self, match_list):
        print("Sélectionner un match:")
        match_number = 0
        for match in match_list:
            match_number += 1
            print(f"Macth Numéro {match_number}: {match}")
        match_selected = int(input("Entrer le numéro du match:\n"))
        print(f"Vous avez sélectionner le match: {match_list[match_selected]}")
        return match_selected

