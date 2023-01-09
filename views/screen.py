import curses


class Screen:
    def __init__(self):
        self.title = "  Gestionnaire de Tournoi d'Echec  "
        self.stdscr = curses.initscr()
        curses.cbreak()
        self.stdscr.keypad(True)
        curses.curs_set(1)
        self.stdscr.clear()
        self.stdscr.border()
        curses.echo()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        self.middle_width_screen = self.screen_width // 2
        self.middle_height_screen = self.screen_height // 2
        self.stdscr.addstr(0, self.middle_width_screen - len(self.title) // 2, self.title)
        self.stdscr.refresh()

    def display_title(self):
        self.stdscr.border()
        self.stdscr.addstr(0, self.middle_width_screen - len(self.title) // 2, self.title)
        self.stdscr.refresh()

    def display_comment_on_last_lines(self, comment):
        self.stdscr.addstr(
            self.screen_height - 2, self.middle_width_screen - len(comment) // 2, f"{comment.__str__()}"
        )
        self.stdscr.refresh()

    def clear_lines(self, pos_y):
        self.stdscr.move(pos_y, 1)
        self.stdscr.clrtobot()
        self.stdscr.border()
        self.stdscr.refresh()

    def close_screen(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()

    def message(self, message, title):
        comment = " Appuyer sur une touche pour continuer "
        curses.curs_set(0)
        self.stdscr.addstr(5, self.middle_width_screen - len(title) // 2, title)
        self.stdscr.addstr(self.middle_height_screen, self.middle_width_screen - len(message) // 2, message)
        self.stdscr .addstr(self.screen_height - 1, self.middle_width_screen - len(comment) // 2, comment)
        self.stdscr.refresh()
        self.stdscr.getch()
        self.close_screen()
