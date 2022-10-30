from ocr_projet_4.views.view_match import ViewMatch


class ControlMatch:

    def __int__(self, match):
        self.view_match = ViewMatch()

    def select_match(self, list_match):
        match_selected = self.view_match.select_match(match_list=list_match)
        return match_selected

    def result_match(self, player_1, player_2):
        result = self.view_match.match_result(player_1=player_1, player_2=player_2)
        return result


