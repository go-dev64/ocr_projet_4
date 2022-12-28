from views.view_checker import ViewChecker
import curses
from toto import MenuDisplay


class ViewGeneric:
    def __init__(self):
        self.checker = ViewChecker()

    def confirm_element_registration(self, element, elements_list):
        print(f"{element} inscrit dans {elements_list}")

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

    def back_to_menu(self, name):
        list_of_choice = ["Y", "N"]
        print(f"Voulez-vous retourner au {name} ?")
        check = self.checker.check_string(list_choice=list_of_choice)
        if check == "Y":
            return True
        else:
            return False

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

    def confirmation(self, confirmation_text):
        self.print_center(confirmation_text)

        current_option = "yes"
        self.print_confirm(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == "yes":
                current_option = "no"
            elif key == curses.KEY_LEFT and current_option == "no":
                current_option = "yes"
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return True if current_option == "yes" else False

            self.print_confirm(current_option)

    def print_center(self, text):
        stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

