from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
import exceptions
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
    try:
        surveys = crud.createSurveys(db, surveys)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return surveys

@app.get("/api/surveys", response_model=list[schemas.Survey])
def get_surveys(db:Session=Depends(getDB)):
    try:
        surveys = crud.getSurveys(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return surveys

@app.get("/api/surveys/{survey_id}")
def get_survey_by_id(survey_id:int, db:Session=Depends(getDB)):
    try:
        survey = crud.getSurveysById(db, survey_id)
    except exceptions.SurveyNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return survey

@app.delete("/api/surveys/{survey_id}")
def delete_survey_by_id(survey_id:int, db:Session=Depends(getDB)):
    try:
        res = crud.delete_survey_by_id(db, survey_id)
    except exceptions.SurveyNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return "Success"

@app.put("/api/surveys/{survey_id}")
def update_survey_by_id(survey:schemas.SurveyCreate, survey_id:int, db:Session=Depends(getDB)):
    try:
        updated_survey = crud.update_survey_by_id(db, survey_id, survey)
    except exceptions.SurveyNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return updated_survey

