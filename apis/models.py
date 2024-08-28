from sqlalchemy import Column, Integer, JSON
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)  # PostgreSQL에서는 JSONB로 자동 변환됩니다.