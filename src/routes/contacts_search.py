from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from starlette import status

from src.database.db import get_db
from src.repository.contacts import match_by_name, match_by_surname, match_by_email
from src.schemas import ContactResponseModel

router = APIRouter(prefix='/contacts/search', tags=['search contacts'])


@router.get('/name/{name}', response_model=List[ContactResponseModel])
async def search_by_name(name: str, db: Session = Depends(get_db)):
    contacts = await match_by_name(name, db)
    return contacts


@router.get('/surname/{surname}', response_model=List[ContactResponseModel])
async def search_by_surname(surname: str, db: Session = Depends(get_db)):
    contacts = await match_by_surname(surname, db)
    return contacts


@router.get('/email/{email}', response_model=ContactResponseModel)
async def search_by_email(email: EmailStr, db: Session = Depends(get_db)):
    contact = await match_by_email(email, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact
