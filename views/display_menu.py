import curses
from views.screen import Screen
from views.option_selection import Confirmation


class MenuDisplay(Screen):
    """
    display and select element in element list on window
    """
    def __init__(self, elements_list, title, confirm_text):
        super().__init__()
        self.elements_list = elements_list
        self.title = title
        self.confirm_text = confirm_text
        self.index_selected = int
        
    def menu_selector(self):
        """
        get element selected by user in element list
        :return: index of element selected by user in elements list
        """
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        current_row = 0
        self.print_menu(current_row)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.elements_list) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self.index_selected = current_row
                break
            elif key in [27, 127]:
                choice = Confirmation(text=self.confirm_text).select_option()
                if choice:
                    break

            self.print_menu(current_row)

    def print_menu(self, selected_row_idx):
        """
            display element of elements_list
        :param selected_row_idx: current lines selected
        :return: display element
        """
        self.stdscr.refresh()
        self.stdscr.addstr(
            self.middle_height_screen - len(self.elements_list) // 2 - 3,
            self.middle_width_screen - len(self.title) // 2,
            self.title,
            curses.A_BOLD
        )
        for idx, element in enumerate(self.elements_list):
            pos_x = self.middle_width_screen - len(element.__str__()) // 2
            pos_y = self.middle_height_screen - len(self.elements_list) // 2 + idx
            if idx == selected_row_idx:
                self.color_print(pos_y, pos_x, element.__str__(), 1)
            else:
                self.stdscr.addstr(pos_y, pos_x, element.__str__())
                self.stdscr.refresh()
        self.display_comment_on_last_lines(
            comment=" Deplacement avec les fléches / Valider avec Entrer / Menu précédent avec ESC "
        )
        self.stdscr.refresh()

    def color_print(self, y, x, text, pair_num):
        """
        color the current line
        :param y: y position of line
        :param x: x position of line
        :param text: text colored
        :param pair_num: param of color
        :return: None
        """
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def display_list(self):
        """
        display self.element list
        :return: None
        """
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.display_comment_on_last_lines(
            comment="Appuyer sur une touche pour revenir au Menu Précédent "
        )
        self.print_list()
        self.stdscr.getch()

    def print_list(self):
        for idx, element in enumerate(self.elements_list):
            pos_x = self.middle_width_screen - len(element.__str__()) // 2
            pos_y = self.middle_height_screen - len(self.elements_list) // 2 + idx

            self.stdscr.addstr(pos_y, pos_x, f"{idx + 1} - {element.__str__()}")
        self.stdscr.refresh()
