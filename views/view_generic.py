from views.view_checker import ViewChecker


class ViewGeneric:
    def __init__(self):
        self.checker = ViewChecker()

    def confirm_element_registration(self, element, elements_list):
        print(f"{element} inscrit dans {elements_list}")

    def user_select_element(self, list_of_elements, type_of_element):
        list_of_elements = list_of_elements
        print(f"Sélectionner un {type_of_element}:")
        choice_element = 0
        for element in list_of_elements:
            choice_element += 1
            print(f"{choice_element} - {element}")
        check = self.checker.check_num_choice(
            list_choice=list_of_elements
        )
        element_selected = check - 1
        print(f"Vous avez sélectionner:\n"
              f"{list_of_elements[element_selected]}")
        return element_selected

    def view_menu(self, list_of_choice, name_of_menu):
        print(f"{name_of_menu}")
        n = 0
        for element in list_of_choice:
            n += 1
            print(f"{n} - {element}")
        user_choice = self.checker.check_num_choice(
            list_choice=list_of_choice
        )
        return user_choice

    def back_to_menu(self, name):
        list_of_choice = ["Y", "N"]
        print(f"Voulez-vous retourner au {name} ?")
        check = self.checker.check_string(
            list_choice=list_of_choice
        )
        if check == "Y":
            return True
        else:
            return False

    def display_elements_of_list(self, elements_list):
        compteur = 0
        for element in elements_list:
            compteur += 1
            print(f"{compteur} - {element}")

