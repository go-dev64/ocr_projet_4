from ocr_projet_4.modeles.player import Player
from ocr_projet_4.modeles.round import Round
from ocr_projet_4.controllers.control_round import ControlRound
from ocr_projet_4.modeles.match import Match



play_1 = Player(name="Toto", first_name="patrick",
                date_of_birth="11/02/88", gender="homme")
play_1.rang = 1
play_1.number_point = 0

play_2 = Player(name="Pitt", first_name="brad",
                date_of_birth="11/05/60", gender="homme")
play_2.rang = 3
play_2.number_point = 0
play_3 = Player(name="Portman", first_name="nathalie",
                date_of_birth="18/07/87", gender="femme")
play_3.rang = 2
play_3.number_point = 0
play_4 = Player(name="dupont", first_name="antoine",
                date_of_birth="11/22/90", gender="homme")
play_4.rang = 7
play_4.number_point = 0
play_5 = Player(name="Sansuss", first_name="laure",
                date_of_birth="14/03/2000", gender="femme")
play_5.rang = 5
play_5.number_point = 0
play_6 = Player(name="Mayans", first_name="marjorie",
                date_of_birth="25/09/2001", gender="femme")
play_6.rang = 6
play_6.number_point = 0
play_7 = Player(name="Penaud", first_name="Damian",
                date_of_birth="11/011/88", gender="homme")
play_7.rang = 4
play_7.number_point = 0
play_8 = Player(name="Guerdain", first_name="blanche",
                date_of_birth="11/02/88", gender="femme")
play_8.rang = 8
play_8.number_point = 0

list_players = [play_1, play_2, play_3, play_4, play_5, play_6, play_7, play_8]

round_1 = Round(name="round 1", players_list=list_players)
got = ControlRound(round_1, players_list=list_players)
got.run_round()
list_round = [round_1]




