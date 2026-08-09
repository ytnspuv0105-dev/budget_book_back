from fastapi import APIRouter, Depends
from app.schemas.transaction import TransactionCreate
from app.models.transaction import Transaction
from app.db import get_db
from sqlalchemy.orm import Session
import traceback

router = APIRouter()


# 🥇 GET（一覧取得）
@router.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    try:
        transactions = db.query(Transaction).all()

        return {
            "data": [
                {
                    "id": t.id,
                    "title": t.title,
                    "amount": t.amount,
                    "type": t.type,
                    "date": t.date,
                    "category_id": t.category_id,
                }
                for t in transactions
            ],
            "meta": {},
        }
    except Exception:
        print(traceback.format_exc())
        raise

# 🥈 POST（作成）
@router.post("/transactions")
def create_transaction(
    data: TransactionCreate,
    db: Session = Depends(get_db)
):
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

    return new_transaction

# 🥉 PUT（更新）
@router.put("/transactions/{transaction_id}")
def update_transaction(
    transaction_id: int,
    data: TransactionCreate,
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return {"error": "not found"}

    transaction.title = data.title
    transaction.amount = data.amount
    transaction.type = data.type
    transaction.date = data.date
    transaction.category_id = data.category_id

    db.commit()

    return {"message": "updated"}

# 🏁 DELETE（削除）
@router.delete("/transactions/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction:
        db.delete(transaction)
        db.commit()

    return {"message": "deleted"}