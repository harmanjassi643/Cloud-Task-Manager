# import reqiured sql col 
from sqlalchemy import Column , Integer , String

from database import Base

class Task(Base):
    # table name 
    __tablename__ = "tasks"

    # primary key 
    id = Column(Integer , primary_key= True)

    # task titel 
    task_title = Column(String, nullable= False)

    description = Column(String)

    assigned_to = Column(String)

    priority = Column(String)

    status = Column(String)

    due_date = Column(String)

    created_by = Column(String)

    # this file just defines the structure of the database table , it does not create the table in the database . the tbale will be created when we Run the main file 
