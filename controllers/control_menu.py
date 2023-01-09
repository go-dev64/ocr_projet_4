from views.display_menu import MenuDisplay
from views.option_selection import Confirmation


class ControlMenu:
    def __init__(self, create_tournament, control_tournament, player):

        #self.generic = Generic()
        self.create_tournament = create_tournament
        self.control_tournament = control_tournament
        self.control_player = player

    def main_menu(self):
        list_of_action = ["Menu Tournoi", "Menu Joueur", "Arrêter le programme"]
        while True:
            action_main_menu = MenuDisplay(
                elements_list=list_of_action,
                confirm_text="Voulez-vous arrêter le programme?",
                title="Menu Principal"
            )
            action_main_menu.menu_selector()
            if action_main_menu.index_selected == 0:
                self.tournament_menu()
            elif action_main_menu.index_selected == 1:
                self.menu_player()
            else:
                choice = Confirmation(text="Voulez-vous arrêter le programme?").select_option()
                if choice:
                    break

    def tournament_menu(self):
        while True:
            list_of_action = ["Nouveau Tournoi",
                              "Reprendre un Tournoi",
                              "Afficher tous les Tournois",
                              "Afficher tous les Rounds d'un Tournoi",
                              "Afficher tous les Matchs d'un Round"
                              ]
            action_main_menu = MenuDisplay(
                elements_list=list_of_action,
                confirm_text="Voulez-vous retourner au Menu Principal?",
                title="Menu Tournoi"
            )
            action_main_menu.menu_selector()
            index_action_selected_of_menu = action_main_menu.index_selected

            if index_action_selected_of_menu == 0:
                "new tournament"
                tournament = self.create_tournament.create_new_tournament()
                choice = self.create_tournament.launch_new_tournament(
                    new_tournament=tournament
                )
                if choice == "Y":
                    self.control_tournament.play_tournament(tournament=tournament)
                else:
                    continue

            elif index_action_selected_of_menu == 1:
                "reload in progress tournament"
                tournament = self.control_tournament.select_tournament()
                self.control_tournament.play_tournament(tournament=tournament)
                if self.generic.view_generic.back_to_menu(name="Menu Principal"):
                    break
                else:
                    continue

            elif index_action_selected_of_menu == 2:
                "display all tournaments"
                self.generic.display_list(
                    list_of_elements=self.control_tournament.data_tournaments_list,
                    title="Liste des tournois"
                )

            elif index_action_selected_of_menu == 3:
                "display all rounds of tournament"
                tournament_list = self.control_tournament.data_tournaments_list
                index_tournament_selected = self.generic.select_of_element_in_list(
                    element_list=tournament_list,
                    title="Sélectionner un Tournoi",
                    text="Retour au Menu precedent"
                )
                if index_tournament_selected < len(tournament_list):
                    tournament_selected = tournament_list[index_tournament_selected]
                    self.generic.display_list(
                        list_of_elements=tournament_selected.round_list,
                        title=f"Liste des rounds du {tournament_selected}"
                    )

            elif index_action_selected_of_menu == 4:
                "display all matchs of round of tournament"
                tournament_list = self.control_tournament.data_tournaments_list
                index_tournament_selected = self.generic.select_of_element_in_list(
                    element_list=tournament_list,
                    title="Sélectionner un Tournoi",
                    text="Retour au Menu precedent"
                )
                if index_tournament_selected < len(tournament_list):
                    tournament_selected = tournament_list[index_tournament_selected]
                    index_round_selected = self.generic.select_of_element_in_list(
                        element_list=tournament_selected.round_list,
                        title=f"Sélectionner un Round du {tournament_selected}",
                        text="Retour au Menu precedent"
                    )
                    if index_round_selected < len(tournament_selected.round_list):
                        round_selected = tournament_selected.round_list[index_round_selected]
                        self.generic.display_list(
                            list_of_elements=round_selected.list_of_match,
                            title=f"Liste des matchs du {round_selected.name} du {tournament_selected}"
                        )

            else:
                break

    def menu_player(self):
        while True:
            list_of_action = [
                "Afficher la liste de tous joueurs de la base de donnée",
                "Afficher la liste de tous joueurs d'un tournoi",
                "Enregistrer un nouveau joueur",
                "Modifier le classement d'un joueur",
            ]
            action_main_menu = MenuDisplay(
                elements_list=list_of_action,
                confirm_text="Voulez-vous retourner au Menu Principal?",
                title="Menu Joueur"
            )
            action_main_menu.menu_selector()
            index_action_selected = action_main_menu.index_selected

            if index_action_selected == 0:
                "display all players by rang or by name"
                self.control_tournament.control_player.display_players_list(
                    players_list=self.control_player.data_players_list)

            elif index_action_selected == 1:
                "Display all players of tournament"
                tournament_list = self.control_tournament.data_tournaments_list
                action_main_menu = MenuDisplay(
                    elements_list=list_of_action,
                    confirm_text="Voulez-vous retourner au Menu Précédent?",
                    title="Menu Joueur / Sélectionner un tournoi"
                )
                action_main_menu.menu_selector()
                index_tournament_selected = action_main_menu.index_selected
                if index_tournament_selected < len(tournament_list):
                    tournament_selected = tournament_list[index_tournament_selected]

                    players_list = MenuDisplay(
                        elements_list=list_of_action,
                        confirm_text="Voulez-vous retourner au Menu Précédent?",
                        title=f"Liste des joueur du {tournament_selected}"
                    )
                    players_list.display_list()

            elif index_action_selected == 2:
                "add new player"
                self.control_player.add_new_player_by_user(
                    name_of_list="la base de donnée"
                )

            elif index_action_selected == 3:
                "change rang of player"
                players_list_sorted = sorted(
                    self.control_player.data_players_list, key=lambda player: player.name
                )
                action_main_menu = MenuDisplay(
                    elements_list=players_list_sorted,
                    confirm_text="Voulez-vous retourner au Menu Précédent?",
                    title="Menu Joueur / Sélectionner un Joueur "
                )
                action_main_menu.menu_selector()
                index_players_list = action_main_menu.index_selected
                if index_players_list < len(players_list_sorted):
                    self.control_player.change_rang_of_player(
                        player_selected=players_list_sorted[index_players_list])
            else:
                break
