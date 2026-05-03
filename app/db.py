from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://yuki@localhost/budget_app"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)