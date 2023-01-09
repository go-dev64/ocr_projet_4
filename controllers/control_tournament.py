from controllers.control_data import Data, data_tournaments_list
from controllers.control_generic import Generic
from controllers.control_player import ControlPlayer
from controllers.control_round import ControlRound
from modeles.round import Round
from modeles.tournament import Tournament
from views.view_control_tournament import ViewControlTournament


class ControlTournament:
    def __init__(self):

        self.view_control_tournament = ViewControlTournament()
        self.view_tournament = ViewControlTournament()
        self.control_player = ControlPlayer()
        self.control_round = ControlRound()
        self.generic = Generic()
        self.data = Data()
        self.data_tournaments_list = data_tournaments_list

    def create_round(self, name, tournament):
        round = Round(name=name)
        tournament.add_round(round)
        return round

    def create_matchs_of_round_1(self, tournament):
        players_list_divide_per_2 = int(tournament.number_of_player / 2)
        for i in range(1, players_list_divide_per_2 + 1):
            tournament.round_list[-1].create_match(
                name=f"match {i}",
                player_1=tournament.players_list[i - 1],
                player_2=tournament.players_list[players_list_divide_per_2 + i - 1],
            )

    def define_first_round(self, tournament):
        first_round = self.create_round(name="Round 1", tournament=tournament)
        tournament.sort_player_list_by_rang()
        first_round.players_list = tournament.players_list
        self.create_matchs_of_round_1(tournament=tournament)
        first_round.match_in_progress = first_round.list_of_match.copy()
        self.data.update_tournament_in_database(tournament=tournament)
        return first_round

    def define_next_round(self, name, tournament):
        next_round = self.create_round(name=name, tournament=tournament)
        tournament.sort_player_list_by_point()
        next_round.players_list = tournament.players_list
        self.create_matchs_of_next_round(
            list_round=tournament.round_list,
            list_player=tournament.players_list,
            tournament=tournament,
        )
        next_round.match_in_progress = next_round.list_of_match.copy()
        self.data.update_tournament_in_database(tournament=tournament)
        return next_round

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
        while (
            len(tournament.round_list[-1].list_of_match)
            < tournament.number_of_player / 2
        ):
            if compteur > tournament.number_of_player:
                break
            compteur += 1
            player1 = copy_list[0]
            for player2 in copy_list:
                if player2 == player1:
                    continue
                already_played = self.check_match_already_played(
                    list_round=list_round, player_1=player1, player_2=player2
                )
                if not already_played:
                    match_name = len(tournament.round_list[-1].list_of_match) + 1
                    tournament.round_list[-1].create_match(
                        name=f"match {match_name}", player_1=player1, player_2=player2
                    )
                    copy_list.pop(copy_list.index(player2))
                    copy_list.pop(0)
                    break

        if not self.number_of_match_by_round(tournament=tournament):
            self.force_match(tournament=tournament, player_list=copy_list)

    def number_of_match_by_round(self, tournament):
        last_round = tournament.round_list[-1]
        if len(last_round.list_of_match) < tournament.number_of_player / 2:
            return False
        return True

    def force_match(self, tournament, player_list):
        player_1 = player_list[0]
        player_2 = player_list[1]
        tournament.round_list[-1].create_match(
            name="last_match", player_1=player_1, player_2=player_2
        )

    def end_of_tournament(self, tournament):
        tournament.sort_player_list_by_point()
        self.view_control_tournament.view_end_tournament(tournament=tournament)
        tournament.change_status()
        self.data.update_tournament_in_database(tournament=tournament)

    def reload_tournaments_round(self, serialized_rounds_list):
        list_of_rounds_instance = []
        for round_serialized in serialized_rounds_list:
            list_of_rounds_instance.append(
                self.control_round.reload_round(round_info=round_serialized)
            )
        return list_of_rounds_instance

    def reload_tournament(self, tournament):
        the_tournament = Tournament(
            name=tournament["name"],
            place=tournament["place"],
            date=tournament["date"],
            time_control=tournament["time_control"],
            description=tournament["description"],
        )
        the_tournament.players_list.extend(
            self.control_player.get_players_instance_list(
                serialized_player_list=tournament["players_list"]
            )
        )
        the_tournament.number_of_round = tournament["number_of_round"]
        the_tournament.number_of_player = tournament["number_of_player"]
        the_tournament.round_list.extend(
            self.reload_tournaments_round(
                serialized_rounds_list=tournament["round_list"]
            )
        )
        the_tournament.status = tournament["status"]
        the_tournament.id_tournament = tournament["id_tournament"]
        return the_tournament

    def reload_all_tournament_in_database(self):
        for tournament in self.data.table_of_tournament.all():
            self.data_tournaments_list.append(
                self.reload_tournament(tournament=tournament)
            )

    def tournament_in_progress(self):
        tournament_in_progress = []
        for tournament in self.data_tournaments_list:
            if tournament.status == "en cours":
                tournament_in_progress.append(tournament)
        return tournament_in_progress

    def launch_round(self, tournament, round):
        if self.control_round.launch_of_round(round=round) is None:
            return None
        else:
            if (
                self.control_round.play_round(tournament=tournament, round=round)
                is None
            ):
                return None
            else:
                return True

    def apply_first_round(self, tournament):
        first_round = self.define_first_round(tournament=tournament)
        round = self.launch_round(tournament=tournament, round=first_round)
        return round

    def apply_next_round(self, tournament):
        number_round = len(tournament.round_list) + 1
        next_round = self.define_next_round(
            name=f"Round {number_round}", tournament=tournament
        )
        round = self.launch_round(tournament=tournament, round=next_round)
        return round

    def condition(self, tournament):
        try:
            result = len(tournament.round_list[3].match_in_progress)
            assert result == 0
        except IndexError:
            return False
        except AssertionError:
            return False
        else:
            return True

    def play_tournament(self, tournament):
        while len(tournament.round_list) < 5:
            if self.condition(tournament=tournament):
                self.end_of_tournament(tournament=tournament)
                break
            if len(tournament.round_list) == 0:
                if self.apply_first_round(tournament=tournament) is None:
                    break
                else:
                    continue

            elif len(tournament.round_list[-1].match_in_progress) == 0:
                if self.apply_next_round(tournament=tournament) is None:
                    break
                else:
                    continue
            elif len(tournament.round_list[-1].match_in_progress) != 0:
                if (
                    self.control_round.play_round(
                        tournament=tournament,
                        round=tournament.round_list[-1],
                    )
                    is None
                ):
                    break
                else:
                    continue
