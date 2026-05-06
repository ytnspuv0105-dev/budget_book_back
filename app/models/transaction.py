from sqlalchemy import Column, Integer, String
from app.db import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Integer)
    type = Column(String)
    date = Column(String)
    category_id = Column(Integer)
