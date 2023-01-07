import curses
from datetime import datetime
from option_selection import OptionSelection
from screen import Screen
from window import Window


class GetInfo(Screen):
    def __init__(self, key_information, pos_x, pos_y):
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.offset_x = 20
        self.key_information = key_information
        self.value_info = {}

    def color_print(self, y, x, text, pair_num):
        """
        give a color to lines
        :param y: pos y
        :param x: pos x
        :param text: text to display
        :param pair_num: type of color
        :return:
        """
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))

    def get_input(self, info, pos_y):
        """
        displays the information to be given
        :param info: type information to be given
        :param pos_y:  y position in screen
        :return: input user
        """
        curses.curs_set(1)
        x = self.middle_width_screen
        self.stdscr.addstr(pos_y, x - self.offset_x, info)
        info_done = self.stdscr.getstr(pos_y, x - self.offset_x + len(info) + 2, 50).decode("utf-8")
        return info_done

    def valid_string(self, info, pos_y):
        """
        check if len(str) > 0 else return AsserError
        :param info: display type of info to given (name, first_name,etc)
        :param pos_y: position y of display champ
        :return: string input user
        """
        while True:
            self.display_title()
            the_input = self.get_input(info=info, pos_y=pos_y)
            try:
                assert len(the_input) > 0
            except AssertionError:
                title = " Erreur de saisie "
                error_message = "Champ vide!"
                y = pos_y + 3
                x = 10
                self.window_error(window_pos_y=y,
                                  window_pos_x=x,
                                  title=title,
                                  error_message=error_message
                                  )
            else:
                return the_input

    def valid_date(self, type_of_date, pos_y,):
        """
        valid if date have the right format
        :param type_of_date: display type of date (date of creation or date of birth for exempl)
        :param pos_y: y position in screen
        :return: date in right format
        """
        while True:
            self.display_title()

            input_date = self.get_input(info=type_of_date, pos_y=pos_y)
            try:
                if input_date != datetime.strptime(input_date, "%d-%m-%Y").strftime("%d-%m-%Y"):
                    raise ValueError
            except ValueError:
                title = " Erreur Format date "
                error_message = "Format Date Invalide! Format: JJ-MM-AAAA"
                y = pos_y + 3
                x = 10
                self.window_error(window_pos_y=y,
                                  window_pos_x=x,
                                  title=title,
                                  error_message=error_message
                                  )
                self.clear_lines(pos_y=pos_y)
            else:
                return input_date

    def vali_number(self, info, pos_y, element_list):
        self.display_title()
        input_number = self.get_input(info=info, pos_y=pos_y)

        try:
            the_input = int(input_number)
            assert 1 <= the_input < len(element_list) + 1
        except ValueError:
            title = " Erreur Format Saissie "
            error_message = "Format Invalide! Entrer un numéro"
            y = pos_y + 3
            x = 10
            self.window_error(window_pos_y=y,
                              window_pos_x=x,
                              title=title,
                              error_message=error_message
                              )
            self.clear_lines(pos_y=pos_y)
        except AssertionError:
            title = " Erreur Format Saissie "
            error_message = "Numéro Invalide! Entrer un numéro valide"
            y = pos_y + 3
            x = self.screen_width - 20
            self.window_error(window_pos_y=y,
                              window_pos_x=x,
                              title=title,
                              error_message=error_message
                              )
            self.clear_lines(pos_y=pos_y)
        else:
            return the_input

    def window_error(self, window_pos_y, window_pos_x, title, error_message):
        win = Window(window_title=title,
                     pos_y=window_pos_y, pos_x=window_pos_x,
                     number_lines=10,
                     number_columns=self.screen_width - 20
                     )
        win.display_error_message(y=5, error_message=error_message)
        self.stdscr.border()

    def get_info_player(self, title, ):
        """
        get name , first name, date of birth and sex of new player
        :param title:  string that will be displayed
        :return: dictionary of info player
        """
        player_info = {}
        self.stdscr.addstr(self.y + 2, self.middle_width_screen - len(title) // 2, title)
        self.stdscr.nodelay(True)
        self.stdscr.getch()
        self.stdscr.nodelay(False)
        player_info["name"] = self.valid_string(info=self.key_information[0], pos_y=self.y + 4)
        player_info["first_name"] = self.valid_string(info=self.key_information[1], pos_y=self.y + 6)
        player_info["date_of_birth"] = self.valid_date(
            type_of_date="Date de naissance (au format: JJ-MM-AAAA):",
            pos_y=self.y + 8)
        gender_choice = OptionSelection(text=self.key_information[3],
                                        pos_y=self.y + 10,
                                        pos_x=self.middle_width_screen - 20,
                                        list_of_choice=["Femme", "Homme"])
        player_info["gender"] = gender_choice.option_selected
        self.stdscr.refresh()
        return player_info
