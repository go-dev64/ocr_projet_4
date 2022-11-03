from ocr_projet_4.modeles.round import Round
from ocr_projet_4.views.view_control_tournament import ViewControlTournament
from ocr_projet_4.views.view_tournament import ViewTournament
from ocr_projet_4.controllers.control_round import ControlRound



class ControlTournament:

    def __init__(self, tournament):
        self.tournament = tournament
        self.view_control_tournament = ViewControlTournament()
        self.view_tournament = ViewTournament()

    def create_round(self, name):
        round = Round(name=name)
        self.tournament.add_round(round)
        return round

    def view_create_round(self):
        x = self.view_control_tournament.view_create_first_round()
        return x

    def define_first_round(self):
        first_round = self.create_round(name="Round 1")
        self.tournament.sort_player_list_by_rang()
        first_round.players_list = self.tournament.players_list
        first_round.list_of_match = self.tournament.create_matchs_of_round_1()
        first_round.match_in_progress = first_round.list_of_match.copy()
        return first_round

    def define_next_round(self, name):
        next_round = self.create_round(name=name)
        self.tournament.sort_player_list_by_point()
        next_round.players_list = self.tournament.players_list
        next_round.list_of_match = self.tournament.create_matchs_of_next_round(
            list_round=self.tournament.round_list
        )
        next_round.match_in_progress = next_round.list_of_match.copy()
        return next_round

    def run(self):
        if self.view_create_round():
            first_round = self.define_first_round()
            round = ControlRound(tour=first_round,
                                 players_list=self.tournament.players_list
                                 )

            round.run_round()
            for round in range(2, self.tournament.number_of_round + 1):
                next_round = 0
                next_round = self.define_next_round(name=f"Round {round}")
                round = ControlRound(tour=next_round,
                                     players_list=self.tournament.players_list
                                     )
                round.run_round()











