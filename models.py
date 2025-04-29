import datetime

from sqlalchemy import (
    create_engine, Column, Integer, String, Text, DateTime, ForeignKey, CheckConstraint
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    city = Column(Text, nullable=False)
    state = Column(Text, nullable=False)
    zip = Column(Integer, nullable=False)
    create_timestamp = Column(DateTime, default=datetime.datetime.now())

    __table_args__ = (
        CheckConstraint('zip BETWEEN 500 AND 99999', name='zip_check'),
    )


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotel.id'), nullable=False)
    num_rooms = Column(Integer, nullable=False)
    num_beds = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    is_reservable_flag = Column(Integer, nullable=False)

    create_timestamp = Column(DateTime, default=datetime.datetime.now())

    __table_args__ = (
        CheckConstraint('is_reservable_flag IN (0, 1)', name='is_reservable_flag_check'),
    )


class Guest(Base):
    __tablename__ = 'guest'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    phone = Column(Integer, nullable=False)
    create_timestamp = Column(DateTime, default=datetime.datetime.now())


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey('guest.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    rate_id = Column(Integer, ForeignKey('rate.id'), nullable=False)
    discount_pct = Column(Integer, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    create_timestamp = Column(DateTime, default=datetime.datetime.now())

    __table_args__ = (
        CheckConstraint("start_date IS date(start_date)", name='start_date_check'),
        CheckConstraint("end_date IS date(end_date)", name='end_date_check'),
    )


class Invoice(Base):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey('guest.id'), nullable=False)
    reservation_id = Column(Integer, ForeignKey('reservation.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    is_paid_flag = Column(Integer, nullable=False)
    date_paid = Column(String, nullable=True)
    create_timestamp = Column(DateTime, default=datetime.datetime.now())

    __table_args__ = (
        CheckConstraint('is_paid_flag IN (0, 1)', name='is_paid_flag_check'),
    )


class Rate(Base):
    __tablename__ = 'rate'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rate_type = Column(Text, nullable=False)
    rate_amount = Column(Integer, nullable=False)
    create_timestamp = Column(DateTime, default=datetime.datetime.now())
