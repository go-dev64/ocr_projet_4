from tinydb import TinyDB, Query, where
import os



class Data:

    def __init__(self):
        self.db = TinyDB("../DataBase/db.json")
        self.table_of_player = self.db.table("table_of_player")
        self.table_of_tournament = self.db.table("table_of_tournament")
