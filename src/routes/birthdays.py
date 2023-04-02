from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository.contacts import get_birthdays_week
from src.schemas import ContactResponseModel

router = APIRouter(prefix='/birthdays', tags=['birthdays'])


@router.get('/', response_model=List[ContactResponseModel])
async def get_birthdays(db: Session = Depends(get_db)):
    contacts = await get_birthdays_week(db)
    return contacts
