from datetime import date
from pydantic import BaseModel

class Rooms(BaseModel):
    ROOM_ID : int
    ROOM_CODE : str
    ROOM_NAME : str
    ROOM_TYPE : int
    ROOM_CREATE: date

    class Config:
        orm_mode = True

class CreateRoom(BaseModel):
    ROOM_ID : int
    ROOM_CODE : str
    ROOM_NAME : str
    ROOM_TYPE : int
    submitter_id: int