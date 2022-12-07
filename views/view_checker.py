from datetime import datetime


class ViewChecker:

    @staticmethod
    def check_date():
        result = 0
        while result != 1:
            date = input("Entrer la date du tournoi:\n"
                         "Format JJ-MM-AAAA:")
            try:
                if date != datetime.strptime(date, "%d-%m-%Y").strftime('%d-%m-%Y'):
                    raise ValueError
            except ValueError:
                print("Format date invalide!")
            else:
                result += 1
                return date

    @staticmethod
    def check_string(list_choice):
        result = 0
        while result != 1:
            the_input = input("Indiquer votre  choix: Y / N\n").upper()
            result = list_choice.count(the_input)
            try:
                assert result == 1
            except AssertionError:
                print("Oooops! Entrée Invalide!")
            else:
                return the_input



    @staticmethod
    def check_num_choice(list_choice):
        """ list of choice start by 1 not 0"""
        result = 0
        while result != 1:
            the_input = input("Indiquer le numéro de votre choix:\n")
            try:
                the_input = int(the_input)
                assert 1 <= the_input < len(list_choice) + 1
            except ValueError:
                print("Oooops! Entrer un Numéro Valide!")
            except AssertionError:
                print("Oooops! Entrée Invalide!")
            else:
                result += 1
                return the_input


