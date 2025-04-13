from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Survey(Base):
    __tablename__ = "surveys"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip_code = Column(Integer)
    phone_number = Column(String(255))
    email = Column(String(255))
    date = Column(String(255))
    campus_preferences = Column(String(255))
    university_interest = Column(String(255))
    recommend = Column(String(255))