from ocr_projet_4.modeles.player import Player
from ocr_projet_4.modeles.match import Match


play_1 = Player(name="Toto", first_name="patrick",
                date_of_birth="11/02/88", gender="homme")
play_1.rang = 1
play_1.number_point = 10

play_2 = Player(name="Pitt", first_name="brad",
                date_of_birth="11/05/60", gender="homme")
play_2.rang = 3
play_2.number_point = 9
play_3 = Player(name="Portman", first_name="nathalie",
                date_of_birth="18/07/87", gender="femme")
play_3.rang = 2
play_3.number_point = 8
play_4 = Player(name="dupont", first_name="antoine",
                date_of_birth="11/22/90", gender="homme")
play_4.rang = 7
play_4.number_point = 7
play_5 = Player(name="Sansuss", first_name="laure",
                date_of_birth="14/03/2000", gender="femme")
play_5.rang = 5
play_5.number_point = 6
play_6 = Player(name="Mayans", first_name="marjorie",
                date_of_birth="25/09/2001", gender="femme")
play_6.rang = 6
play_6.number_point = 5
play_7 = Player(name="Penaud", first_name="Damian",
                date_of_birth="11/011/88", gender="homme")
play_7.rang = 4
play_7.number_point = 4
play_8 = Player(name="Guerdain", first_name="blanche",
                date_of_birth="11/02/88", gender="femme")
play_8.rang = 8
play_8.number_point = 1

list_players = [play_1, play_2, play_3, play_4, play_5, play_6, play_7, play_8]

toto = Match(name="match_1", player1=list_players[0], player2=list_players[1])
print(toto)



"""print(list_players)
sort_player_list_by_point(list_players)
sort_player_list_by_rang(list_players)"""

"""tournoi_a = Tournament(name="tournoi_a", place="bayonne", date="21/02/2022")
tournoi_a.time_control = "Blitz"
tournoi_a.add_players(list_players)
tournoi_a.add_tournament_description("test tournoi a")

tournoi_b = Tournament(name="tournoi_b", place="biarritz", date="22/02/2022")
tournoi_b.time_control = "Blitz"
tournoi_b.add_players(list_players)
tournoi_b.add_tournament_description("test tournoi b")

list_tournament = []"""

"""list_players.append(Player(name="Toto", first_name="patrick",
                           date_of_birth="11/02/88", gender="homme"))
list_players.append(Player(name="Pitt", first_name="brad",
                           date_of_birth="11/05/60", gender="homme"))
list_players.append(Player(name="Portman", first_name="nathalie",
                           date_of_birth="18/07/87", gender="femme"))
list_players.append(Player(name="dupont", first_name="antoine",
                           date_of_birth="11/22/90", gender="homme"))
list_players.append(Player(name="Sansuss", first_name="laure",
                           date_of_birth="14/03/2000", gender="femme"))
list_players.append(Player(name="Mayans", first_name="marjorie",
                           date_of_birth="25/09/2001", gender="femme"))
list_players.append(Player(name="Penaud", first_name="Damian",
                           date_of_birth="11/011/88", gender="homme"))
list_players.append(Player(name="Guerdain", first_name="blanche",
                           date_of_birth="11/02/88", gender="femme"))"""
