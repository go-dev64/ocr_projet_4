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

class MenuDisplay:

    def __init__(self, menu, text, title):
        """display menu et return action selected"""
        self.menu = menu
        self.title = title
        self.confirmation_text = text
        self.action_selected = int
        curses.wrapper(self.mainloop)

    def mainloop(self, stdscr):
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
                self.action_selected = current_row
                if current_row == len(self.menu) - 1:
                    if self.confirm(self.confirmation_text):
                        break
                else:
                    break
            self.print_menu(current_row)

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2
            y = self.screen_height // 2 - len(self.menu) // 2 + idx
            if idx == selected_row_idx:
                self.color_print(y, x, row, 1)
            else:
                self.stdscr.addstr(y, x, row)
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
