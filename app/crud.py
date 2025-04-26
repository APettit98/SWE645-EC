from sqlalchemy.orm import Session

import models
import schemas
import exceptions

def getSurveys(db: Session):
    return db.query(models.Survey).all()

def getSurveysById(db: Session, id: int):
    res = db.query(models.Survey).filter(models.Survey.id == id).first()
    if res is None:
        raise exceptions.SurveyNotFoundException(id)
    return res

def createSurveys(db: Session, surveys: list[schemas.SurveyCreate]):
    db_surveys = []
    for survey in surveys:
    
        db_survey = models.Survey(
            first_name=survey.first_name,
            last_name=survey.last_name,
            address=survey.address,
            city=survey.city,
            state=survey.state,
            zip_code=survey.zip_code,
            phone_number=survey.phone_number,
            email=survey.email,
            date=survey.date,
            campus_preferences=survey.campus_preferences,
            university_interest=survey.university_interest,
            recommend=survey.recommend
        )

        db.add(db_survey)
        db.commit()
        db.refresh(db_survey)
        db_surveys.append(db_survey)
    return db_surveys

def delete_survey_by_id(db: Session, id: int):
    db_survey = db.query(models.Survey).filter(models.Survey.id == id).one_or_none()
    if db_survey is None:
        raise exceptions.SurveyNotFoundException(id)
    res = db.delete(db_survey)
    db.commit()
    return res

def update_survey_by_id(db: Session, id: int, survey: schemas.SurveyCreate):
    db_survey = db.query(models.Survey).filter(models.Survey.id == id).one_or_none()
    if db_survey is None:
        raise exceptions.SurveyNotFoundException(id)
    
    for var, value in vars(survey).items():
        setattr(db_survey, var, value) if value else None

    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey
