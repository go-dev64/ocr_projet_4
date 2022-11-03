from ocr_projet_4.modeles.round import Round
from ocr_projet_4.modeles.match import Match


class Tournament:
    def __init__(self, name, place, date, time_controle, description):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_round = 4
        self.round_list = []
        self.players_list = []
        self.time_control = time_controle
        self.description = description

    def add_players(self, player):
        """add player to tournament"""
        self.players_list.extend(player)

    def add_tournament_description(self, description):
        self.description = description

    def add_round(self, round):
        self.round_list.append(round)

    def sort_player_list_by_rang(self):
        """sort list by rang, only in first round"""
        self.players_list = sorted(
            self.players_list,
            key=lambda player: player.rang
        )

    def sort_player_list_by_point(self):
        """ sort list by point """
        self.players_list = sorted(
            self.players_list,
            key=lambda player: player.number_point
        )

    def create_matchs_of_round_1(self):
        matchs_list_of_round1 = []
        len_list_divide_per_2 = int(len(self.players_list) / 2)
        for i in range(1, len_list_divide_per_2 + 1):
            i = Match(
                name=i,
                player1=self.players_list[i - 1],
                player2=self.players_list[len_list_divide_per_2 + i - 1]
            )
            i.get_color()
            matchs_list_of_round1.append(i)
        return matchs_list_of_round1

    @staticmethod
    def check_match_already_played(list_round, new_player1, new_player2):
        for old_round in list_round:
            for old_match in old_round:
                player_list = [old_match.player1, old_match.player2, new_player1, new_player2]
                number_player1 = player_list.count(new_player1)
                number_player2 = player_list.count(new_player2)
                if number_player1 + number_player2 == 4:
                    return False

    def create_matchs_of_next_round(self, list_round):
        matchs_list_of_other_round = []
        copy_list = self.players_list.copy()
        i = 0
        while len(copy_list) > 1:
            i += 1
            if self.check_match_already_played(
                    list_round=list_round,
                    new_player1=copy_list[0],
                    new_player2=copy_list[1]
            ):
                i = Match(
                    name=i,
                    player1=copy_list[1],
                    player2=copy_list[0]
                )
                i.get_color()
                matchs_list_of_other_round.append(i)
                copy_list.pop(0)
                copy_list.pop(0)
            else:
                i = Match(
                    name=i,
                    player1=copy_list[0],
                    player2=copy_list[2]
                )
                i.get_color()
                matchs_list_of_other_round.append(i)
                copy_list.pop(2)
                copy_list.pop(0)

        return matchs_list_of_other_round

    def __str__(self):
        return self.name + " de " + self.place

    def __repr__(self):
        return self.name + " de " + self.place
