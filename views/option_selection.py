import curses
from views.screen import Screen


class OptionSelection:
    def __init__(self, text, pos_y, pos_x,  list_of_choice):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list_of_choice = list_of_choice
        self.option_selected = str
        curses.wrapper(self.select_option)

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def print_option_beside(self, selected):
        pos_y = self.pos_y
        pos_x_end_text = self.pos_x + len(self.text)
        curses.setsyx(pos_y, 0)
        self.stdscr.clrtoeol()

        offset_x = 10
        if len(self.list_of_choice) == 2:
            option_1 = self.list_of_choice[0]
            pos_x = pos_x_end_text + offset_x // 2
            if selected == option_1:
                self.color_print(pos_y, pos_x, option_1, 1)
            else:
                self.stdscr.addstr(pos_y, pos_x, option_1)

            option_2 = self.list_of_choice[1]
            pos_x = pos_x_end_text + len(option_1) + offset_x
            if selected == option_2:
                self.color_print(pos_y, pos_x, option_2, 1)
            else:
                self.stdscr.addstr(pos_y, pos_x, option_2)

            self.stdscr.refresh()

        else:
            option_1 = self.list_of_choice[0]
            pos_x = pos_x_end_text + offset_x // 2
            if selected == option_1:
                self.color_print(pos_y, pos_x, option_1, 1)
            else:
                self.stdscr.addstr(pos_y, pos_x, option_1)

            option_2 = self.list_of_choice[1]
            pos_x = pos_x_end_text + len(option_1) + offset_x
            if selected == option_2:
                self.color_print(pos_y, pos_x, option_2, 1)
            else:
                self.stdscr.addstr(pos_y, pos_x, option_2)

            option_3 = self.list_of_choice[2]
            pos_x = pos_x_end_text + len(option_1) + offset_x + len(option_2) + offset_x
            if selected == option_3:
                self.color_print(pos_y, pos_x, option_3, 1)
            else:
                self.stdscr.addstr(pos_y, pos_x, option_3)

            self.stdscr.refresh()

    def select_option(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        """get size of screen"""
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()

        self.print_text()
        current_option = self.list_of_choice[0]
        self.print_option_beside(current_option)
        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == self.list_of_choice[0]:
                current_option = self.list_of_choice[1]

            elif key == curses.KEY_RIGHT and current_option == self.list_of_choice[1]:
                current_option = self.list_of_choice[2]

            elif key == curses.KEY_LEFT and current_option == self.list_of_choice[1]:
                current_option = self.list_of_choice[0]

            elif key == curses.KEY_LEFT and current_option == self.list_of_choice[2]:
                current_option = self.list_of_choice[1]

            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_option == self.list_of_choice[0]:
                    self.option_selected = self.list_of_choice[0]
                    break
                elif current_option == self.list_of_choice[1]:
                    self.option_selected = self.list_of_choice[1]
                    break
                else:
                    self.option_selected = self.list_of_choice[2]
                    break
            self.print_option_beside(current_option)

    def print_text(self):
        x = self.pos_x
        y = self.pos_y
        self.stdscr.addstr(y, x, self.text)
        self.stdscr.refresh()


class Confirmation(Screen):
    def __init__(self, text, title=None):
        super().__init__()
        self.text = text
        self.title = title
        self.list_of_choice = ["Oui", "Non"]

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def print_option_below(self, selected):
        pos_y = self.middle_height_screen + 1
        curses.setsyx(pos_y, 0)
        self.stdscr.clrtoeol()

        offset_x = 10

        option_1 = self.list_of_choice[0]
        pos_x = self.middle_width_screen - len(option_1) - offset_x // 2
        if selected == option_1:

            self.color_print(pos_y, pos_x, option_1, 1)
        else:
            self.stdscr.addstr(pos_y, pos_x, option_1)

        option_2 = self.list_of_choice[1]
        pos_x = self.middle_width_screen + offset_x // 2
        if selected == option_2:
            self.color_print(pos_y, pos_x, option_2, 1)
        else:
            self.stdscr.addstr(pos_y, pos_x, option_2)

        self.stdscr.refresh()

    def select_option(self):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.print_text_center()
        current_option = self.list_of_choice[0]
        self.print_option_below(current_option)
        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == self.list_of_choice[0]:
                current_option = self.list_of_choice[1]
            elif key == curses.KEY_LEFT and current_option == self.list_of_choice[1]:
                current_option = self.list_of_choice[0]
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_option == self.list_of_choice[0]:
                    self.close_screen()
                    return True

                else:
                    self.close_screen()
                    return False

            self.print_option_below(current_option)

    def print_text_center(self):
        x = self.middle_width_screen - len(self.text) // 2
        y = self.middle_height_screen
        self.stdscr.addstr(y, x, self.text)
        if self.title is not None:
            self.stdscr.addstr(y - 2, self.middle_width_screen - len(self.title) // 2, self.title)
        self.stdscr.refresh()
