class ViewTournament:


    def user_choice_of_name_of_tournament(self):
        print("Entrer le nom du tournoi: ")
        name = input("Nom du tournoi:")
        return name

    def user_choice_of_place_of_tournament(self):
        print("Renseigner le lieu du tournoi")
        place = input("lieu du Tournoi:")
        return place

    def user_choice_of_date_of_tournament(self):
        print("Entrer la date  du Tournoi:")
        date = input("Date du tournoi:")
        return date

    def user_choice_of_control_time(self):
        print(" Sélectionner le type Controle de temps:\n"
              "1 - Bullet\n"
              "2 - Blitz\n"
              "3 - Coup Rapide\n")
        control_time = input("Entrer votre choix:")
        match control_time:
            case 1:
                return "Bullet"
            case 2:
                return "Blitz"
            case 3:
                return "Coup rapide"

    def user_choice_of_description_of_tournament(self):
        print("Renseigner une description du tournoi:")
        descritption = input("Description: ")
        return descritption

    def user_choice_of_player(self):
        print("Choix des joueurs:\n"
              "1 - Entrer un nouveau joueur\n"
              "2 - Sélectionner un joueur existant\n"
              )
        choice_of_player = input("Entrer votre choix: ")
        return choice_of_player


toto = ViewTournament()
toto.user_choice_of_player()
toto.user_choice_of_description_of_tournament()
toto.user_choice_of_date_of_tournament()
toto.user_choice_of_name_of_tournament()
toto.user_choice_of_place_of_tournament()
toto.user_choice_of_control_time()


