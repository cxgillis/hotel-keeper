from sqlalchemy.orm import Session

from models import Base, Hotel, Room, Guest, Rate, Reservation, Invoice
from utils import print_output


# Hotels Query Functions

def query_all_hotels(db_engine):
    results = query_hotels(db_engine)
    output = f"All Hotels:\n\n{results}"
    print_output(output)


def query_hotel_by_parm(db_engine):
    name = input("Enter hotel name to query, or enter to skip:\n").strip()
    city = input("Enter hotel city to query, or enter to skip:\n").strip()
    state = input("Enter hotel state to query, or enter to skip:\n").strip()
    zip_c = input("Enter hotel zip to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_hotels(db_engine, name, city, state, zip_c)
    output = f"Hotel Query Results:\n\n{results}"
    print_output(output)


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


# Rooms Query Functions

def query_all_rooms(db_engine):
    results = query_rooms(db_engine)
    output = f"All Rooms:\n\n{results}"
    print_output(output)


def query_room_by_parm(db_engine):
    hotel_id = input("Enter hotel ID to query, or enter to skip:\n").strip()
    num_rooms = input("Enter number of rooms to query, or enter to skip:\n").strip()
    num_beds = input("Enter number of beds to query, or enter to skip:\n").strip()
    floor = input("Enter floor to query, or enter to skip:\n").strip()
    reservable = input("Enter reservable flag (0 -> False or 1 -> True) to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_rooms(db_engine, hotel_id, num_rooms, num_beds, floor, reservable)
    output = f"Room Query Results:\n\n{results}"
    print_output(output)


def query_rooms(db_engine, hotel_id=None, num_rooms=None, num_beds=None, floor=None, reservable=None):
    """Query rooms based on optional parameters."""
    with Session(db_engine) as session:
        sql = session.query(Room)
        if hotel_id:
            sql = sql.filter(Room.hotel_id == int(hotel_id))
        if num_rooms:
            sql = sql.filter(Room.num_rooms == int(num_rooms))
        if num_beds:
            sql = sql.filter(Room.num_beds == int(num_beds))
        if floor:
            sql = sql.filter(Room.floor == int(floor))
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


# Guests Query Functions
def query_all_guests(db_engine):
    results = query_guests(db_engine)
    output = f"All Guests:\n\n{results}"
    print_output(output)


def query_guest_by_parm(db_engine):
    first_name = input("Enter guest first name to query, or enter to skip:\n").strip()
    last_name = input("Enter guest last name to query, or enter to skip:\n").strip()
    address = input("Enter guest address to query, or enter to skip:\n").strip()
    phone = input("Enter guest phone number to query, or enter to skip:\n").strip()
    # Run the query with the provided parameters
    results = query_guests(db_engine, first_name, last_name, address, phone)
    output = f"Guest Query Results:\n\n{results}"
    print_output(output)


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
