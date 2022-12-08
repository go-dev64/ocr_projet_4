from views.view_main_menu import ViewMainMenu
from views.view_checker import ViewChecker
from controllers.control_tournament import ControlTournament
from controllers.create_tournament import CreateTournament
from controllers.control_player import ControlPlayer


class ControlMenu:
    def __init__(self):
        self.view_main_menu = ViewMainMenu()
        self.checker = ViewChecker()

    def action_selected_in_main_menu(self):
        list_of_action = ["Nouveau Tournoi", "Reprendre un Tournoi", "Menu Joueur", "Arrêter le programme"]
        self.view_main_menu.view_menu(list=list_of_action)
        user_action = self.checker.check_num_choice(list_choice=list_of_action)
        return user_action

    def control(self):
        choice = ControlMenu().action_selected_in_main_menu()
        match choice:
            case 0:
                tournament = CreateTournament().create_new_tournament()
                choice = CreateTournament().launch_new_tournament(new_tournament=tournament)
                if choice == 1:
                    ControlTournament().play_tournament(tournament=tournament)
                else:
                    self.control()
            case 1:
                tournament = ControlTournament().select_tournament()
                ControlTournament().play_tournament(tournament=tournament)
                self.control()
            case 2:
                ControlPlayer()
            case 3:
                pass