from fastapi import FastAPI , Depends

from database import Base , engine , get_db

from models import Task
from sqlalchemy.orm import Session


from schemas import TaskSchema


# ocnnects to neon and checks the tasks table exists , if not then create it 
Base.metadata.create_all(bind = engine )

# here base contains all database table definatn 
# and engine , contains the cloud databse connection 

app= FastAPI()

# home api 
@app.get("/")
def home():
    return{"message":"Welcome to Cloud Task Manager API"}

# this api tells that : Fastapi is running and the application started successfully 

# now run the project using uvicorn main:app --reload 

# as per day_2
@app.post("/create_task")
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    # create a new task object
    new_task = Task(
        task_title=task.task_title,
        description=task.description,
        assigned_to=task.assigned_to,
        priority=task.priority,
        status=task.status,
        due_date=task.due_date,
        created_by=task.created_by
    )
    # add the new task to the database
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Task created successfully"}

#  use the data sent from postman is first validates by the TaskSchema (pydantic schemas) , if it is valid , the values 
# are then copied into the task model , which represnt the database table and finally stored in the databse   

@app.get("/tasks")
def get_task(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    return{"message": tasks}
