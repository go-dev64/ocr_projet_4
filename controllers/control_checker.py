from datetime import datetime


class ControlChecker:

    def check_date(self, this_input):
        if this_input != datetime.strptime(this_input, "%d/%m/%y"):
            print("Format date invalide!")
            return False
        else:
            return True

    def check_string(self, list_choice):
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

    def check_num_choice(self, list_choice):
        """ list of choice start by 1 not 0"""
        result = 0
        while result != 1:
            the_input = input("Indiquer le numéro de votre choix:\n")
            try:
                the_input = int(the_input)
                assert 1 <= the_input < len(list_choice) + 1
            except ValueError:
                print("Ooops! Entrer un Numéro Valide!")
            except AssertionError:
                print("Oooops! Entrée Invalide!")
            else:
                result += 1
                return the_input
