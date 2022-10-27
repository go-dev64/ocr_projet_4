from datetime import datetime


class Round:
    def __init__(self, name):
        self.name = name
        self.list_of_match = []
        self.date_of_start = date_of_start
        self.hour_of_start = hour_of_start
        self.date_of_end = date_of_end
        self.hour_of_end = hour_of_end

    def start_of_round(self):
        self.date_of_start = datetime.today().strftime("%d/%m/%y")
        self.hour_of_start = datetime.today().isoformat(timespec="seconds")








