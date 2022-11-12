from fastapi import APIRouter
import database
import schemas
import models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from controllers import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.DetailUserSchema)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.DetailUserSchema)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
