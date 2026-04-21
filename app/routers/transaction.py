from fastapi import APIRouter
from app.schemas.transaction import TransactionCreate

router = APIRouter()

@router.get("/transactions")

def get_transactions():
    return {
        "data": [
            {
                "id": 1,
                "title": "ランチ",
                "amount": 1000,
                "type": "expense"
            },
            {
                "id": 2,
                "title": "給料",
                "amount": 300000,
                "type": "income"
            }
        ],
        "meta": {}
    }

@router.post("/transactions")
def create_transaction(data: TransactionCreate):
    return data