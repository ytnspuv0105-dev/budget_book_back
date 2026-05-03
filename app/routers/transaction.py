from fastapi import APIRouter
from app.schemas.transaction import TransactionCreate
from app.db import SessionLocal
from app.models.transaction import Transaction

router = APIRouter()


# 🥇 GET（一覧取得）
@router.get("/transactions")
def get_transactions():
    db = SessionLocal()

    transactions = db.query(Transaction).all()

    result = []
    for t in transactions:
        result.append({
            "id": t.id,
            "title": t.title,
            "amount": t.amount,
            "type": t.type,
            "date": t.date,
            "category_id": t.category_id,
        })

    db.close()

    return {"data": result, "meta": {}}


# 🥈 POST（作成）
@router.post("/transactions")
def create_transaction(data: TransactionCreate):
    db = SessionLocal()

    new_transaction = Transaction(
        title=data.title,
        amount=data.amount,
        type=data.type,
        date=data.date,
        category_id=data.category_id,
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    db.close()

    return {
        "id": new_transaction.id,
        "title": new_transaction.title,
        "amount": new_transaction.amount,
        "type": new_transaction.type,
        "date": new_transaction.date,
        "category_id": new_transaction.category_id,
    }


# 🥉 PUT（更新）
@router.put("/transactions/{transaction_id}")
def update_transaction(transaction_id: int, data: TransactionCreate):
    db = SessionLocal()

    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        db.close()
        return {"error": "not found"}

    transaction.title = data.title
    transaction.amount = data.amount
    transaction.type = data.type
    transaction.date = data.date
    transaction.category_id = data.category_id

    db.commit()

    db.close()

    return {"message": "updated"}


# 🏁 DELETE（削除）
@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):
    db = SessionLocal()

    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction:
        db.delete(transaction)
        db.commit()

    db.close()

    return {"message": "deleted"}