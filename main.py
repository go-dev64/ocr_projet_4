from controllers.create_tournament import CreateTournament
from controllers.control_tournament import ControlTournament
from controllers.control_player import ControlPlayer
from controllers.control_menu import ControlMenu
from controllers.control_data import data_tournaments_list, data_players_list


def main():
    create = CreateTournament()
    control_tournament = ControlTournament()
    player = ControlPlayer()
    player.instancing_all_player_in_data_players_list()
    control_tournament.reload_all_tournament_in_database()
    ControlMenu(
        create_tournament=create,
        control_tournament=control_tournament,
        player=player).main_menu()


if __name__ == "__main__":
    main()
