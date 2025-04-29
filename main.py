from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

from services import query_all_hotels, query_hotel_by_parm, query_room_by_parm, query_all_rooms, query_guest_by_parm, \
    query_all_guests
from utils import print_title_bar, print_output, initialize_db, seed_db

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
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)


def display_hotels_menu(db_engine):
    global active_screen

    print_title_bar("HOTELS MENU")
    print("\nHotels Menu: Please select an option:\n")
    print("1. Search for Hotels")
    print("2. Show All Hotels")
    print("3. Create New Hotel")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_hotel_by_parm(db_engine)
        case '2':
            query_all_hotels(db_engine)
        case '3':
            print_output("Create New Hotel:")
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)


def display_rooms_menu(db_engine):
    global active_screen

    print_title_bar("ROOMS MENU")
    print("\nRooms Menu: Please select an option:\n")
    print("1. Search for Rooms")
    print("2. Show All Rooms")
    print("3. Create New Room")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_room_by_parm(db_engine)
        case '2':
            query_all_rooms(db_engine)
        case '3':
            print_output("Create New Room:")
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)

def display_guests_menu(db_engine):
    global active_screen

    print_title_bar("GUESTS MENU")
    print("\nGuests Menu: Please select an option:\n")
    print("1. Search for Guests")
    print("2. Show All Guests")
    print("3. Create New Guest")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            query_guest_by_parm(db_engine)
        case '2':
            query_all_guests(db_engine)
        case '3':
            print_output("Create New Guest:")
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)


def display_reservations_menu(db_engine):
    global active_screen

    print_title_bar("RESERVATIONS MENU")
    print("\nRates Menu: Please select an option:\n")
    print("1. View All Reservations")
    print("2. Create new Reservation")
    print("3. Cancel Reservation")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            print_output("Show All Reservations:")
        case '2':
            print_output("Create New Reservation:")
        case '3':
            print_output("Cancel Reservation:")
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)


def display_invoices_menu(db_engine):
    global active_screen

    print_title_bar("INVOICES MENU")
    print("\nRates Menu: Please select an option:\n")
    print("1. View All Invoices")
    print("2. Create new Invoice")
    print("3. Pay Invoice")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            print_output("Show All Invoices:")
        case '2':
            print_output("Create New Invoice:")
        case '3':
            print_output("Pay Invoice:")
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)


def display_rates_menu(db_engine):
    global active_screen

    print_title_bar("RATES MENU")
    print("\nRates Menu: Please select an option:\n")
    print("1. View All Rates")
    print("2. Create new Rate")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            print_output("Show All Rates:")
        case '2':
            print_output("Create New Rate:")
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
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
            print_output(goodbye_msg)
            exit(0)
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
