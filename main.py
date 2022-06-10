from fastapi import Form, File, UploadFile, Request, FastAPI, Depends
from typing import List
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
# from typing import Optional, List
#from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from flask import Flask, session
import tempfile
from apps import database, pre_designed_urls, schemas, model, crud

engine = database.engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#templates = Jinja2Templates(directory="templates")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/upload")
async def upload(base: schemas.Base = Depends(), file: UploadFile = File(...), db: session = Depends(get_db)):
    finename = pre_designed_urls.generate(file.filename)
    temp = file.filename
    print(temp)
    with open(temp,'r') as p:
        p.read()
        print(p.read())
    print("********",finename)
    received_data = base.dict()
    print(received_data)
    return crud.upload(db=db, user=base, file=finename)


#@app.get("/", response_class=HTMLResponse)
#def main(request: Request):
 #   return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/login")
# async def login(user: schemas.UserCreate):
#     email=user.email
#     password=user.password
#     return {"email":email, "passord":password}
