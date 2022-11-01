from ocr_projet_4.views.view_match import ViewMatch


class ControlMatch:
    def __init__(self, match):
        self.match = match
        self.view_match = ViewMatch()
        self.player_1 = self.match.player1
        self.player_2 = self.match.player2

    def get_result_match(self):
        """ return
        1 : Winner is player 1,
        2 : Winner is player 2
        3 : draw """
        result = ViewMatch().match_result(
            player_1=self.player_1,
            player_2=self.player_2)
        return result

    def return_result(self, result):
        match result:
            case 1:
                return [self.player_1]
            case 2:
                return [self.player_2]
            case 3:
                return [self.player_1, self.player_2]

    def run(self):
        result = self.get_result_match()
        self.match.result_of_match(result=result)
        self.match.give_player_point(result=result)
        self.match.save_match()
        winner = self.return_result(result=result)
        return winner




"""go = ControlMatch(test.toto)
print(go.player_1.number_point)
print(go.player_2.number_point)
go.run()
print(go.player_1.number_point)
print(go.player_2.number_point)"""










