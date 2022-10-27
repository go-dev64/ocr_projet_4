from datetime import datetime


class Round:
    def __init__(self, name):
        self.name = name
        self.list_of_match = []
        self.date_of_start = "date_of_start"
        self.hour_of_start = "hour_of_start"
        self.date_of_end = "date_of_end"
        self.hour_of_end = "hour_of_end"

    def start_of_round(self):
        self.date_of_start = self.get_time_now()[1]
        self.hour_of_start = self.get_time_now()[1]

    def end_of_round(self):
        self.date_of_end = self.get_time_now()[1]
        self.hour_of_end = self.get_time_now()[1]

    def get_time_now(self):
        date = datetime.today().strftime("%d/%m/%y")
        hour = datetime.today().isoformat(timespec="seconds")
        return date, hour

    def __str__(self):
        return f"{self.name}", f"{self.list_of_match}"

