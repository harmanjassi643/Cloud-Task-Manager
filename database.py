# import create_engine to establish database connection
from sqlalchemy import create_engine

# import sessionmaker to create database session . orm(object relation maker)
from sqlalchemy.orm import sessionmaker

# import declarative_base to create models
from sqlalchemy.orm import declarative_base

# as per day 2
import os
from dotenv import load_dotenv
load_dotenv()
# import the function that can read a .env , i.e open the .env and load all of its variables 
# into the memory 


# database connection string
DATABASE_URL= os.getenv("DATABASE_URL")
# we are connectiong to a postgresql for connectiong fastapi

# click the show password and copy the complete connection string 
# create sql engine sqlAlehmy
# the engine is responsible for connection 

# create database engine
engine = create_engine(DATABASE_URL)

# create sessions
SessionLocal = sessionmaker(bind = engine)

# create base class
Base  = declarative_base()

# dependency function
def get_db():

    # create database session
    db = SessionLocal()

    try:

        # use database session
        yield db

    finally:
        # close database session
        db.close()