

class ViewMainMenu:
    def __init__(self):
        pass

    def view_menu(self, list):
        print("Gestionnaire de tournoi")
        n = 0
        for element in list:
            n += 1
            print(f"{n} - {element}")

