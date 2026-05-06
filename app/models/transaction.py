from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, func, Index
from app.db import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)

    type = Column(String, nullable=False)

    date = Column(Date, nullable=False)  # ← String → Date

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        Index("ix_transactions_date", "date"),
        Index("ix_transactions_category_id", "category_id"),
    )