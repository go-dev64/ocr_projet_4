from views.view_checker import ViewChecker
from views.window import Window
from views.screen import Screen
from views.option_selection import Confirmation


class ViewGeneric:
    def __init__(self):
        self.checker = ViewChecker()

    @staticmethod
    def confirm_element_registration(message, title):
        Screen().message(
            message=message,
            title=title
        )

    @staticmethod
    def confirm_choice(message, title=None):
        choice = Confirmation(text=message, title=title).select_option()
        return choice

    def user_select_element(self, list_of_elements, type_of_element, sort_by=None):
        list_of_elements = list_of_elements
        print(f"Sélectionner un {type_of_element}:")
        self.display_elements_of_list(elements_list=list_of_elements, sort_by=sort_by)
        check = self.checker.check_num_choice(list_choice=list_of_elements)
        element_selected = check - 1
        print(f"Vous avez sélectionner:\n" f"{list_of_elements[element_selected]}")
        return element_selected

    def view_menu(self, list_of_choice, name_of_menu):
        print(f"{name_of_menu}")
        n = 0
        for element in list_of_choice:
            n += 1
            print(f"{n} - {element}")
        user_choice = self.checker.check_num_choice(list_choice=list_of_choice)
        return user_choice


    def display_elements_of_list(self, elements_list, sort_by=None):
        if sort_by == "rang":
            list_sorted = sorted(elements_list, key=lambda player: player.rang)
            compteur = 0
            for element in list_sorted:
                compteur += 1
                print(f"{compteur} - {element}: N°{element.rang} au classement")
        else:
            compteur = 0
            for element in elements_list:
                compteur += 1
                print(f"{compteur} - {element}")


