class Player:

    def __init__(self, name, first_name, date_of_birth, gender):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.grading = 0
        self.number_point = 0

    def __str__(self):
        return f"{self.name}"