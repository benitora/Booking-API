
from fastapi import APIRouter
from fastapi.params import Depends

from config.database import SessionLocal
from sqlalchemy.orm import Session

from modules import rooms

router = APIRouter(        #กำหนด instance
    responses={            #response กรณีที่ค้นหาไม่เจอ
        404 : {
            'message': 'Not Found'
        }
    }
)

users = [                      #fake data
    {
        'user_id': 1,
        'name'   : 'Thanwa',
        'age'    : 23
    },
    {
        'user_id': 2,
        'name'   : 'Palette',
        'age'    : 23
    }
]

# @router.get('/readme/{user_id}')        #สร้างเส้นทาง API ด้วย router
# async def read_me(user_id: int):
#     user_id -= 1        #ลบ 1 เพราะว่า users เป็น list(array) ซึ่ง index จะเริ่มที่ 0

#     logging.info('So should this')

#     response=[
#         {
#             'user':users[user_id]
#         }
#     ]

#     return response   #คืนค่าผลลัพธ์

@router.get('/rooms')        #สร้างเส้นทาง API ด้วย router
async def all():
    #logging.info('So should this')

    response={
        'status':True,
        'message':'Successfully',
        'datas':users
    }

    return response   #คืนค่าผลลัพธ์

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/room/search')
async def findRoom(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    # create a new database session
    # session = Session(bind=engine, expire_on_commit=False)
    # data = 

    items = rooms.list_rooms(db, offset, limit)

    response={
        'status':True,
        'message':'Success ssss',
        'datas':items
    }

    return response