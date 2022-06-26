from routers import authen

import uvicorn
from fastapi import FastAPI,Request,status,APIRouter
from fastapi.middleware.cors import CORSMiddleware

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from pydantic import BaseModel # New import

# from .routers import rooms


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["POST", "GET","PUT","DELETE"],
    allow_headers=["*"]
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"errors": exc.errors(),
                "body": exc.body,
                "message": {"Oops! Something Went Wrong "}}),
    )

router = APIRouter(        #กำหนด instance
    responses={            #response กรณีที่ค้นหาไม่เจอ
        404 : {
            'message': 'Not Found'
        }
    }
)

# New
book_db = [
    {
        "title":"The C Programming",
        "price": 720
    },
    {
        "title":"Learn Python the Hard Way",
        "price": 870
    },
    {
        "title":"JavaScript: The Definitive Guide",
        "price": 1369
    },
    {
        "title":"Python for Data Analysis",
        "price": 1394
    },
    {
        "title":"Clean Code",
        "price": 1500
    },
]

# Model
class Book(BaseModel):
    title: str
    price: float

@app.get("/")
async def root():
    return {"message": "Booking API version 1.0.0"}

# @app.get("/book/")
# async def get_books():
#     return book_db

# @app.get("/book/{book_id}")
# async def get_book(book_id: int):
#     return book_db[book_id-1]

# @app.post("/book")
# async def create_book(book: Book):
#     book_db.append(book.dict())
#     return book_db[-1]

# def config_router():                  #สร้างฟังก์ชันขึ้นมาเพื่อ include router ฟังก์ชันชื่ออะไรก็ได้
#     app.include_router(authen.router)
#     app.include_router(rooms.router)
    

# config_router()

if __name__ == '__main__':
    # uvicorn.run(app, host="0.0.0.0", port=8888, debug=True)
    uvicorn.run(app,port=8888, debug=True)