from fastapi import Body,Request,APIRouter,Header,HTTPException

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, validator ,ValidationError

from config.database import engine, SessionLocal
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from modules import authentication

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class oauth2Item(BaseModel):
    client_key: str
    client_secret: str

@router.post('/oauth2/token')
async def oauth2(request: oauth2Item):
    try:

        if not request.client_secret:
            raise HTTPException(status_code=404, detail="Name field is required")

        if request.client_key :
            print('Variavel definida')
            response={
                'status':True,
                'message':'Successfully',
                'data':request
            }

            return response
        else :
            print ("OOps: Something Els")

    except ValidationError as err:
        raise HTTPException(status_code=500, detail=jsonable_encoder(err.errors()))
        # catastrophic error. bail.
    
    except ValueError as err:
        raise HTTPException(status_code=500, detail=jsonable_encoder(err.errors()))
        # catastrophic error. bail.
        
    # authenResponse = authentication.api_key_auth
