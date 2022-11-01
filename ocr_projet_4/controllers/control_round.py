from ocr_projet_4.views.view_round import ViewRound
from ocr_projet_4.modeles.round import Round
from ocr_projet_4.modeles.match import Match


class ControlRound:
    def __init__(self):
        self.view_round = ViewRound()

    def select_match(self, list_match):
        match_selected = self.view_round.select_match(match_list=list_match)
        return match_selected
