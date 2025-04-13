from pydantic import BaseModel

class SurveyBase(BaseModel):
    first_name: str 
    last_name: str
    address: str
    city: str
    state: str
    zip_code: int
    phone_number: str
    email: str
    date: str
    campus_preferences: str
    university_interest: str
    recommend: str

class SurveyCreate(SurveyBase):
    pass

class Survey(SurveyBase):
    id: int