from views.view_checker import ViewChecker
from views.view_generic import ViewGeneric
from views.input import GetInfo
from views.display_menu import MenuDisplay


class ViewTournament:
    def __init__(self):
        self.checker = ViewChecker()
        self.view_generic = ViewGeneric()

    def get_info_tournament(self):
        info_tournament = GetInfo(pos_x=30,
                                  pos_y=5
                                  ).get_info_tournament()
        return info_tournament

    def user_choice_of_player(self):
        """define if user select old player or create new player
        args : list [
        """
        list_choice = [
            "Sélectionner un joueur dans notre base de donnée",
            "Entrer un nouveau joueur",
        ]
        index_action_selected = self.view_generic.user_select_element_in_list(
            elements_list=list_choice,
            confirmation_text="Voulez-vous revenir au menu precedent",
            title=" Inscription des joueurs au tournoi:")
        return index_action_selected

    def confirm_creation_tournament(self, tournament):
        self.view_generic.confirm_element_registration(
            message=f"Création de Tournoi: {tournament}",
            title="Menu tournoi"
        )

    def confirm_launch_new_tournament(self, tournament):
        choice = self.view_generic.confirm_choice(f"Voulez vous commencer le tournoi: {tournament} ?")
        return choice
