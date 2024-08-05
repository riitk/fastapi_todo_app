# FastAPI To-Do List

A simple To-Do List API built with FastAPI. This project demonstrates the basic CRUD operations (Create, Read, Update, Delete) using FastAPI.

## Features

- Create a new to-do item
- Read all to-do items
- Read a single to-do item by ID
- Update a to-do item by ID
- Delete a to-do item by ID

## Getting Started

### Prerequisites

- Python 3.7+
- Git

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/fastapi-todo-app.git
    cd fastapi-todo-app
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    # Activate the virtual environment
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install fastapi uvicorn
    ```

### Running the Application

1. **Start the FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation.


## API Endpoints

### Create a To-Do

- **URL**: `/todos/`
- **Method**: `POST`
- **Body**:
    ```json
    {
      "title": "Learn FastAPI",
      "description": "Read the FastAPI documentation"
    }
    ```
- **Response**:
    ```json
    {
      "id": 1,
      "title": "Learn FastAPI",
      "description": "Read the FastAPI documentation",
      "completed": false,
      "due_date": null
    }
    ```

### Read All To-Dos

- **URL**: `/todos/`
- **Method**: `GET`
- **Response**:
    ```json
    [
      {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Read the FastAPI documentation",
        "completed": false,
        "due_date": null
      }
    ]
    ```

### Read a Single To-Do

- **URL**: `/todos/{todo_id}`
- **Method**: `GET`
- **Response**:
    ```json
    {
      "id": 1,
      "title": "Learn FastAPI",
      "description": "Read the FastAPI documentation",
      "completed": false,
      "due_date": null
    }
    ```

### Update a To-Do

- **URL**: `/todos/{todo_id}`
- **Method**: `PUT`
- **Body**:
    ```json
    {
      "title": "Learn FastAPI",
      "description": "Read the FastAPI documentation and build a project",
      "completed": true,
      "due_date": "2024-08-01"
    }
    ```
- **Response**:
    ```json
    {
      "id": 1,
      "title": "Learn FastAPI",
      "description": "Read the FastAPI documentation and build a project",
      "completed": true,
      "due_date": "2024-08-01"
    }
    ```

### Delete a To-Do

- **URL**: `/todos/{todo_id}`
- **Method**: `DELETE`
- **Response**:
    ```json
    {
      "id": 1,
      "title": "Learn FastAPI",
      "description": "Read the FastAPI documentation",
      "completed": false,
      "due_date": null
    }
    ```

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```bash
    git commit -m "Add some feature"
    ```
5. **Push to the branch**:
    ```bash
    git push origin feature-branch
    ```
6. **Create a new Pull Request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)

