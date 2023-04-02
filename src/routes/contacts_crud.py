from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.database.db import get_db
from src.repository.contacts import get_contacts, get_contact, post_contact, put_contact, delete_contact
from src.schemas import ContactResponseModel, ContactInputModel

router = APIRouter(prefix='/contacts', tags=['contacts'])


@router.get('/', response_model=List[ContactResponseModel])
async def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    contacts = await get_contacts(skip, limit, db)
    return contacts


@router.get('/{contact_id}', response_model=ContactResponseModel)
async def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.post('/', response_model=ContactInputModel)
async def create_contact(body: ContactInputModel, db: Session = Depends(get_db)):
    return await post_contact(body, db)


@router.put('/update/{contact_id}', response_model=ContactResponseModel)
async def update_contact(contact_id: int, body: ContactInputModel, db: Session = Depends(get_db)):
    return await put_contact(contact_id, body, db)


@router.delete('/del/{contact_id}', response_model=ContactResponseModel)
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await delete_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact
