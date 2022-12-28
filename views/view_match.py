from views.view_checker import ViewChecker


class ViewMatch:
    def __init__(self):
        self.checker = ViewChecker()

    def match_result(self, player_1, player_2):
        players = [player_1, player_2, "match nul"]
        print(
            "Sélectionner le résultat du match:\n"
            "1 - "
            f"Victoire de {player_1}\n"
            "2 - "
            f"Victoire de {player_2}\n"
            "3 - Match nul"
        )
        check = self.checker.check_num_choice(list_choice=players)
        match_result = check - 1
        if match_result == 0:
            print(f"Le vainqueur est {player_1}")
            return match_result
        elif match_result == 1:
            print(f"Le vainqueur est {player_2}")
            return match_result
        else:
            print("Match nul")
            return match_result
