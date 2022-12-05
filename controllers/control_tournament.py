from controllers.control_round import ControlRound
from controllers.control_data import Data, data_tournaments_list
from controllers.control_player import ControlPlayer
from modeles.round import Round
from modeles.tournament import Tournament
from views.view_control_tournament import ViewControlTournament
from views.view_tournament import ViewTournament
import random


class ControlTournament:

    def __init__(self):

        self.view_control_tournament = ViewControlTournament()
        self.view_tournament = ViewTournament()
        self.control_player = ControlPlayer()
        self.control_round = ControlRound()

    def create_round(self, name, tournament):
        round = Round(name=name)
        tournament.add_round(round)
        return round

    def view_create_round(self, name_of_round):
        create_round = self.view_control_tournament.view_create_new_round(
            name_of_round=name_of_round
        )
        return create_round

    def create_matchs_of_round_1(self, tournament):
        len_list_divide_per_2 = int(
            len(tournament.players_list) / 2
        )
        for i in range(1, len_list_divide_per_2 + 1):
            tournament.round_list[-1].create_match(
                name=i,
                player_1=tournament.players_list[i - 1],
                player_2=tournament.players_list[
                    len_list_divide_per_2 + i - 1
                    ]
            )

    def define_first_round(self, tournament):
        first_round = self.create_round(name="Round 1",
                                        tournament=tournament)
        tournament.sort_player_list_by_rang()
        first_round.players_list = tournament.players_list
        self.create_matchs_of_round_1(tournament=tournament)
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

    def create_matchs_of_next_round(self, list_round, list_player, tournament):
        copy_list = list_player.copy()
        compteur = 0
        while len(
                tournament.round_list[-1].list_of_match
        ) < tournament.number_of_player/2:
            if compteur > tournament.number_of_player:
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
                    tournament.round_list[-1].create_match(
                        name=i,
                        player_1=player1,
                        player_2=player2)
                    copy_list.pop(copy_list.index(player2))
                    copy_list.pop(0)
                    break

        if not self.number_of_match_by_round(tournament=tournament):
            self.pop_last_match_of_round(tournament=tournament)
            free_player_list = self.get_free_players(tournament=tournament)
            self.create_matchs_of_next_round(
                list_round=tournament.round_list,
                list_player=free_player_list,
                tournament=tournament
                )

    def number_of_match_by_round(self, tournament):
        for the_round in tournament.round_list:
            if len(the_round.list_of_match) < tournament.number_of_round:
                return False
        return True

    def pop_last_match_of_round(self, tournament):
        tournament.round_list[-1].list_of_match.pop()

    def get_unfree_players_of_last_round(self, tournament):
        unfree_layers_list = []
        for match in tournament.round_list[-1].list_of_match:
            unfree_layers_list.append(match.player1)
            unfree_layers_list.append(match.player2)
        return unfree_layers_list

    def get_free_players(self, tournament):
        unfree_players = self.get_unfree_players_of_last_round(
            tournament=tournament
        )
        free_players = tournament.players_list.copy()
        for player in unfree_players:
            free_players.pop(player)
        random.shuffle(free_players)
        return free_players

    def force_match(self, tournament):
        if not self.number_of_match_by_round(
                tournament=tournament
        ):
            free_player_list = self.get_free_players(
                tournament=tournament
            )
            player_1 = free_player_list[0]
            player_2 = free_player_list[1]
            tournament.round_list[-1].create_match(
                name="last_match",
                player_1=player_1,
                player_2=player_2
            )

    def define_next_round(self, name, tournament):
        next_round = self.create_round(
            name=name,
            tournament=tournament
        )
        tournament.sort_player_list_by_point()
        next_round.players_list = tournament.players_list
        self.create_matchs_of_next_round(
            list_round=tournament.round_list,
            list_player=tournament.players_list,
            tournament=tournament
        )
        next_round.match_in_progress = next_round.list_of_match.copy()
        return next_round

    def display_end_of_tournament(self, tournament):
        tournament.sort_player_list_by_point()
        self.view_control_tournament.view_end_tournament(
            tournament=tournament
        )

    def reload_tournaments_round(self, serialized_rounds_list):
        list_of_rounds_instance = []
        for round_serialized in serialized_rounds_list:
            list_of_rounds_instance.append(
                self.control_round.reload_round(
                    round_info=round_serialized
                )
            )
        return list_of_rounds_instance

    def reload_tournament(self, tournament):
        the_tournament = Tournament(
            name=tournament['name'],
            place=tournament['place'],
            date=tournament['date'],
            time_control=tournament['time_control'],
            description=tournament['description']
        )
        self.control_player.reload_all_player_in_list(
            serialized_list=tournament["players_list"],
            instance_list=the_tournament.players_list
        )
        the_tournament.number_of_round = tournament["number_of_round"]
        the_tournament.number_of_player = tournament["number_of_player"]
        the_tournament.round_list = self.reload_tournaments_round(
            serialized_rounds_list=tournament["round_list"]
        )
        return the_tournament

    def reload_all_tournament_in_database(self):
        for tournament in Data().table_of_tournament.all():
            data_tournaments_list.append(self.reload_tournament(
                    tournament=tournament
                )
            )

    def run(self, tournament):
        if self.view_create_round(name_of_round="Round 1"):
            first_round = self.define_first_round(tournament=tournament)
            round = ControlRound()
            round.run_round(round=first_round)
            for round in range(2, tournament.number_of_round + 1):
                next_round = self.define_next_round(
                    name=f"Round {round}",
                    tournament=tournament
                )
                round = ControlRound()
                round.run_round(round=next_round)
            self.display_end_of_tournament(tournament=tournament)


go = ControlTournament()
go.reload_all_tournament_in_database()
print(data_tournaments_list)
print(data_tournaments_list)

go.run(tournament=data_tournaments_list[-1])

