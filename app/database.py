from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

DATABASE = {
    'drivername': 'mysql+mysqldb',
    'username': 'admin',
    'password': 'GoScots2020!',
    'host': 'swe645-hw3-mysql.c7uckauqk7sl.us-east-1.rds.amazonaws.com',
    'port': 3306,
    'database': 'swe645'
}
DB_URL = URL.create(**DATABASE)
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()