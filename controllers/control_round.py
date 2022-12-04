from views.view_round import ViewRound
from controllers.control_match import ControlMatch
from modeles.round import Round


class ControlRound:
    def __init__(self, tour, players_list):
        self.view_round = ViewRound()
        self.tour = tour
        self.player_list = players_list

    def display_match_of_round(self):
        list_of_match = self.tour.match_in_progress
        self.view_round.display_match(
            match_list=list_of_match,
            round=self.tour.name
        )

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
        match_selected = self.view_round.select_match(
            self.tour.match_in_progress
        )
        match = self.tour.match_in_progress[match_selected]
        return match

    def input_match_result(self):
        match = self.select_match()
        result_match = ControlMatch(match=match).run()
        self.tour.add_winner(result_match)
        self.tour.take_out_the_finished_match(match)

    def deserialized_round(self, round_info):
        round = Round(name=round_info["name"])
        round.list_of_match = round_info["list_of_match"]
        round.match_in_progress = round_info["match_in_progress"]
        round.in_game_player_list = round_info["in_game_player_list"]
        round.players_list = round_info["player_list"]
        round.date_of_start = round_info["date_of_start"]
        round.date_of_end = round_info["date_of_end"]
        round.hour_of_start = round_info["hour_of_start"]
        round.hour_of_end = round_info["hour_of_end"]
        return round

    def toto(self):
        list= []
        for element in list:
            list.append()



    def run_round(self):
        self.display_match_of_round()
        self.start_round()
        while len(self.tour.match_in_progress) != 0:
            self.input_match_result()
        if len(self.tour.match_in_progress) == 0:
            self.end_round()
