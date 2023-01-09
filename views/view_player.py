from views.view_checker import ViewChecker
from views.screen import Screen
from views.input import GetInfo


class ViewPlayer:
    def __init__(self):
        self.checker = ViewChecker()

    @staticmethod
    def display_player_rang(player_name, player_rang):
        print(
            f"{player_name} est actuellement au rang " f"N°{player_rang} du classement."
        )

    def change_player_rang(self, player, player_list):
        new_rang = GetInfo(pos_x=30, pos_y=5).get_new_rang_player(
            player=player,
            list_player=player_list
        )
        return new_rang


        new_rang = None
        list_of_choice = ["Y", "N"]
        self.display_player_rang(player_name=player.name, player_rang=player.rang)
        print(f"Vous modifier le rang du joueur: " f"{player.name}")
        check = self.checker.check_string(list_choice=list_of_choice)
        if check == "Y":
            result_ok = 0
            while result_ok != 1:
                try:
                    rang = int(
                        input(
                            f"Entrer le nouveau rang au classement"
                            f" de {player.name}:"
                        )
                    )
                except ValueError:
                    print("Oooops, Entrer Invalide. Entrer un Nombre!")
                else:
                    result_ok += 1
                    new_rang = rang
            print(f"\nNouveau Rang de {player.name}: {new_rang}")
            return new_rang

        else:
            return None

    @staticmethod
    def input_player_rang():
        print("Renseigner le classement du Joueur:\n")
        result_ok = 0
        while result_ok != 1:
            try:
                rang = int(input("Entrer le rang au classement"))
            except ValueError:
                print("Oooops, Entrer Invalide. Entrer un Nombre!")
            else:
                result_ok += 1
                return rang

    @staticmethod
    def player_already_selected(player, list_where_player_exist):
        Screen().message(
            message=f"Le joueur {player} est deja inscrit dans {list_where_player_exist}!",
            title=" Message Erreur ! "
        )

    def valid_player_exist(self):

        print("Joueur deja existant dans la base de données.\n")
        list_of_action = [
            "Sélectionner le joueur existant",
            "Recommencer la saisie",
        ]
        print("Voulez-vous:")
        choice = 0
        for action in list_of_action:
            choice += 1
            print(f"{choice}: {action}")
        check = self.checker.check_num_choice(list_choice=list_of_action)
        action_selected = check - 1
        return action_selected
