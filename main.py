from fastapi import FastAPI, HTTPException, status
from schemas import Todo
from typing import List

app = FastAPI()

todo_list : List[Todo] = []
current_id = 1


@app.post("/todo/", response_model= Todo)
def create_task(todo : Todo):
    global current_id
    todo.id = current_id
    current_id += 1
    todo_list.append(todo)
    return todo

@app.get("/todo/", response_model=List[Todo])
def get_all_task():
    return todo_list

@app.get("/todo/{id}", response_model=Todo)
def task_by_id(id: int):
    for task in todo_list:
        if task.id == id:
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

@app.delete("/todo/{id}")
def delete_task(id: int):
    for index, task in enumerate(todo_list):
        if task.id == id:
            todo_list.pop(index)
            return f"Task with ID {id} deleted Successfully"
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"Task with ID {id} not found")