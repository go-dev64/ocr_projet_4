from views.view_checker import ViewChecker
from views.view_generic import ViewGeneric


class ViewRound:
    def __init__(self):
        self.checker = ViewChecker()
        self.view_generic = ViewGeneric()

    def display_match(self, match_list, round):
        self.view_generic.display_element_list(
            elements_list=match_list,
            title=f"Voici la liste des matchs du prochain Round: Le {round}",
            confirmation_text=None
        )

    def select_match(self, match_list, round):
        index_match_selected = self.view_generic.user_select_element_in_list(
            elements_list=match_list,
            confirmation_text=" Voulez-vous revenir au menu precedent?",
            title=f"Sélectionner un match du {round.name}:"
        )
        self.view_generic.confirm_element_registration(
            message=f"Vous avez sélectionner le match:\n" f"{match_list[index_match_selected]}",
            title=" Sélection Match"
            )
        return index_match_selected

    def confirm_play_next_match(self, round):
        choice = self.view_generic.confirm_choice(
            message=f"Voulez-vous saisir le résultat d'un match du {round.name} ?",
            title=" Entrer résultat Match"
        )
        return choice

    def view_start_of_round(self, name_of_round):
        choice = self.view_generic.confirm_choice(
            message=f"Voulez-vous commencer le {name_of_round} ?"
        )
        if choice is True:
            self.view_generic.confirm_element_registration(
                message=f"\nLe {name_of_round} est lancé!",
                title=" Lancement nouveau Round"
            )
        return choice

    def view_end_of_round(self, name_of_round, winner_players_list):
        self.view_generic.display_element_list(
            elements_list=winner_players_list,
            confirmation_text="voulez-vous retournez au menu precedent",
            title=f"Fin du {name_of_round}! les gagnats sont:"
        )
