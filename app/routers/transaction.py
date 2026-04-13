from fastapi import APIRouter
from app.schemas.transaction import TransactionCreate

router = APIRouter()

@router.get("/transactions")
def get_transactions():
    return {
        "data": [],
        "meta": {}
    }

@router.post("/transactions")
def create_transaction(data: TransactionCreate):
    return data