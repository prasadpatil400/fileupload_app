from fastapi import Form, File, UploadFile, Request, FastAPI, Depends
from typing import List
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
# from typing import Optional, List
#from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import requests
from flask import Flask, session
import tempfile
import os
from apps import database, pre_designed_urls, schemas, model, crud
basepath='/Users/hash/'

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
    data = (await file.read()).decode("utf-8")
    path = basepath+file.filename
    f = open(path, "a")
    f.write(data)
    f.close()
    URL = pre_designed_urls.generate(file.filename,basepath)
    print("********",URL)
    received_data = base.dict()
    print(received_data)
    return crud.upload(db=db, user=base, file=URL)


#@app.get("/", response_class=HTMLResponse)
#def main(request: Request):
 #   return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/login")
# async def login(user: schemas.UserCreate):
#     email=user.email
#     password=user.password
#     return {"email":email, "passord":password}
