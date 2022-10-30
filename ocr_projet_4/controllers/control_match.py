from ocr_projet_4.views.view_match import ViewMatch


class ControlMatch:

    def __int__(self, match):
        self.match = match
        self.view_match = ViewMatch()
        self.player_1 = self.match.player1
        self.player_2 = self.match.player2

    def get_result_match(self):
        """ return
        1 : Winner is player 1,
        2 : Winner is player 2
        3 : draw """
        result = self.view_match.match_result(
            player_1=self.player_1,
            player_2=self.player_2)
        return result

    def run(self):
        result = self.get_result_match()
        self.match.result_of_match(result=result)
        self.match.give_player_point(result=result)
        self.match.save_match()





