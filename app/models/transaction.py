from sqlalchemy import Column, Integer, String
from app.db import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Integer)
    type = Column(String)
    date = Column(String)
    category_id = Column(Integer)

# テーブル作成
Base.metadata.create_all(bind=engine)