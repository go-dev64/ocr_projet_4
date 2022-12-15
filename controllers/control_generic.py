from views.view_checker import ViewChecker
from views.view_generic import ViewGeneric


class Generic:
    def __init__(self):
        self.checker = ViewChecker()
        self.view_generic = ViewGeneric()

    def action_selected_in_menu_by_user(self, actions_list, name_of_menu):
        """return index of action selected in actions list"""
        list_of_action = actions_list
        user_choice = self.view_generic.view_menu(
            list_of_choice=list_of_action, name_of_menu=name_of_menu
        )
        return user_choice

    def select_element_in_list(self, list_of_elements, type_of_element, sort_by):
        index_element_selected = self.view_generic.user_select_element(
            list_of_elements=list_of_elements,
            type_of_element=type_of_element,
            sort_by=sort_by,
        )
        element_selected = list_of_elements[index_element_selected]
        return element_selected
