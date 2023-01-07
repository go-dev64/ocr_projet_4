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
        self.stdscr.addstr(self.screen_height - 1, self.middle_width_screen - len(comment) // 2, comment)
        self.stdscr.refresh()

    def clear_lines(self, pos_y):
        self.stdscr.move(pos_y , 1)
        self.stdscr.clrtobot()
        self.stdscr.border()
        self.stdscr.refresh()

    def close_screen(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()


class MyScreen:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        stdscr = self.init_screen()
        self.function(*args)
        self.close_screen(stdscr)


    def init_screen(self):
        title = "  Gestionnaire de Tournoi d'Echec  "
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(True)
        curses.curs_set(1)
        stdscr.clear()
        stdscr.border()
        curses.echo()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.screen_height, self.screen_width = stdscr.getmaxyx()
        stdscr.addstr(0, screen_width // 2 - len(title) // 2, title)
        stdscr.refresh()
        return stdscr

    def display_title(self):
        self.stdscr.addstr(0, screen_width // 2 - len(title) // 2, title)
        stdscr.refresh()

    @staticmethod
    def close_screen(stdscr):
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
