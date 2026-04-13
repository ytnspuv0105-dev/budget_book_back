from pydantic import BaseModel
from enum import Enum

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class TransactionCreate(BaseModel):
    title: str
    amount: int
    type: TransactionType
    date: str
    category_id: int