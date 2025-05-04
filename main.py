from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

from services import *
from utils import *

active_screen: str = 'main_menu'
select_option_msg: str = "\nPlease select an option:\n"
invalid_option_msg: str = "INVALID OPTION! Please try again."
goodbye_msg: str = "Exiting the application. Goodbye!"


def display_main_menu():
    global active_screen

    print_title_bar("MAIN MENU")
    print("\nWelcome to Hotel-Keeper! Please select an option:\n")
    print("1. Hotels Menu")
    print("2. Rooms Menu")
    print("3. Guests Menu")
    print("4. Reservations Menu")
    print("5. Invoices Menu")
    print("6. Rates Menu")
    print("0. Admin Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            active_screen = 'hotels_menu'
        case '2':
            active_screen = 'rooms_menu'
        case '3':
            active_screen = 'guests_menu'
        case '4':
            active_screen = 'reservations_menu'
        case '5':
            active_screen = 'invoices_menu'
        case '6':
            active_screen = 'rates_menu'
        case '0':
            active_screen = 'admin_menu'
        case 'x':
            exit_app()
        case _:
            print_output(invalid_option_msg)


def display_hotels_menu(db_engine):
    global active_screen

    print_title_bar("HOTELS MENU")
    print("\nHotels Menu: Please select an option:\n")
    print("1. Search for Hotels")
    print("2. Show All Hotels")
    print("3. Create New Hotel")
    print("4. Delete Hotel")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_hotel_by_parm(db_engine)
        case '2':
            query_all_hotels(db_engine)
        case '3':
            create_hotel(db_engine)
        case '4':
            delete_hotel(db_engine)
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            exit_app()
        case _:
            print_output(invalid_option_msg)


def display_rooms_menu(db_engine):
    global active_screen

    print_title_bar("ROOMS MENU")
    print("\nRooms Menu: Please select an option:\n")
    print("1. Search for Rooms")
    print("2. Show All Rooms")
    print("3. Change Room Availability")
    print("4. Create New Room")
    print("5. Delete Room")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_room_by_parm(db_engine)
        case '2':
            query_all_rooms(db_engine)
        case '3':
            change_room_availability(db_engine)
        case '4':
            create_room(db_engine)
        case '5':
            delete_room(db_engine)
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            exit_app()
        case _:
            print_output(invalid_option_msg)


def display_guests_menu(db_engine):
    global active_screen

    print_title_bar("GUESTS MENU")
    print("\nGuests Menu: Please select an option:\n")
    print("1. Search for Guests")
    print("2. Show All Guests")
    print("3. Create New Guest")
    print("4. Delete Guest")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_guest_by_parm(db_engine)
        case '2':
            query_all_guests(db_engine)
        case '3':
            create_guest(db_engine)
        case '4':
            delete_guest(db_engine)
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            exit_app()
        case _:
            print_output(invalid_option_msg)


def display_reservations_menu(db_engine):
    global active_screen

    print_title_bar("RESERVATIONS MENU")
    print("\nRates Menu: Please select an option:\n")
    print("1. Search for Reservations")
    print("2. View All Reservations")
    print("3. Create new Reservation")
    print("4. Cancel Reservation")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_reservation_by_parm(db_engine)
        case '2':
            query_all_reservations(db_engine)
        case '3':
            create_reservation(db_engine)
        case '4':
            delete_reservation(db_engine)
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            exit_app()
        case _:
            print_output(invalid_option_msg)


def display_invoices_menu(db_engine):
    global active_screen

    print_title_bar("INVOICES MENU")
    print("\nRates Menu: Please select an option:\n")
    print("1. Search for Invoices")
    print("2. View All Invoices")
    print("3. Create new Invoice")
    print("4. Delete Invoice")
    print("5. Pay Invoice")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_invoice_by_parm(db_engine)
        case '2':
            query_all_invoices(db_engine)
        case '3':
            create_invoice(db_engine)
        case '4':
            delete_invoice(db_engine)
        case '5':
            pay_invoice(db_engine)
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            exit_app()
        case _:
            print_output(invalid_option_msg)


def display_rates_menu(db_engine):
    global active_screen

    print_title_bar("RATES MENU")
    print("\nRates Menu: Please select an option:\n")
    print("1. View All Rates")
    print("2. Create new Rate")
    print("3. Delete Rate")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_all_rates(db_engine)
        case '2':
            create_rate(db_engine)
        case '3':
            delete_rate(db_engine)
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            exit_app()
        case _:
            print_output(invalid_option_msg)


def display_admin_menu(db_engine):
    global active_screen

    print_title_bar("ADMIN MENU")
    print("\nAdmin Menu: Please select an option:\n")
    print("1. Reset/Purge Database")
    print("2. Seed Database with Initial Data")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            print_output("Reset/Purge Database:")
            initialize_db(db_engine)
        case '2':
            print_output("Seed Database with Initial Data:")
            seed_db(db_engine)
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            exit_app()
        case _:
            print_output(invalid_option_msg)


def main():
    engine = create_engine(
        'sqlite:///hotel_keeper.db',
        connect_args={'check_same_thread': False},  # Need for SQLite
        # echo=True # Adding logging for debugging
    )
    if not database_exists(engine.url):
        initialize_db(engine)

    # Main Menu Loop
    while True:
        match active_screen:
            case 'main_menu':
                display_main_menu()
            case 'hotels_menu':
                display_hotels_menu(engine)
            case 'rooms_menu':
                display_rooms_menu(engine)
            case 'guests_menu':
                display_guests_menu(engine)
            case 'reservations_menu':
                display_reservations_menu(engine)
            case 'invoices_menu':
                display_invoices_menu(engine)
            case 'rates_menu':
                display_rates_menu(engine)
            case 'admin_menu':
                display_admin_menu(engine)
            case _:
                print_output(invalid_option_msg)
                # Kick back to the Main Menu if an invalid screen is detected
                display_main_menu()


if __name__ == "__main__":
    main()
