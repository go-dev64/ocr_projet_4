from tinydb import TinyDB, Query, where


tournaments_list = []
players_list = []


class Data:

    def __init__(self):
        self.db = TinyDB("../DataBase/db.json")
        self.table_of_player = self.db.table("table_of_player")
        self.table_of_tournament = self.db.table("table_of_tournament")


db = Data()

for i in db.table_of_player:
    print(i)
print(len(db.table_of_player))
print(db.table_of_player.all())
for i in db.table_of_tournament:
    print(i)
print(len(db.table_of_tournament))
