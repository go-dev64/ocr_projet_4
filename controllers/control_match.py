from views.view_match import ViewMatch
from modeles.match import Match
from controllers.control_player import ControlPlayer


class ControlMatch:
    def __init__(self):
        self.control_player = ControlPlayer()
        self.view_match = ViewMatch()

    def get_result_match(self, match):
        """ return
        1 : Winner is player 1,
        2 : Winner is player 2
        3 : draw """
        result = ViewMatch().match_result(
            player_1=match.player_1,
            player_2=match.player_2)
        return result

    def return_result(self, match, result):
        match result:
            case 1:
                return [match.player_1]
            case 2:
                return [match.player_2]
            case 3:
                return [match.player_1, match.player_2]

    def reload_match(self, match_info):
        match = Match(
            name=match_info["name"],
            player1=self.control_player.instance_player(
                player_info=match_info["player1"]
            ),
            player2=self.control_player.instance_player(
                player_info=match_info["player2"]
            )
        )
        match.finished_match = match_info["finished_match"]
        match.player_with_black_piece = match_info["player_with_black_piece"]
        match.result_player1 = match_info["result_player1"]
        match.result_player2 = match_info["result_player2"]
        match.data = match_info["data"]
        return match

    def run(self, match):
        result = self.get_result_match(match=match)
        match.result_of_match(result=result)
        match.give_player_point(result=result)
        match.status_match_is_finish()
        match.save_match()
        winner = self.return_result(match=match, result=result)
        return winner
