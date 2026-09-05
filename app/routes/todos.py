from fastapi import APIRouter, HTTPException, responses
from pydantic import HttpUrl

from app.database import supabase
from app.schemas.todo import TodoCreate, TodoUpdate

router = APIRouter(
    prefix="/api/todos",
    tags=["Todos"],
)


@router.post("/")
def create_todo(todo: TodoCreate):
    response = (
        supabase.table("todos")
        .insert(
            {
                "title": todo.title,
                "priority": todo.priority,
                "due_date": todo.due_date.isoformat() if todo.due_date else None,
            }
        )
        .execute()
    )

    return response.data[0]


@router.get("/")
def get_todos():
    response = supabase.table("todos").select("").execute()
    return response.data


@router.get("/{todo_id}")
def get_todo(todo_id: int):
    response = supabase.table("todos").select("*").eq("id", todo_id).execute()

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Todo not found",
        )
    return response.data[0]


@router.put("/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate):
    update_data = todo.model_dump(exclude_unset=True)

    if "due_date" in update_data and update_data["due_date"]:
        update_data["due_date"] = update_data["due_date"].isoformat()

    response = supabase.table("todos").update(update_data).eq("id", todo_id).execute()

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Todo not found",
        )
    return response.data[0]


@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    response = supabase.table("todos").delete().eq("id", todo_id).execute()

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Todo not found",
        )

    return {
        "message": "Todo deleted successfully",
        "todo": response.data[0],
    }
