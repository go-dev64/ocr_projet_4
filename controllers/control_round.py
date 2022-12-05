from views.view_round import ViewRound
from controllers.control_match import ControlMatch
from controllers.control_player import ControlPlayer
from modeles.round import Round


class ControlRound:
    def __init__(self):
        self.view_round = ViewRound()
        self.control_match = ControlMatch()
        self.control_player = ControlPlayer()

    def display_match_of_round(self, round):
        list_of_match = round.match_in_progress
        self.view_round.display_match(
            match_list=list_of_match,
            round=round.name
        )

    def start_round(self, round):
        self.view_round.view_start_of_round(
            name_of_round=round.name
        )
        round.start_of_round()

    def end_round(self, round):
        self.view_round.view_end_of_round(
            name_of_round=round.name,
            player_list=round.in_game_player_list
        )
        round.end_of_round()

    def select_match(self, round):
        match_selected = self.view_round.select_match(
            round.match_in_progress
        )
        match = round.match_in_progress[match_selected]
        return match

    def input_match_result(self, round):
        match_selected = self.select_match(round=round)
        result_match = ControlMatch().run(match=match_selected)
        round.add_winner(result_match)
        round.take_out_the_finished_match(match_selected)

    def reload_match_of_round(self, matchs_list_serialized):
        matchs_list = []
        for match_serialized in matchs_list_serialized:
            matchs_list.append(self.control_match.reload_match(
                match_info=match_serialized)
            )
        return matchs_list

    def reload_round(self, round_info):
        round = Round(name=round_info["name"])
        round.list_of_match = self.reload_match_of_round(
            matchs_list_serialized=round_info["list_of_match"])
        round.match_in_progress = self.reload_match_of_round(
            matchs_list_serialized=round_info["match_in_progress"])
        self.control_player.reload_all_player_in_list(
            serialized_list=round_info["in_game_player_list"],
            instance_list=round.in_game_player_list
        )
        self.control_player.reload_all_player_in_list(
            serialized_list=round_info["player_list"],
            instance_list=round.players_list
        )
        round.date_of_start = round_info["date_of_start"]
        round.date_of_end = round_info["date_of_end"]
        round.hour_of_start = round_info["hour_of_start"]
        round.hour_of_end = round_info["hour_of_end"]
        return round

    def run_round(self, round):
        self.display_match_of_round(round=round)
        self.start_round(round=round)
        while len(round.match_in_progress) != 0:
            self.input_match_result(round=round)
        if len(round.match_in_progress) == 0:
            self.end_round(round=round)
