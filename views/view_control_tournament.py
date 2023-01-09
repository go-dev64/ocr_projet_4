from views.view_checker import ViewChecker
from views.view_generic import ViewGeneric


class ViewControlTournament:
    def __init__(self):
        self.checker = ViewChecker()
        self.view_generic = ViewGeneric()

    def view_select_tournament(self, tournament_list):
        print("Sélection du tournoi")
        number = 0
        for tournament in tournament_list:
            number += 1
            print(f"{number} - {tournament}")
        check = self.checker.check_num_choice(list_choice=tournament_list)
        tournament_selected = check - 1
        print(
            f"Vous avez sélectionner le tournoi:\n"
            f"{tournament_list[tournament_selected]}"
        )
        return tournament_list[tournament_selected]

    def view_end_tournament(self, tournament):
        self.view_generic.display_element_list(
            elements_list=tournament.players_list,
            confirmation_text="retour au menu principal!",
            title=f"Le {tournament} est terminé!\n" "Résultat du tournoi:")

    def view_create_new_round(self, name_of_round):
        choice = self.view_generic.confirm_choice(
            message=f"voulez-vous génerer le {name_of_round} ?",
            title=" Création nouveau Round "
        )
        if choice is True:
            self.view_generic.confirm_element_registration(
                message=f"Création du {name_of_round}",
                title=" Création nouveau Round "
            )
            return True
        else:
            return None
