class ViewMenu:
    def __init__(self):
        pass

    def view_menu(self, list_of_choice, name_of_menu):
        print(f"{name_of_menu}")
        n = 0
        for element in list_of_choice:
            n += 1
            print(f"{n} - {element}")
