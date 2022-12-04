from controllers.control_round import ControlRound
from controllers.control_data import Data, data_tournaments_list
from controllers.control_player import ControlPlayer
from modeles.round import Round
from modeles.tournament import Tournament
from views.view_control_tournament import ViewControlTournament
from views.view_tournament import ViewTournament
import random


class ControlTournament:

    def __init__(self, tournament):
        self.tournament = tournament
        self.view_control_tournament = ViewControlTournament()
        self.view_tournament = ViewTournament()

    def create_round(self, name):
        round = Round(name=name)
        self.tournament.add_round(round)
        return round

    def view_create_round(self, name_of_round):
        create_round = self.view_control_tournament.view_create_new_round(
            name_of_round=name_of_round
        )
        return create_round

    def create_matchs_of_round_1(self):
        len_list_divide_per_2 = int(
            len(self.tournament.players_list) / 2
        )
        for i in range(1, len_list_divide_per_2 + 1):
            self.tournament.round_list[-1].create_match(
                name=i,
                player_1=self.tournament.players_list[i - 1],
                player_2=self.tournament.players_list[
                    len_list_divide_per_2 + i - 1
                    ]
            )

    def define_first_round(self):
        first_round = self.create_round(name="Round 1")
        self.tournament.sort_player_list_by_rang()
        first_round.players_list = self.tournament.players_list
        self.create_matchs_of_round_1()
        first_round.match_in_progress = first_round.list_of_match.copy()
        return first_round

    @staticmethod
    def check_match_already_played(list_round, player_1, player_2):
        for old_round in list_round:
            for old_match in old_round.list_of_match:
                old_player1 = old_match.player1
                old_player2 = old_match.player2
                if player_1 is old_player1 or player_1 is old_player2:
                    if player_2 is old_player1 or player_2 is old_player2:
                        return True
        return False

    def create_matchs_of_next_round(self, list_round, list_player):
        copy_list = list_player.copy()
        compteur = 0
        while len(
                self.tournament.round_list[-1].list_of_match
        ) < self.tournament.number_of_player/2:
            if compteur > self.tournament.number_of_player:
                break
            compteur += 1
            i = compteur
            player1 = copy_list[0]
            for player2 in copy_list:
                if player2 == player1:
                    continue
                already_played = self.check_match_already_played(
                    list_round=list_round,
                    player_1=player1,
                    player_2=player2
                )
                if not already_played:
                    self.tournament.round_list[-1].create_match(
                        name=i,
                        player_1=player1,
                        player_2=player2)
                    copy_list.pop(copy_list.index(player2))
                    copy_list.pop(0)
                    break

        if not self.number_of_match_by_round():
            self.pop_last_match_of_round()
            free_player_list = self.get_free_players()
            self.create_matchs_of_next_round(
                list_round=self.tournament.round_list,
                list_player=free_player_list
                )

    def number_of_match_by_round(self):
        for the_round in self.tournament.round_list:
            if len(the_round.list_of_match) < self.tournament.number_of_round:
                return False
        return True

    def pop_last_match_of_round(self):
        self.tournament.round_list[-1].list_of_match.pop()

    def get_unfree_players_of_last_round(self):
        unfree_layers_list = []
        for match in self.tournament.round_list[-1].list_of_match:
            unfree_layers_list.append(match.player1)
            unfree_layers_list.append(match.player2)
        return unfree_layers_list

    def get_free_players(self):
        unfree_players = self.get_unfree_players_of_last_round()
        free_players = self.tournament.players_list.copy()
        for player in unfree_players:
            free_players.pop(player)
        random.shuffle(free_players)
        return free_players

    def force_match(self):
        if not self.number_of_match_by_round():
            free_player_list = self.get_free_players()
            player_1 = free_player_list[0]
            player_2 = free_player_list[1]
            self.tournament.round_list[-1].create_match(
                name="last_match",
                player_1=player_1,
                player_2=player_2
            )

    def define_next_round(self, name):
        next_round = self.create_round(name=name)
        self.tournament.sort_player_list_by_point()
        next_round.players_list = self.tournament.players_list
        self.create_matchs_of_next_round(
            list_round=self.tournament.round_list,
            list_player=self.tournament.players_list
        )
        next_round.match_in_progress = next_round.list_of_match.copy()
        return next_round

    def display_end_of_tournament(self):
        self.tournament.sort_player_list_by_point()
        self.view_control_tournament.view_end_tournament(
            tournament=self.tournament
        )

    def reload_tournament(self, tournament):
        name = Tournament(
            name=tournament['name'],
            place=tournament['place'],
            date=tournament['date'],
            time_control=tournament['time_control'],
            description=tournament['description']
        )
        name.players_list.extend(
            self.reload_tournament_players(
                tournament=tournament
            )
        )
        return name

    def reload_tournament_players(self, tournament):
        tournament_players_list = []
        for tournament_player in tournament['players_list']:
            player = ControlPlayer().instance_player(
                player_info=tournament_player
            )
            tournament_players_list.append(player)
        return tournament_players_list

    def deserialized_all_tournament_in_database(self):
        for tournament in Data().table_of_tournament.all():
            data_tournaments_list.append(self.reload_tournament(
                    tournament=tournament
                )
            )

    def run(self):
        if self.view_create_round(name_of_round="Round 1"):
            first_round = self.define_first_round()
            round = ControlRound(tour=first_round,
                                 players_list=self.tournament.players_list
                                 )

            round.run_round()
            for round in range(2, self.tournament.number_of_round + 1):
                next_round = self.define_next_round(name=f"Round {round}")
                round = ControlRound(tour=next_round,
                                     players_list=self.tournament.players_list
                                     )
                round.run_round()
            self.display_end_of_tournament()
