from sqlmodel import create_engine, SQLModel
from models import User  # Imports models to register them

sqlite_url = "sqlite:///./trade_finance.db"
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)