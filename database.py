# import create_engine to establish database connection
from sqlalchemy import create_engine

# import sessionmaker to create database session . orm(object relation maker)
from sqlalchemy.orm import sessionmaker

# import declarative_base to create models
from sqlalchemy.orm import declarative_base

# database connection string
DATABASE_URL= "postgresql://neondb_owner:npg_nib90ajXMIBo@ep-wild-term-ao8nlm0e-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
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