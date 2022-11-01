from ocr_projet_4.views.view_match import ViewMatch
import ocr_projet_4.test as test

tata = test.toto


class ControlMatch:
    def __init__(self):
        self.match = tata
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

    def run(self):
        result = self.get_result_match()
        self.match.result_of_match(result=result)
        self.match.give_player_point(result=result)
        self.match.save_match()


"""go = ControlMatch()
print(go.player_1.number_point)
print(go.player_2.number_point)
go.run()
print(go.player_1.number_point)
print(go.player_2.number_point)"""










