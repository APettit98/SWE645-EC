from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def getDB():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/api/surveys", response_model=list[schemas.Survey])
def create_survey(surveys:list[schemas.SurveyCreate], db:Session=Depends(getDB)):
    return crud.createSurveys(db, surveys)

@app.get("/api/surveys", response_model=list[schemas.Survey])
def get_surveys(db:Session=Depends(getDB)):
    return crud.getSurveys(db)

