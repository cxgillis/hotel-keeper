import math
from sqlalchemy.orm import Session

from models import Base, Hotel, Room, Guest, Rate, Reservation, Invoice


def print_title_bar(msg: str):
    # Calculate padding for centering the message
    padding = (146-len(msg))/2
    pad_left = math.floor(padding)
    pad_right = math.ceil(padding)
    # Generate the title bar for better visibility
    print("\n\n")
    print("**********"*15)
    print("**"+" "*pad_left+f"{msg}"+" "*pad_right+"**")
    print("**********"*15)


def print_output(msg: str):
    print_title_bar("OUTPUT")
    print(" ")
    print(msg)
    print(" ")
    print("**********"*15)


def initialize_db(db_engine):
    """Drop and recreate all DB tables if they do not exist."""
    # Drop all tables
    Base.metadata.drop_all(db_engine)
    # Recreate all tables
    Base.metadata.create_all(db_engine)


def seed_db(db_engine):
    with Session(db_engine) as session:
        # Insert sample records into the `hotel` table
        hotels = [
            Hotel(name='Grand Plaza', city='New York', state='NY', zip=10001),
            Hotel(name='Hudson Piazza', city='New York', state='NY', zip=10001),
            Hotel(name='Gulf Mansion', city='Tampa Bay', state='FL', zip=33606),
            Hotel(name='Ocean View', city='Miami', state='FL', zip=33101),
            Hotel(name='Mountain Retreat', city='Denver', state='CO', zip=80201)
        ]
        session.add_all(hotels)

        # Insert sample records into the `room` table
        rooms = [
            Room(hotel_id=1, num_rooms=1, num_beds=2, floor=1, is_reservable_flag=1),
            Room(hotel_id=1, num_rooms=1, num_beds=1, floor=1, is_reservable_flag=1),
            Room(hotel_id=2, num_rooms=2, num_beds=3, floor=2, is_reservable_flag=0)
        ]
        session.add_all(rooms)

        # Insert sample records into the `guest` table
        guests = [
            Guest(first_name='John', last_name='Doe', address='123 Elm St, New York, NY', phone=1234567890),
            Guest(first_name='Jane', last_name='Smith', address='456 Oak St, Miami, FL', phone=9876543210),
            Guest(first_name='Alice', last_name='Johnson', address='789 Pine St, Denver, CO', phone=5551234567)
        ]
        session.add_all(guests)

        # Insert sample records into the `rate` table
        rates = [
            Rate(rate_type='Standard', rate_amount=150),
            Rate(rate_type='Deluxe', rate_amount=250),
            Rate(rate_type='Suite', rate_amount=400)
        ]
        session.add_all(rates)

        # Insert sample records into the `reservation` table
        reservations = [
            Reservation(guest_id=1, room_id=1, rate_id=1, discount_pct=10, start_date='2023-10-01', end_date='2023-10-05'),
            Reservation(guest_id=2, room_id=2, rate_id=2, discount_pct=0, start_date='2023-10-10', end_date='2023-10-15'),
            Reservation(guest_id=3, room_id=3, rate_id=3, discount_pct=5, start_date='2023-10-20', end_date='2023-10-25')
        ]
        session.add_all(reservations)

        # Insert sample records into the `invoice` table
        invoices = [
            Invoice(guest_id=1, reservation_id=1, amount=135, is_paid_flag=1, date_paid='2023-10-06'),
            Invoice(guest_id=2, reservation_id=2, amount=250, is_paid_flag=0),
            Invoice(guest_id=3, reservation_id=3, amount=380, is_paid_flag=1, date_paid='2023-10-26')
        ]
        session.add_all(invoices)

        # Commit the transaction
        session.commit()

        print("Database successfully seeded with sample data.")
