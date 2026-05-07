from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    ForeignKey,
    func,
    CheckConstraint,
    Text
)

from sqlalchemy.orm import relationship

from app.db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    __table_args__ = (
        CheckConstraint(
            "type IN ('income', 'expense')",
            name="check_transaction_type"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Integer, nullable=False)

    type = Column(String, nullable=False)

    date = Column(Date, nullable=False, index=True),

    memo = Column(Text, nullable=True)

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=True,
        index=True
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    category = relationship(
        "Category",
        back_populates="transactions"
    )