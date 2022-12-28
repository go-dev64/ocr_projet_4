from controllers.control_generic import Generic , MenuDisplay


class ControlMenu:
    def __init__(self, create_tournament, control_tournament, player):

        self.generic = Generic()
        self.create_tournament = create_tournament
        self.control_tournament = control_tournament
        self.control_player = player

    def main_menu(self):
        list_of_action = ["Menu Tournoi", "Menu Joueur", "Arrêter le programme"]
        while True:
            choice = MenuDisplay(menu=list_of_action,
                                 text="Voulez-vous arrêter le programme?",
                                 title="Menu Principal"
                                 ).action_selected
            if choice == 0:
                self.tournament_menu()
            elif choice == 1:
                self.menu_player()
            else:
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
            choice = MenuDisplay(menu=list_of_action,
                                 text="Voulez-vous retourner au Menu Principal?",
                                 title="Menu Tournoi"
                                 ).action_selected

            if choice == 0:
                tournament = self.create_tournament.create_new_tournament()
                choice = self.create_tournament.launch_new_tournament(
                    new_tournament=tournament
                )
                if choice == "Y":
                    self.control_tournament.play_tournament(tournament=tournament)
                else:
                    continue
            elif choice == 1:
                tournament = self.control_tournament.select_tournament()
                self.control_tournament.play_tournament(tournament=tournament)
                if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                    break
                else:
                    continue
            elif choice == 2:
                self.generic.view_generic.display_elements_of_list(
                    elements_list=self.control_tournament.data_tournaments_list,
                )
                if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                    break
                else:
                    continue
            elif choice == 3:
                self.control_tournament.display_round_of_tournament()
                if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                    break
                else:
                    continue
            elif choice == 4:
                self.control_tournament.display_match_of_round()
                if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                    break
                else:
                    continue
            else:
                break

    def menu_player(self):
        while True:
            list_of_action = [
                "Afficher la liste de tous joueurs de la base de donnée",
                "Afficher la liste de tous joueurs d'un tournoi",
                "Enregistrer un nouveau joueur",
                "Modifier le classement d'un joueur",
                "Retour Menu Principal",
            ]
            action_selected = MenuDisplay(
                menu=list_of_action,
                text="Voulez-vous retourner au Menu Principal?",
                title="Menu Joueur"
            ).action_selected
            if action_selected == 0:
                self.control_player.display_players_list(
                    players_list=self.control_player.data_players_list,
                    name_of_menu="Menu Joueur / Liste des Joueur dans la base de données",
                )
            elif action_selected == 1:
                tournament = self.generic.select_element_in_list(
                    list_of_elements=self.control_tournament.data_tournaments_list,
                    type_of_element="tournoi"
                )
                self.control_player.display_players_list(
                    players_list=tournament.players_list,
                    name_of_menu=f"Menu Joueur / Liste des Joueur du {tournament}",
                )
            elif action_selected == 2:
                self.control_player.add_new_player_by_user(
                    name_of_list="la base de donnée"
                )

            elif action_selected == 3:
                self.control_player.change_rang_of_player()
            else:
                break
