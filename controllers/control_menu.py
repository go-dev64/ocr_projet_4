from views.view_main_menu import ViewMainMenu
from views.view_checker import ViewChecker


class ControlMenu:
    def __init__(self, create_tournament, control_tournament, player):
        self.view_main_menu = ViewMainMenu()
        self.checker = ViewChecker()
        self.create_tournament = create_tournament
        self.control_tournament = control_tournament
        self.player = player

    def action_selected_in_main_menu(self):
        list_of_action = ["Nouveau Tournoi", "Reprendre un Tournoi", "Menu Joueur", "Arrêter le programme"]
        self.view_main_menu.view_menu(list_of_choice=list_of_action)
        user_action = self.checker.check_num_choice(list_choice=list_of_action)
        return user_action

    def control(self):
        choice = self.action_selected_in_main_menu()
        match choice:
            case 1:
                tournament = self.create_tournament.create_new_tournament()
                choice = self.create_tournament.launch_new_tournament(
                    new_tournament=tournament
                )
                if choice == 1:
                    self.control_tournament.play_tournament(
                        tournament=tournament
                    )
                else:
                    self.control()
            case 2:
                tournament = self.control_tournament.select_tournament()
                self.control_tournament.play_tournament(
                    tournament=tournament
                )
                self.control()
            case 3:
                pass
            case 4:
                print("Arrêt du programme")
