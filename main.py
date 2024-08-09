from fastapi import FastAPI, HTTPException, status, Depends
from schemas import Todo
from typing import List
import models
from database import engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

todo_list : List[Todo] = []
current_id = 1


@app.post("/todo/", response_model= Todo, status_code=status.HTTP_201_CREATED)
def create_task(request : Todo, db: Session = Depends(get_db)):
    new_task = models.Todo(title = request.title, description = request.description, completed = request.completed)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/todo/", status_code= status.HTTP_200_OK)
def get_all_task(db: Session = Depends(get_db)):
    tasks = db.query(models.Todo).all()
    return tasks

@app.get("/todo/{id}")
def task_by_id(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Todo).filter(models.Todo.id == id).first()
    if task:
        return task
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"Task with ID {id} not found")

@app.put("/todo/{id}", response_model=Todo)
def update_task(id: int, todo: Todo):
    for index, task in enumerate(todo_list):
        if task.id == id:
            todo.id = id
            todo_list[index] = todo
            return todo
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"Task with ID {id} not found")

@app.delete("/todo/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_task(id: int, db: Session = Depends(get_db)):
    db.query(models.Todo).filter(models.Todo.id == id).delete(synchronize_session=False)
    db.commit()
    return f"Task with ID {id} deleted successfully"
    # raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"Task with ID {id} not found")
