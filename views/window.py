import curses
from screen import MyScreen, Screen


class Window:
    def __init__(self, window_title, pos_y, pos_x, number_lines, number_columns):
        self.title = window_title
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.number_lines = number_lines
        self.number_columns = number_columns
        self.middle_width = self.number_columns // 2
        self.middle_height = self.number_columns // 2
        self.window = self.new_window(nlines=self.number_lines,
                                      ncols=self.number_columns,
                                      begin_y=self.pos_y,
                                      begin_x=self.pos_x)
        self.window.border()

    def new_window(self, nlines, ncols, begin_y, begin_x):
        new_window = curses.newwin(nlines,
                                   ncols,
                                   begin_y,
                                   begin_x
                                   )
        return new_window

    def display_title(self):
        self.window.addstr(0, self.middle_width - len(self.title) // 2, f" {self.title} ")
        self.window.refresh()

    def display_comment_on_last_lines(self, comment):
        curses.curs_set(0)
        self.window.addstr(self.number_lines - 1 , self.middle_width - len(comment) // 2, f" {comment.__str__()}")
        self.window.refresh()

    def clear_lines(self, pos_y):
        self.window.move(pos_y - 1, 1)
        self.window.clrtobot()
        self.window.border()
        self.window.refresh()

    def display_error_message(self, y, error_message):
        comment = " Appuyer sur une touche pour continuer "
        self.display_title()
        curses.curs_set(0)
        self.window.addstr(y, self.middle_width - len(error_message) // 2, error_message)
        self.window.addstr(self.number_lines - 1, self.middle_width - len(comment) // 2, comment)
        self.window.refresh()
        self.window.getch()
        self.window.erase()
        self.window.refresh()


class ErrorWindow(Window):
    def __init__(self, window_title, pos_y, pos_x, number_lines, number_columns, error_message):
        self.error_message = error_message
        super().__init__(window_title, pos_y, pos_x, number_lines, number_columns)

    def display_message(self):
        comment = " Appuyer sur une touche pour continuer "
        self.display_title()
        curses.curs_set(0)
        self.window.addstr(self.middle_height, self.middle_width - len(self.error_message) // 2, self.error_message)
        self.window.addstr(self.number_lines, self.middle_width - len(comment) // 2, comment)
        self.window.refresh()
        self.window.getch()
        self.window.erase()
        self.window.refresh()
