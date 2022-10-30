from ocr_projet_4.test import list_players, get_match_of_round


class ViewMatch:

    def select_match(self, match_list):
        print("Sélectionner un match:")
        match_number = 0
        for match in match_list:
            match_number += 1
            print(f"Macth Numéro {match_number}: {match}")
        match_selected = int(input("Entrer le numéro du match:\n"))
        print(f"Vous avez sélectionner le match: {match_list[match_selected]}")
        return match_selected

    def match_result(self, player_1, player_2):
        print("Sélctionner le vainqueur du match:\n"
              "1 - " f"{player_1}\n"
              "2 - " f"{player_2}\n"
              "3 - Match nul")
        result = int(input("Résultat du match: "))
        match result:
            case 1:
                print(f"Le vainqueur est {player_1}")
            case 2:
                print(f"Le vainqueur est {player_2}")
            case 3:
                print("Match nul")
        return result


go = ViewMatch()
tata = go.match_result(player_1=list_players[0], player_2=list_players[2])
print(tata)
