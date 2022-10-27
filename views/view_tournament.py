class ViewTournament:


    def user_choice_of_name_of_tournament(self):
        name = input("Nom du tournoi:")
        print("Nom du tournoi: " + name)
        return name


    def user_choice_of_place_of_tournament(self):
        place = input("Renseigner le lieu du Tournoi:")
        return place


    def user_choice_of_date_of_tournament(self):
        print("Entrer la date  du Tournoi:")
        date = input("Date du tournoi:")
        return date


    def user_choice_of_control_time(self):
        control_time = input(" Sélectionner le type Controle de temps:"
                             "1 - Bullet"
                             "2 - Blitz"
                             "3 - Coup Rapide")
        match control_time:
            case 1:
                return "Bullet"
            case 2:
                return "Blitz"
            case 3:
                return "Coup rapide"

    def user_choice_of_description_of_tournament(self):
        descritption = input("Entrer une description du tournoi")
        return descritption

    def user_choice_of_player(self):
        print("Choix des joueurs:"
              "1 - Entrer un nouveau joueur"
              "2 - Sélectionner un joueur existant"
              )
        choice_of_player = input("Entrer votre choix")




