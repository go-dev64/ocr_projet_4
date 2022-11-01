from ocr_projet_4.views.view_round import ViewRound
from ocr_projet_4.controllers.control_match import ControlMatch



class ControlRound:
    def __init__(self, tour, players_list):
        self.view_round = ViewRound()
        self.tour = tour

    def create_match(self):
        self.tour.get_match_of_round()

    def display_match_of_round(self):
        list_of_match = self.tour.list_of_match
        self.view_round.display_match(match_list=list_of_match)

    def select_match(self):
        match = self.view_round.select_match(match_list=self.tour.list_of_match)
        return match

    def start_round(self):
        self.view_round.view_start_of_round(name_of_round=self.tour)
        self.tour.start_of_round()

    def end_round(self):
        self.view_round.view_end_of_round(name_of_round=self.tour)
        self.tour.end_of_round()

    def input_match_result(self):
        match = self.tour.list_of_match[self.select_match()]
        result_match = ControlMatch(match=match).run()








    def select_match(self):
        match_selected = self.view_round.select_match(self.tour.list_of_match)
        return match_selected
