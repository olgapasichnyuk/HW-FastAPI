from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.routes import contacts_crud, birthdays, contacts_search

app = FastAPI()


@app.get('/')
async def root():
    return {'massage': 'Main page Contacts'}


@app.get('/api/healthchecker')
def healthchecker(db: Session = Depends(get_db)):
    try:
        res = db.execute(text('SELECT 1')).fetchone()
        if res is None:
            raise HTTPException(status_code=500, detail='DB configured not correctly')
        return {'massage': 'Welcome to FastAPI'}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail='Error connecting to the DB')


app.include_router(contacts_crud.router)
app.include_router(contacts_search.router)
app.include_router(birthdays.router)
