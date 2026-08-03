from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False, unique=True)

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    transactions = relationship(
        "Transaction",
        back_populates="category"
    )