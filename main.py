from controllers.create_tournament import CreateTournament
from controllers.control_tournament import ControlTournament
from controllers.control_player import ControlPlayer
from controllers.control_menu import ControlMenu


def main():
    menu = ControlMenu()
    choice = ControlMenu().action_selected_in_main_menu()
    match choice:
        case 0:
            CreateTournament().create_new_tournament()

        case 1:
            tournament = ControlTournament().select_tournament()
            ControlTournament().play_tournament(tournament=tournament)
        case 2:
            ControlPlayer()
        case 3:
            pass




if __name__ == "__main__":
    main()

