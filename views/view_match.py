from ocr_projet_4.controllers.control_checker import ControlChecker


class ViewMatch:

    def __init__(self):
        self.checker = ControlChecker()

    def match_result(self, player_1, player_2):
        players = [player_1, player_2, "match nul"]
        print("Sélectionner le résultat du match:\n"
              "1 - " f"Victoire de {player_1}\n"
              "2 - " f"Victoire de {player_2}\n"
              "3 - Match nul")
        check = self.checker.check_num_choice(
            list_choice=players
        )
        match_result = check - 1
        match match_result:
            case 1:
                print(f"Le vainqueur est {player_1}")
                return match_result
            case 2:
                print(f"Le vainqueur est {player_2}")
                return match_result
            case 3:
                print("Match nul")
                return match_result
