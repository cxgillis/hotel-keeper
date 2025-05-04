from datetime import datetime
from math import floor

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models import Hotel, Room, Guest, Rate, Reservation, Invoice
from utils import print_output, print_query_results


# Hotel Functions

def query_all_hotels(db_engine):
    results = query_hotels(db_engine)
    msg_prefix = f"All Hotels:\n\n"
    print_query_results(results, msg_prefix)


def query_hotel_by_parm(db_engine):
    name = input("Enter hotel name to query, or enter to skip:\n").strip()
    city = input("Enter hotel city to query, or enter to skip:\n").strip()
    state = input("Enter hotel state to query, or enter to skip:\n").strip()
    zip_c = input("Enter hotel zip to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_hotels(db_engine, name, city, state, zip_c)
    msg_prefix = f"Hotel Query Results:\n\n"
    print_query_results(results, msg_prefix)


def query_hotels(db_engine, name=None, city=None, state=None, zip_c=None):
    """Query hotels based on optional parameters."""
    with Session(db_engine) as session:
        sql = session.query(Hotel)
        if name:
            sql = sql.filter(Hotel.name == name)
        if city:
            sql = sql.filter(Hotel.city == city)
        if state:
            sql = sql.filter(Hotel.state == state)
        if zip_c:
            sql = sql.filter(Hotel.zip == zip_c)
        # Get results based on any provided filters
        results = sql.all()
        if not results:
            return "NO RESULTS FOUND MATCHING THE CRITERIA."
        else:
            query_result = "\n".join(
                [f"ID: {hotel.id} | Name: {hotel.name} | City: {hotel.city} | State: {hotel.state} | ZIP: {hotel.zip}"
                 for hotel in results])
        return query_result


def create_hotel(db_engine):
    name = input("Enter hotel name:\n").strip()
    city = input("Enter hotel city:\n").strip()
    state = input("Enter hotel state:\n").strip()
    zip_c = input("Enter hotel zip:\n").strip()

    try:
        with Session(db_engine) as session:
            new_hotel = Hotel(name=name, city=city, state=state, zip=int(zip_c))
            session.add(new_hotel)
            session.commit()
            print_output(f"Hotel '{name}' created successfully with ID: {new_hotel.id}")
    except ValueError:
        print_output("Error: ZIP code must be a valid number")
    except SQLAlchemyError as e:
        session.rollback()
        print_output(f"Database error occurred: {str(e)}")


def delete_hotel(db_engine):
    id_to_del = input("Enter Hotel ID:\n").strip()

    with Session(db_engine) as session:
        hotel_to_del = session.query(Hotel).filter(Hotel.id == int(id_to_del)).first()
        if hotel_to_del:
            session.delete(hotel_to_del)
            session.commit()
            print_output(f"Hotel '{id_to_del}' deleted successfully.")
        else:
            print_output(f"Hotel '{id_to_del}' not found.")


# Room Functions

def query_all_rooms(db_engine):
    results = query_rooms(db_engine)
    msg_prefix = f"All Rooms:\n\n"
    print_query_results(results, msg_prefix)


def query_room_by_parm(db_engine):
    hotel_id = input("Enter hotel ID to query, or enter to skip:\n").strip()
    num_rooms = input("Enter number of rooms to query, or enter to skip:\n").strip()
    num_beds = input("Enter number of beds to query, or enter to skip:\n").strip()
    floor_num = input("Enter floor to query, or enter to skip:\n").strip()
    reservable = input("Enter reservable flag (0 -> False or 1 -> True) to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_rooms(db_engine, hotel_id, num_rooms, num_beds, floor_num, reservable)
    msg_prefix = f"Room Query Results:\n\n"
    print_query_results(results, msg_prefix)


def query_rooms(db_engine, hotel_id=None, num_rooms=None, num_beds=None, floor_num=None, reservable=None):
    """Query rooms based on optional parameters."""
    with Session(db_engine) as session:
        sql = session.query(Room)
        if hotel_id:
            sql = sql.filter(Room.hotel_id == int(hotel_id))
        if num_rooms:
            sql = sql.filter(Room.num_rooms == int(num_rooms))
        if num_beds:
            sql = sql.filter(Room.num_beds == int(num_beds))
        if floor_num:
            sql = sql.filter(Room.floor == int(floor_num))
        if reservable in ('0', '1'):
            sql = sql.filter(Room.is_reservable_flag == int(reservable))
        # Get results based on any provided filters
        results = sql.all()
        if not results:
            return "NO RESULTS FOUND MATCHING THE CRITERIA."
        else:
            query_result = "\n".join(
                [f"ID: {room.id} | Hotel ID: {room.hotel_id} | Num Rooms: {room.num_rooms} | Num Beds: {room.num_beds} | "
                f"Floor: {room.floor} | Reservable: {room.is_reservable_flag}" for room in results])
        return query_result


def change_room_availability(db_engine):
    id_to_change = input("Enter Room ID:\n").strip()
    new_availability = input("Enter new availability (0 -> False or 1 -> True):\n").strip()
    if new_availability not in ('0', '1'):
        print_output("ERROR: Availability must be either 0 or 1")
        return

    with Session(db_engine) as session:
        room_to_change = session.query(Room).filter(Room.id == int(id_to_change)).first()
        if room_to_change:
            room_to_change.is_reservable_flag = int(new_availability)
            session.commit()
            print_output(f"Room {id_to_change} availability changed to {'False' if new_availability == 0 else 'True'}.")
        else:
            print_output(f"ERROR: Room {id_to_change} not found.")


def create_room(db_engine):
    hotel_id = input("Enter hotel ID:\n").strip()
    num_rooms = input("Enter number of rooms:\n").strip()
    num_beds = input("Enter number of beds:\n").strip()
    floor_num = input("Enter floor:\n").strip()
    reservable = input("Enter reservable flag (0 -> False or 1 -> True):\n").strip()

    try:
        with Session(db_engine) as session:
            new_room = Room(hotel_id=int(hotel_id), num_rooms=int(num_rooms), num_beds=int(num_beds),
                            floor=int(floor_num), is_reservable_flag=int(reservable))
            session.add(new_room)
            session.commit()
            print_output(f"Room created successfully with ID: {new_room.id}")
    except ValueError:
        print_output("Error: All fields must be valid numbers")
    except SQLAlchemyError as e:
        session.rollback()
        print_output(f"Database error occurred: {str(e)}")


def delete_room(db_engine):
    id_to_del = input("Enter Room ID:\n").strip()

    with Session(db_engine) as session:
        room_to_del = session.query(Room).filter(Room.id == int(id_to_del)).first()
        if room_to_del:
            session.delete(room_to_del)
            session.commit()
            print_output(f"Room '{id_to_del}' deleted successfully.")
        else:
            print_output(f"Room '{id_to_del}' not found.")


# Guest Functions

def query_all_guests(db_engine):
    results = query_guests(db_engine)
    msg_prefix = f"All Guests:\n\n"
    print_query_results(results, msg_prefix)


def query_guest_by_parm(db_engine):
    first_name = input("Enter guest first name to query, or enter to skip:\n").strip()
    last_name = input("Enter guest last name to query, or enter to skip:\n").strip()
    address = input("Enter guest address to query, or enter to skip:\n").strip()
    phone = input("Enter guest phone number to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_guests(db_engine, first_name, last_name, address, phone)
    msg_prefix = f"Guest Query Results:\n\n"
    print_query_results(results, msg_prefix)


def query_guests(db_engine, first_name=None, last_name=None, address=None, phone=None):
    """Query guests based on optional parameters."""
    with Session(db_engine) as session:
        sql = session.query(Guest)
        if first_name:
            sql = sql.filter(Guest.first_name == first_name)
        if last_name:
            sql = sql.filter(Guest.last_name == last_name)
        if address:
            sql = sql.filter(Guest.address == address)
        if phone:
            sql = sql.filter(Guest.phone == int(phone))
        # Get results based on any provided filters
        results = sql.all()
        if not results:
            return "NO RESULTS FOUND MATCHING THE CRITERIA."
        else:
            query_result = "\n".join(
                [f"ID: {guest.id} | First Name: {guest.first_name} | Last Name: {guest.last_name} | "
                 f"Address: {guest.address} | Phone: {guest.phone}" for guest in results])
        return query_result


def create_guest(db_engine):
    first_name = input("Enter guest first name:\n").strip()
    last_name = input("Enter guest last name:\n").strip()
    address = input("Enter guest address:\n").strip()
    phone = input("Enter guest phone number:\n").strip()

    try:
        with Session(db_engine) as session:
            new_guest = Guest(first_name=first_name, last_name=last_name, address=address, phone=int(phone))
            session.add(new_guest)
            session.commit()
            print_output(f"Guest created successfully with ID: {new_guest.id}")
    except ValueError:
        print_output("Error: Phone number must be a valid number")
    except SQLAlchemyError as e:
        session.rollback()
        print_output(f"Database error occurred: {str(e)}")


def delete_guest(db_engine):
    id_to_del = input("Enter Guest ID:\n").strip()

    with Session(db_engine) as session:
        guest_to_del = session.query(Guest).filter(Guest.id == int(id_to_del)).first()
        if guest_to_del:
            session.delete(guest_to_del)
            session.commit()
            print_output(f"Guest '{id_to_del}' deleted successfully.")
        else:
            print_output(f"Guest '{id_to_del}' not found.")


# Reservation Functions

def query_all_reservations(db_engine):
    results = query_reservations(db_engine)
    msg_prefix = f"All Reservations:\n\n"
    print_query_results(results, msg_prefix)


def query_reservation_by_parm(db_engine):
    guest_id = input("Enter guest ID to query, or enter to skip:\n").strip()
    room_id = input("Enter room ID to query, or enter to skip:\n").strip()
    rate_id = input("Enter rate ID to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_reservations(db_engine, guest_id, room_id, rate_id)
    msg_prefix = f"Reservation Query Results:\n\n"
    print_query_results(results, msg_prefix)


def query_reservations(db_engine, guest_id=None, room_id=None, rate_id=None):
    """Query reservations based on optional parameters."""
    with Session(db_engine) as session:
        sql = session.query(Reservation)
        if guest_id:
            sql = sql.filter(Reservation.guest_id == int(guest_id))
        if room_id:
            sql = sql.filter(Reservation.room_id == int(room_id))
        if rate_id:
            sql = sql.filter(Reservation.rate_id == int(rate_id))
        # Get results based on any provided filters
        results = sql.all()
        if not results:
            return "NO RESULTS FOUND MATCHING THE CRITERIA."
        else:
            query_result = "\n".join(
                [f"ID: {reservation.id} | Guest ID: {reservation.guest_id} | Room ID: {reservation.room_id} | "
                 f"Rate ID: {reservation.rate_id} | Discount %: {reservation.discount_pct} | "
                 f"Start Date: {reservation.start_date} | End Date: {reservation.end_date}" for reservation in results])
        return query_result


def create_reservation(db_engine):
    guest_id = input("Enter guest ID:\n").strip()
    room_id = input("Enter room ID:\n").strip()
    rate_id = input("Enter rate ID:\n").strip()
    discount_pct = input("Enter discount percentage:\n").strip()
    start_date = input("Enter start date (YYYY-MM-DD):\n").strip()
    end_date = input("Enter end date (YYYY-MM-DD):\n").strip()

    try:
        with Session(db_engine) as session:
            new_reservation = Reservation(guest_id=int(guest_id), room_id=int(room_id), rate_id=int(rate_id),
                                          discount_pct=int(discount_pct), start_date=start_date, end_date=end_date)
            session.add(new_reservation)
            session.commit()
            print_output(f"Reservation created successfully with ID: {new_reservation.id}")
    except ValueError:
        print_output("Error: All fields must be whole numbers")
    except SQLAlchemyError as e:
        session.rollback()
        print_output(f"Database error occurred: {str(e)}")


def delete_reservation(db_engine):
    id_to_del = input("Enter Reservation ID:\n").strip()

    with Session(db_engine) as session:
        reservation_to_del = session.query(Reservation).filter(Reservation.id == int(id_to_del)).first()
        if reservation_to_del:
            session.delete(reservation_to_del)
            session.commit()
            print_output(f"Reservation '{id_to_del}' deleted successfully.")
        else:
            print_output(f"Reservation '{id_to_del}' not found.")


# Invoice Functions

def query_all_invoices(db_engine):
    results = query_invoices(db_engine)
    msg_prefix = f"All Invoices:\n\n"
    print_query_results(results, msg_prefix)


def query_invoice_by_parm(db_engine):
    guest_id = input("Enter guest ID to query, or enter to skip:\n").strip()
    reservation_id = input("Enter reservation ID to query, or enter to skip:\n").strip()
    is_paid = input("Enter paid flag (0 -> False or 1 -> True) to query, or enter to skip:\n").strip()
    date_paid = input("Enter date paid in YYYY-MM-DD to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_invoices(db_engine, guest_id, reservation_id, is_paid, date_paid)
    msg_prefix = f"Invoice Query Results:\n\n"
    print_query_results(results, msg_prefix)


def query_invoices(db_engine, guest_id=None, reservation_id=None, is_paid=None, date_paid=None):
    """Query invoices based on optional parameters."""
    try:
        with Session(db_engine) as session:
            sql = session.query(Invoice)
            if guest_id:
                sql = sql.filter(Invoice.guest_id == int(guest_id))
            if reservation_id:
                sql = sql.filter(Invoice.reservation_id == int(reservation_id))
            if is_paid in ('0', '1'):
                sql = sql.filter(Invoice.is_paid_flag == int(is_paid))
            if date_paid:
                sql = sql.filter(Invoice.date_paid == date_paid)
            # Get results based on any provided filters
            results = sql.all()
            if not results:
                query_result = "NO RESULTS FOUND MATCHING THE CRITERIA."
            else:
                query_result = "\n".join(
                    [f"ID: {invoice.id} | Guest ID: {invoice.guest_id} | Reservation ID: {invoice.reservation_id} | "
                     f"Amount: {invoice.amount} | Paid: {invoice.is_paid_flag}" for invoice in results])
    except ValueError:
        query_result = "Error: Invalid data type provided for one or more search fields"
    except SQLAlchemyError as e:
        session.rollback()
        query_result = f"Database error occurred: {str(e)}"
    return query_result


def create_invoice(db_engine):
    reservation_id = input("Enter reservation ID:\n").strip()

    try:
        with Session(db_engine) as session:
            # Check if invoice already created for this reservation
            existing_invoice = session.query(Invoice).filter(Invoice.reservation_id == int(reservation_id)).first()
            if existing_invoice:
                print_output(f"Invoice already exists for Reservation ID: {reservation_id}")
                return
            # else create a new invoice
            else:
                # get foreign keys for new invoice from existing reservation
                reservation = session.query(Reservation).filter(Reservation.id == int(reservation_id)).first()
                # calculate the invoice amount from rate and total length of stay
                rate = session.query(Rate).filter(Rate.id == reservation.rate_id).first()
                # Convert date strings to datetime objects
                start = datetime.strptime(reservation.start_date, '%Y-%m-%d')
                end = datetime.strptime(reservation.end_date, '%Y-%m-%d')
                total_days = (end - start).days
                amount = floor(rate.rate_amount * total_days * (1 - reservation.discount_pct / 100))
                # create a new invoice with calculated values
                new_invoice = Invoice(guest_id=reservation.guest_id, reservation_id=reservation.id, amount=amount)
                session.add(new_invoice)
                session.commit()
                print_output(f"Invoice created successfully with ID: {new_invoice.id}")
    except ValueError:
        print_output("Error: All fields must be valid numbers")
    except SQLAlchemyError as e:
        session.rollback()
        print_output(f"Database error occurred: {str(e)}")


def delete_invoice(db_engine):
    id_to_del = input("Enter Invoice ID:\n").strip()

    with Session(db_engine) as session:
        invoice_to_del = session.query(Invoice).filter(Invoice.id == int(id_to_del)).first()
        if invoice_to_del:
            session.delete(invoice_to_del)
            session.commit()
            print_output(f"Invoice '{id_to_del}' deleted successfully.")
        else:
            print_output(f"Invoice '{id_to_del}' not found.")


def pay_invoice(db_engine):
    id_to_pay = input("Enter Invoice ID:\n").strip()

    with Session(db_engine) as session:
        invoice_to_pay = session.query(Invoice).filter(Invoice.id == int(id_to_pay)).first()
        if invoice_to_pay:
            # Check if the invoice is already paid
            if invoice_to_pay.is_paid_flag == 1:
                print_output(f"Invoice '{id_to_pay}' is already paid.")
                return
            # else update the invoice to paid
            else:
                invoice_to_pay.is_paid_flag = 1
                invoice_to_pay.date_paid = datetime.now().strftime('%Y-%m-%d')
                session.commit()
                print_output(f"Invoice '{id_to_pay}' paid successfully.")
        else:
            print_output(f"Invoice '{id_to_pay}' not found.")


def print_invoice(db_engine):
    id_to_print = input("Enter Invoice ID:\n").strip()

    with Session(db_engine) as session:
        invoice_to_print = session.query(Invoice).filter(Invoice.id == int(id_to_print)).first()
        if invoice_to_print:
            # Lookup related table details from foreign keys
            guest = session.query(Guest).filter(Guest.id == invoice_to_print.guest_id).first()
            reservation = session.query(Reservation).filter(Reservation.id == invoice_to_print.reservation_id).first()
            rate = session.query(Rate).filter(Rate.id == reservation.rate_id).first()
            room = session.query(Room).filter(Room.id == reservation.room_id).first()
            hotel = session.query(Hotel).filter(Hotel.id == room.hotel_id).first()
            # Print the invoice details
            invoice_text = f"Invoice ID: {invoice_to_print.id}"
            invoice_text = invoice_text + f"\nGuest: {guest.first_name} {guest.last_name}"
            invoice_text = invoice_text + f"\nHotel: {hotel.name}, {hotel.city}, {hotel.state}, {hotel.zip}"
            invoice_text = invoice_text + f"\nRoom: {room.id}, Floor: {room.floor}, Beds: {room.num_beds}"
            invoice_text = invoice_text + f"\nRate: {rate.rate_type}, Amount: {rate.rate_amount} per day"
            invoice_text = invoice_text + f" --> Discount applied: {reservation.discount_pct}%"
            invoice_text = invoice_text + f"\nReservation Dates: {reservation.start_date} to {reservation.end_date}"
            invoice_text = invoice_text + (f", Length of Stay: {(datetime.strptime(reservation.end_date, '%Y-%m-%d') 
                                               - datetime.strptime(reservation.start_date, '%Y-%m-%d')).days} days")
            invoice_text = invoice_text + f"\nInvoice Total Amount: {invoice_to_print.amount}"
            invoice_text = invoice_text + f"\nInvoice Paid: {'Yes' if invoice_to_print.is_paid_flag == 1 else 'No'}"
            print_output(invoice_text)
        else:
            print_output(f"Invoice '{id_to_print}' not found.")


# Rate Functions

def query_all_rates(db_engine):
    results = query_rates(db_engine)
    msg_prefix = f"All Rates:\n\n"
    print_query_results(results, msg_prefix)


def query_rate_by_parm(db_engine):
    rate_type = input("Enter rate type to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_rates(db_engine, rate_type)
    msg_prefix = f"Rate Query Results:\n\n"
    print_query_results(results, msg_prefix)

def query_rates(db_engine, rate_type=None):
    """Query rates based on optional parameters."""
    with Session(db_engine) as session:
        sql = session.query(Rate)
        if rate_type:
            sql = sql.filter(Rate.rate_type == rate_type)
        # Get results based on any provided filters
        results = sql.all()
        if not results:
            return "NO RESULTS FOUND MATCHING THE CRITERIA."
        else:
            query_result = "\n".join(
                [f"ID: {rate.id} | Rate Type: {rate.rate_type} | Rate Amount: {rate.rate_amount}" for rate in results])
        return query_result


def create_rate(db_engine):
    rate_type = input("Enter rate type:\n").strip()
    rate_amount = input("Enter rate amount:\n").strip()

    try:
        with Session(db_engine) as session:
            new_rate = Rate(rate_type=rate_type, rate_amount=int(rate_amount))
            session.add(new_rate)
            session.commit()
            print_output(f"Rate created successfully with ID: {new_rate.id}")
    except ValueError:
        print_output("Error: Rate amount must be a valid number")
    except SQLAlchemyError as e:
        session.rollback()
        print_output(f"Database error occurred: {str(e)}")


def delete_rate(db_engine):
    id_to_del = input("Enter Rate ID:\n").strip()

    with Session(db_engine) as session:
        rate_to_del = session.query(Rate).filter(Rate.id == int(id_to_del)).first()
        if rate_to_del:
            session.delete(rate_to_del)
            session.commit()
            print_output(f"Rate '{id_to_del}' deleted successfully.")
        else:
            print_output(f"Rate '{id_to_del}' not found.")
