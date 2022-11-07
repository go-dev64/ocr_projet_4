from datetime import datetime


class ControlChecker:

    def check_date(self, this_input):
        if this_input != datetime.strptime(this_input, "%d/%m/%y"):
            print("Format date invalide!")
            return False
        else:
            return True

    def check_string(self, this_input, list_choice):
        try:
            valid = list_choice.count(this_input)
            if valid < 1:
                print("Oooops! Entrée Invalide!")
                return False
        except:
            print("Oooops! Entrée Invalide!")
        else:
            return True

    def check_num_choice(self, this_input, list_choice):
        """ list of choice start by 1 not 0"""
        try:
            result = int(this_input)
            if result < 1 or result > len(list_choice)+1:
                print("Oooops! Entrée Invalide!")
                return False
        except ValueError:
            print("Oooops! Entrée Invalide!")
            return False
        else:
            return True
