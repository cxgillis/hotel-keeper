
active_screen: str = 'main_menu'
select_option_msg: str = "\nPlease select an option:\n"
invalid_option_msg: str = "INVALID OPTION! Please try again."
goodbye_msg: str = "Exiting the application. Goodbye!"

def print_output(msg: str):
    print()
    print("**********"*15)
    print("**"+" "*70+"OUTPUT"+" "*70+"**")
    print("**********"*15)
    print(" ")
    print(msg)
    print(" ")
    print("**********"*15)

def display_main_menu():
    global active_screen

    print("\nWelcome to Hotel-Keeper! Please select an option:\n")
    print("1. Hotels Menu")
    print("2. Rooms Menu")
    print("3. Rates Menu")
    print("4. Reservations Menu")
    print("5. Invoices Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            active_screen = 'hotels_menu'
        case '2':
            active_screen = 'rooms_menu'
        case '3':
            active_screen = 'rates_menu'
        case '4':
            active_screen = 'reservations_menu'
        case '5':
            active_screen = 'invoices_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)


def display_hotels_menu():
    global active_screen

    print("\nHotels Menu: Please select an option:\n")
    print("1. View by Hotel Name")
    print("2. Show All Hotels")
    print("3. Create New Hotel")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            print_output("Filter by Hotel Name:")
        case '2':
            print_output("Show All Hotels:")
        case '3':
            print_output("Create New Hotel:")
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)


def display_rooms_menu():
    global active_screen

    print("\nRooms Menu: Please select an option:\n")
    print("1. View Rooms by Hotel Name")
    print("2. Show All Rooms")
    print("3. Show Reservable Rooms")
    print("4. Create New Room")
    print("b. Back to Main Menu")
    print("x. Exit")

    choice = input(select_option_msg).strip()
    match choice:
        case '1':
            print_output("Filter by Hotel Name:")
        case '2':
            print_output("Show All Rooms:")
        case '3':
            print_output("Show Reservable Rooms:")
        case '4':
            print_output("Create New Room:")
        case 'b':
            active_screen = 'main_menu'
        case 'x':
            print_output(goodbye_msg)
            exit(0)
        case _:
            print_output(invalid_option_msg)


def display_rates_menu():
    global active_screen

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


def display_reservations_menu():
    global active_screen

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


def display_invoices_menu():
    global active_screen

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


def main():

    # Main Menu Loop
    while True:
        match active_screen:
            case 'main_menu':
                display_main_menu()
            case 'hotels_menu':
                display_hotels_menu()
            case 'rooms_menu':
                display_rooms_menu()
            case 'rates_menu':
                display_rates_menu()
            case 'reservations_menu':
                display_reservations_menu()
            case 'invoices_menu':
                display_invoices_menu()
            case _:
                print_output(invalid_option_msg)

if __name__ == "__main__":
    main()
