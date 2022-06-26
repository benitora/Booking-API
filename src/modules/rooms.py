#<project>/modules/rooms/rooms.py
from sqlalchemy.orm import Session
import logging

# Import Module
from models.roomModel import roomModel
from databases.schemas import Rooms # New import

def list_rooms(db: Session , skip: int = 0 ,limit: int = 100):

    query = db.query(roomModel).all()

    array = []
    for row in query:
        data_set={
            'id':row.ROOM_ID,
            'name':row.ROOM_NAME,
            'date':row.ROOM_CREATE
        }

        array.append(data_set)
    return array
    # return db.query(roomModel).offset(skip).limit(limit).all()