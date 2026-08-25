from datetime import date
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, PositiveInt


class TransactionType(str, Enum):
    income = "income"
    expense = "expense"


class TransactionBase(BaseModel):
    title: str | None = None
    amount: PositiveInt
    type: TransactionType
    date: date
    category_id: PositiveInt


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):
    model_config = ConfigDict(from_attributes=True)

    id: PositiveInt


class TransactionListResponse(BaseModel):
    data: list[TransactionResponse]
    meta: dict[str, Any] = Field(default_factory=dict)
