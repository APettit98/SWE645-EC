from sqlalchemy.orm import Session

import models
import schemas

def getSurveys(db: Session):
    return db.query(models.Survey).all()

def getSurveysById(db: Session, id: int):
    return db.query(models.Survey).filter(models.Survey.id == id).first()

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
    res = db.query(models.Survey).filter(models.Survey.id == id).delete()
    db.commit()
    return res

def update_survey_by_id(db: Session, id: int, survey: schemas.SurveyCreate):
    db.query(models.Survey).filter(models.Survey.id == id).update(
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
    db.commit()
    return survey
