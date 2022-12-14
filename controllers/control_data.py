from tinydb import TinyDB, Query, where


data_tournaments_list = []
data_players_list = []


class Data:
    def __init__(self):
        self.db = TinyDB("DataBase/db.json")
        self.table_of_player = self.db.table("table_of_player")
        self.table_of_tournament = self.db.table("table_of_tournament")
        self.where = where
        self.query = Query()

    def add_tournament_in_database(self, tournament):
        serialized_tournament = tournament.serialized_tournament()
        id_tournament = self.table_of_tournament.insert(serialized_tournament)
        self.table_of_tournament.update(
            {"id_tournament": id_tournament},
            self.where("id_tournament") == id_tournament,
        )

    def update_tournament_in_database(self, tournament):
        serialized_tournament = tournament.serialized_tournament()
        self.table_of_tournament.update(
            serialized_tournament,
            self.where("id_tournament") == tournament.id_tournament,
        )

    def save_new_player_in_database(self, player):
        serialized_name = player.serialized_player()
        id_player = self.table_of_player.insert(serialized_name)
        self.table_of_player.update(
            {"id_player": id_player}, self.where("id_player") == id_player
        )

    def update_player_in_database(self, player):
        serialized_player = player.serialized_player()
        self.table_of_player.update(
            serialized_player, self.where("id_player") == player.id_player
        )
