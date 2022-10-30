from ocr_projet_4.test import list_players, get_match_of_round


class ViewMatch:

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

