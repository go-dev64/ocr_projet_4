

class ViewMainMenu:
    def __init__(self):
        pass

    def view_menu(self, list_of_choice):
        print("Gestionnaire de tournoi")
        n = 0
        for element in list_of_choice:
            n += 1
            print(f"{n} - {element}")
