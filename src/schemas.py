from datetime import date

from pydantic import BaseModel, Field, EmailStr



class ContactInputModel(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    surname: str = Field(min_length=2, max_length=15)
    email: EmailStr
    phone: str = Field()
    birthday: date


class ContactResponseModel(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    phone: str
    birthday: date

    class Config:
        orm_mode = True
