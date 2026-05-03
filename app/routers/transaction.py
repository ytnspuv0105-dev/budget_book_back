from fastapi import APIRouter
from app.schemas.transaction import TransactionCreate

router = APIRouter()

# 👇 追加（メモリ保存）
transactions = [
    {
        "id": 1,
        "title": "ランチ",
        "amount": 1000,
        "type": "expense",
        "date": "2026-05-01",
        "category_id": 1
    },
    {
        "id": 2,
        "title": "給料",
        "amount": 300000,
        "type": "income",
        "date": "2026-05-01",
        "category_id": 1
    }
]

@router.get("/transactions")
def get_transactions():
    return {
        "data": transactions,
        "meta": {}
    }

@router.post("/transactions")
def create_transaction(data: TransactionCreate):
    new_id = len(transactions) + 1

    new_transaction = {
        "id": new_id,
        **data.dict()
    }

    transactions.append(new_transaction)

    return new_transaction

@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):
    global transactions

    transactions = [
        t for t in transactions if t["id"] != transaction_id
    ]

    return {"message": "deleted"}