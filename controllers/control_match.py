from views.view_match import ViewMatch
from modeles.match import Match
from controllers.control_player import ControlPlayer


class ControlMatch:
    def __init__(self):
        self.control_player = ControlPlayer()
        self.view_match = ViewMatch()

    def get_result_match(self, match):
        """return
        0: Winner is player 1,
        1 : Winner is player 2
        2 : draw"""
        result = ViewMatch().match_result(
            player_1=match.player1, player_2=match.player2
        )
        return result

    def return_result(self, match, result):
        if result == 0:
            return [match.player1]
        elif result == 1:
            return [match.player2]
        else:
            return [match.player1, match.player2]

    def reload_match_result(self, match_result):
        list_player1 = [
            self.control_player.find_player_in_data_player_list(
                player_serialized=match_result["player1"]
            ),
            match_result["result_player1"],
        ]
        list_player2 = [
            self.control_player.find_player_in_data_player_list(
                player_serialized=match_result["player2"]
            ),
            match_result["result_player2"],
        ]
        match_result = (list_player1, list_player2)
        return match_result

    def reload_match(self, match_info):
        match = Match(
            name=match_info["name"],
            player1=self.control_player.find_player_in_data_player_list(
                player_serialized=match_info["player1"]
            ),
            player2=self.control_player.find_player_in_data_player_list(
                player_serialized=match_info["player2"]
            ),
        )
        match.finished_match = match_info["finished_match"]
        match.player_with_black_piece = (
            self.control_player.find_player_in_data_player_list(
                player_serialized=match_info["player_with_black_piece"]
            )
        )
        match.result_player1 = match_info["result_player1"]
        match.result_player2 = match_info["result_player2"]
        match.match_result = self.reload_match_result(
            match_result=match_info["match_result"]
        )
        return match

    def play_match(self, match):
        result = self.get_result_match(match=match)
        match.result_of_match(result=result)
        match.give_player_point(result=result)
        match.status_match_is_finish()
        match.save_result_of_match()
        self.control_player.data.update_player_in_database(player=match.player1)
        self.control_player.data.update_player_in_database(player=match.player2)
        winner = self.return_result(match=match, result=result)
        return winner
