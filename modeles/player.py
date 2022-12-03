class Player:

    def __init__(self,
                 name,
                 first_name,
                 date_of_birth,
                 gender,
                 rang):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rang = rang
        self.number_point = 0

    def serialized_player(self):
        serialized_player = {
            "name": self.name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "rang": self.rang,
            "number_point": self.number_point
         }
        return serialized_player

    def edit_grading(self, new_grading):
        self.rang = new_grading

    def __str__(self):
        return f"{self.name} {self.first_name}"

    def __repr__(self):
        return f"{self.name} {self.first_name}"
