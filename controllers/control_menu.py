from controllers.control_generic import Generic


class ControlMenu:
    def __init__(self, create_tournament, control_tournament, player):

        self.generic = Generic()
        self.create_tournament = create_tournament
        self.control_tournament = control_tournament
        self.control_player = player

    def main_menu(self):
        list_of_action = ["Menu Tournoi", "Menu Joueur", "Arreter le programme"]
        while True:
            choice = self.generic.action_selected_in_menu_by_user(
                actions_list=list_of_action, name_of_menu="Menu Principal"
            )
            match choice:
                case 1:
                    self.tournament_menu()
                case 2:
                    self.menu_player()
                case 3:
                    print("Arrêt du programme")
                    break

    def tournament_menu(self):
        while True:
            list_of_action = [
                "Nouveau Tournoi",
                "Reprendre un Tournoi",
                "Afficher tous les Tournois",
                "Afficher tous les Rounds d'un Tournoi",
                "Afficher tous les Matchs d'un Round",
                "Retour au Menu Principal",
            ]
            choice = self.generic.action_selected_in_menu_by_user(
                actions_list=list_of_action, name_of_menu="Menu Tournoi"
            )

            match choice:
                case 1:
                    tournament = self.create_tournament.create_new_tournament()
                    choice = self.create_tournament.launch_new_tournament(
                        new_tournament=tournament
                    )
                    if choice == "Y":
                        self.control_tournament.play_tournament(tournament=tournament)
                    else:
                        continue
                case 2:
                    tournament = self.control_tournament.select_tournament()
                    self.control_tournament.play_tournament(tournament=tournament)
                    if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                        break
                    else:
                        continue
                case 3:
                    self.generic.view_generic.display_elements_of_list(
                        elements_list=self.control_tournament.data_tournaments_list,
                    )
                    if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                        break
                    else:
                        continue
                case 4:
                    self.control_tournament.display_round_of_tournament()
                    if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                        break
                    else:
                        continue
                case 5:
                    self.control_tournament.display_match_of_round()
                    if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                        break
                    else:
                        continue
                case 6:
                    break

    def menu_player(self):
        choice = 0
        while choice != 1:
            list_of_action = [
                "Afficher la liste de tous joueurs de la base de donnée",
                "Afficher la liste de tous joueurs d'un tournoi",
                "Enregistrer un nouveau joueur",
                "Modifier le classement d'un joueur",
                "Retour Menu Principal",
            ]
            action_selected = self.generic.action_selected_in_menu_by_user(
                actions_list=list_of_action, name_of_menu="Menu Joueur"
            )
            match action_selected:
                case 1:
                    self.control_player.display_players_list(
                        players_list=self.control_player.data_players_list,
                        name_of_menu="Menu Joueur / Liste des Joueur dans la base de données",
                    )
                case 2:
                    tournament = self.generic.select_element_in_list(
                        list_of_elements=self.control_tournament.data_tournaments_list,
                        type_of_element="tournoi"
                    )
                    self.control_player.display_players_list(
                        players_list=tournament.players_list,
                        name_of_menu=f"Menu Joueur / Liste des Joueur du {tournament}",
                    )
                case 3:
                    self.control_player.add_new_player_by_user(
                        name_of_list="la base de donnée"
                    )

                case 4:
                    self.control_player.change_rang_of_player()
                case 5:
                    break
