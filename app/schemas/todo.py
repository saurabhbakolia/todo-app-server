from datetime import date
from typing import Literal

from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    priority: Literal["high", "medium", "low"] | None = None
    due_date: date | None = None


class TodoUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None
    priority: Literal["high", "medium", "low"] | None = None
    due_date: date | None = None
