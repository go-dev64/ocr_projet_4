from controllers.control_generic import Generic


class ControlMenu:
    def __init__(self, create_tournament, control_tournament, player):
        self.generic = Generic()
        self.create_tournament = create_tournament
        self.control_tournament = control_tournament
        self.control_player = player

    def main_menu(self):
        list_of_action = ["Menu Tournoi", "Menu Joueur", "Arrêter le programme"]
        while True:
            choice = self.generic.action_selected_in_menu_by_user(
                actions_list=list_of_action,
                name_of_menu="Menu Principal"
            )
            match choice:
                case 1:
                    self.control_tournament.tournament_menu()
                case 2:
                    self.control_player.menu_player()
                case 3:
                    print("Arrêt du programme")
                    break
