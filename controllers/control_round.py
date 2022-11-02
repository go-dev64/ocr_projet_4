from ocr_projet_4.views.view_round import ViewRound
from ocr_projet_4.controllers.control_match import ControlMatch


class ControlRound:
    def __init__(self, tour, players_list):
        self.view_round = ViewRound()
        self.tour = tour
        self.player_list = players_list

    def create_match_of_round1(self):
        self.tour.sort_player_list_by_rang()
        self.tour.create_matchs_of_round_1()

    def create_match_next_round(self):
        self.tour.sort_player_list_by_point()
        self.tour.create_matchs_of_next_round()

    def display_match_of_round(self):
        list_of_match = self.tour.list_of_match
        self.view_round.display_match(match_list=list_of_match)

    def start_round(self):
        self.view_round.view_start_of_round(
            name_of_round=self.tour.name
        )
        self.tour.start_of_round()

    def end_round(self):
        self.view_round.view_end_of_round(
            name_of_round=self.tour.name,
            player_list=self.tour.in_game_player_list
        )
        self.tour.end_of_round()

    def select_match(self):
        match_selected = self.view_round.select_match(self.tour.list_of_match)
        match = self.tour.list_of_match[match_selected]
        return match

    def input_match_result(self):
        match = self.select_match()
        result_match = ControlMatch(match=match).run()
        self.tour.add_winner(result_match)
        self.tour.take_out_the_finished_match(match)

    def run_round(self):
        self.display_match_of_round()
        self.start_round()
        while len(self.tour.list_of_match) != 0:
            self.input_match_result()
        if len(self.tour.list_of_match) == 0:
            self.end_round()







