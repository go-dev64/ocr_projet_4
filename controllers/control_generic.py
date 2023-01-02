from views.view_checker import ViewChecker
from views.view_generic import ViewGeneric
import curses


class Generic:
    def __init__(self):
        self.checker = ViewChecker()
        self.view_generic = ViewGeneric()

    def action_selected_in_menu_by_user(self, actions_list, name_of_menu):
        """return index of action selected in actions list"""
        list_of_action = actions_list
        user_choice = self.view_generic.view_menu(
            list_of_choice=list_of_action, name_of_menu=name_of_menu
        )
        return user_choice

    def select_element_in_list(self, list_of_elements, type_of_element, sort_by=None):
        index_element_selected = self.view_generic.user_select_element(
            list_of_elements=list_of_elements,
            type_of_element=type_of_element,
            sort_by=sort_by,
        )
        element_selected = list_of_elements[index_element_selected]
        return element_selected

    def convert_objects_list_in_string_list(self, object_list, ):
        str_list = []
        for element in object_list:
            string = element.__str__()
            str_list.append(string)
        return str_list

    def add_exit(self, elements_list):
        elements_list.append("Retour au Menu Précédent")

    def select_of_element_in_list(self, element_list, text, title):
        """
    user select element in list elements
        :param element_list:
        :param text: confirm back to menu
        :param title: title of menu or action to do (ex: select a player)
        :return: index of element selected
        """
        liste = element_list
        list_elements = self.convert_objects_list_in_string_list(liste)
        self.add_exit(elements_list=list_elements)
        the_element = MenuDisplay(
            element=list_elements,
            text=text,
            title=title
        )
        the_element.launch_menu_selector()
        return the_element.selected

    def display_list(self, list_of_elements, title):
        """
        display element of list
        :param list_of_elements:
        :param title:
        :return:
        """
        #elements_list = self.convert_objects_list_in_string_list(object_list=list_of_elements)
        MenuDisplay(
            element=list_of_elements,
            title=title
        ).launch_display_list()


class MenuDisplay:

    def __init__(self, element, title, text=None):
        """display menu et return action selected"""
        self.menu = element
        self.title = title
        self.confirmation_text = text
        self.selected = int

    def launch_menu_selector(self):
        curses.wrapper(self.menu_selector)

    def launch_display_list(self):
        curses.wrapper(self.display_list)

    def lauch_input_user(self):
        curses.wrapper(self.input_user)

    def input_user(self):
        baba = "quel est votre nom"
        width = self.screen_width // 2
        height = self.screen_height // 2
        self.stdscr.clear()
        self.stdscr.addstr(width, height, baba)
        self.input_user = self.stdscr.getstr(y=width + 1 + len(baba), x=height)
        self.stdscr.getch()

    def menu_selector(self, stdscr):
        """turn off cursor blinking"""
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.stdscr = stdscr
        """get size of screen"""
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        """specify the current selected row"""
        current_row = 0
        self.print_menu(current_row)
        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self.selected = current_row
                if current_row == len(self.menu) - 1:
                    if self.confirm(self.confirmation_text):
                        break
                else:
                    break
            self.print_menu(current_row)

    def middle_screen_width(self, text):
        middle_width = self.screen_width // 2 - len(text) // 2
        return middle_width

    def middle_screen_height(self, element):
        middle_height = self.screen_height // 2 - len(element) // 2
        return middle_height

    def print_title_application(self):
        title = "  Gestionnaire de Tournoi d'Echec  "
        self.stdscr.border()
        self.stdscr.addstr(0, self.middle_screen_width(text=title), title)

    def print_name_of_menu(self):
        middle_screen_width_title = self.middle_screen_width(text=self.title)
        height_position = self.screen_height // 2 - len(self.menu) // 2 - 5
        self.stdscr.addstr(height_position, middle_screen_width_title, self.title)

    def print_guideline(self, text_guideline):
        middle_screen_width = self.middle_screen_width(text=text_guideline)
        down_screen = self.screen_height - 2
        self.stdscr.addstr(down_screen, middle_screen_width, text_guideline)

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        self.print_title_application()
        self.print_name_of_menu()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row.__str__()) // 2
            y = self.screen_height // 2 - len(self.menu) // 2 + idx
            if idx == selected_row_idx:
                self.color_print(y, x, row.__str__(), 1)
            else:
                self.stdscr.addstr(y, x, row.__str__())
        self.print_guideline(
            text_guideline="Utiliser les fléches pour vous déplacer / Appuyer sur Entrée pour valider"
        )
        self.stdscr.refresh()

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def print_confirm(self, selected="Oui"):
        # clear yes/no line
        curses.setsyx(self.screen_height // 2 + 1, 0)
        self.stdscr.clrtoeol()

        y = self.screen_height // 2 + 1
        options_width = 10

        # print yes
        option = "Oui"
        x = self.screen_width // 2 - options_width // 2 + len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print no
        option = "Non"
        x = self.screen_width // 2 + options_width // 2 - len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()

    def confirm(self, confirmation_text):
        self.print_center(confirmation_text)

        current_option = "Oui"
        self.print_confirm(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == "Oui":
                current_option = "Non"
            elif key == curses.KEY_LEFT and current_option == "Non":
                current_option = "Oui"
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return True if current_option == "Oui" else False

            self.print_confirm(current_option)

    def print_center(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

    def display_list(self, stdscr):
        """turn off cursor blinking"""
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.stdscr = stdscr
        """get size of screen"""
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        self.print_list()
        self.stdscr.getch()

    def print_list(self):
        self.stdscr.clear()
        self.print_title_application()
        self.print_name_of_menu()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row.__str__()) // 2
            y = self.screen_height // 2 - len(self.menu) // 2 + idx
            self.stdscr.addstr(y, x, f"{idx + 1} - {row.__str__()}")
        self.print_guideline(text_guideline="Appuyer sur une touche pour revenir au Menu Précédent")
        self.stdscr.refresh()
