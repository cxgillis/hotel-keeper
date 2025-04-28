
current_screen: str = 'main_menu'

def display_main_menu():
    print("\nWelcome to Hotel-Keeper! Please select an option:\n")
    print("1. Hotels Menu")
    print("2. Rooms Menu")
    print("3. Rates Menu")
    print("4. Reservations Menu")
    print("5. Invoices Menu")
    print("x. Exit")
    global current_screen
    current_screen = 'main_menu'


def display_hotels_menu():
    print("\nHotels Menu: Please select an option:\n")
    print("1. View by Hotel Name")
    print("2. Show All Hotels")
    print("b. Back to Main Menu")
    print("x. Exit")
    global current_screen
    current_screen = 'hotels_menu'


def display_rooms_menu():
    print("\nRooms Menu: Please select an option:\n")
    print("1. View Rooms by Hotel Name")
    print("2. Show All Rooms")
    print("3. Show Reservable Rooms")
    print("b. Back to Main Menu")
    print("x. Exit")
    global current_screen
    current_screen = 'rooms_menu'


def display_rates_menu():
    print("\nRates Menu: Please select an option:\n")
    print("1. View All Rates")
    print("2. Create new Rate")
    print("b. Back to Main Menu")
    print("x. Exit")
    global current_screen
    current_screen = 'rates_menu'


def display_reservations_menu():
    print("\nRates Menu: Please select an option:\n")
    print("1. View All Reservations")
    print("2. Create new Reservation")
    print("b. Back to Main Menu")
    print("x. Exit")
    global current_screen
    current_screen = 'reservations_menu'


def display_invoices_menu():
    print("\nRates Menu: Please select an option:\n")
    print("1. View All Invoices")
    print("2. Create new Invoice")
    print("3. Pay Invoice")
    print("b. Back to Main Menu")
    print("x. Exit")
    global current_screen
    current_screen = 'invoices_menu'


def main():

    # Setup initial menu screen
    display_main_menu()

    # Main Menu Loop
    while True:

        choice = input("\nPlease select an option: ").strip()

        match current_screen:
            case 'main_menu':
                match choice:
                    case '1':
                        display_hotels_menu()
                    case '2':
                        display_rooms_menu()
                    case 'x':
                        print("Exiting the application. Goodbye!")
                        break
                    case _:
                        print("Invalid option. Please try again.")
            case 'hotels_menu':
                match choice:
                    case '1':
                        print("\nFilter by Hotel Name:")
                    case '2':
                        print("\nShow All Hotels:")
                    case '3':
                        print("\nCreate New Hotel:")
                    case 'b':
                        display_main_menu()
                    case 'x':
                        print("Exiting the application. Goodbye!")
                        break
                    case _:
                        print("Invalid option. Please try again.")
            case 'rooms_menu':
                match choice:
                    case '1':
                        print("\nFilter by Hotel Name:")
                    case '2':
                        print("\nShow All Rooms:")
                    case '3':
                        print("\nShow Reservable Rooms:")
                    case '4':
                        print("\nCreate New Room:")
                    case 'b':
                        display_main_menu()
                    case 'x':
                        print("Exiting the application. Goodbye!")
                        break
                    case _:
                        print("Invalid option. Please try again.")
            case 'rates_menu':
                match choice:
                    case '1':
                        print("\nShow All Rates:")
                    case '2':
                        print("\nCreate New Rate:")
                    case 'b':
                        display_main_menu()
                    case 'x':
                        print("Exiting the application. Goodbye!")
                        break
                    case _:
                        print("Invalid option. Please try again.")
            case 'reservations_menu':
                match choice:
                    case '1':
                        print("\nShow All Reservations:")
                    case '2':
                        print("\nCreate New Reservation:")
                    case 'b':
                        display_main_menu()
                    case 'x':
                        print("Exiting the application. Goodbye!")
                        break
                    case _:
                        print("Invalid option. Please try again.")
            case 'invoices_menu':
                match choice:
                    case '1':
                        print("\nShow All Invoices:")
                    case '2':
                        print("\nCreate New Invoice:")
                    case '3':
                        print("\nPay Invoice:")
                    case 'b':
                        display_main_menu()
                    case 'x':
                        print("Exiting the application. Goodbye!")
                        break
                    case _:
                        print("Invalid option. Please try again.")
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()