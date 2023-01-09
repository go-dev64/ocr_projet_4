from views.view_checker import ViewChecker
from views.view_generic import ViewGeneric


class ViewMatch:
    def __init__(self):
        self.checker = ViewChecker()
        self.view_generic = ViewGeneric()

    def match_result(self, player_1, player_2):
        players = [f"Victoire de {player_1}", f"Victoire de {player_2}", "match nul"]
        result = self.view_generic.user_select_element_in_list(
            elements_list=players,
            title="Sélectionner le résultat du match:",
            confirmation_text="Voulez-vous revenir au menu précdent?"
        )
        if result == 0:
            self.view_generic.confirm_element_registration(
                message=f"Le vainqueur est {player_1}",
                title="Vainqueur du match:"
            )

        elif result == 1:
            self.view_generic.confirm_element_registration(
                message=f"Le vainqueur est {player_2}",
                title="Vainqueur du match:"
            )

        else:
            self.view_generic.confirm_element_registration(
                message=f"Match Nul",
                title="Vainqueur du match:"
            )

        return result
