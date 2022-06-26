from sqlalchemy import Column , String, Integer, Text ,DateTime

from config.database import Base

# model/rooms
class roomModel(Base):
    __tablename__ = "rooms"

    ROOM_ID = Column(Integer, primary_key=True, index=True)
    ROOM_CODE = Column(String(255), unique=True)
    ROOM_NAME = Column(String(255))
    ROOM_TYPE = Column(Integer)
    ROOM_CREATE = Column(DateTime)