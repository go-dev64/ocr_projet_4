from ocr_projet_4.controllers.control_checker import ControlChecker


class ViewMatch:

    def __init__(self):
        self.checker = ControlChecker()

    def match_result(self, player_1, player_2):
        players = [player_1, player_2, "match nul"]
        print("Sélctionner le resultat du match:\n"
              "1 - " f"Victoire de {player_1}\n"
              "2 - " f"Victoire de {player_2}\n"
              "3 - Match nul")
        result = input("Indiquer votre choix:")
        valid_result = self.checker.check_num_choice(
            this_input=result,
            list_choice=players
        )
        if valid_result:
            match int(result):
                case 1:
                    print(f"Le vainqueur est {player_1}")
                    return int(result)
                case 2:
                    print(f"Le vainqueur est {player_2}")
                    return int(result)
                case 3:
                    print("Match nul")
                    return int(result)
        else:
            self.match_result(player_1=players[0],
                              player_2=players[1]
                              )



"""go = ViewMatch()
go.match_result(player_1='toto', player_2='tata')"""