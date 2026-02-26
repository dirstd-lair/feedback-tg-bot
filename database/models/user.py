from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, Integer
from datetime import datetime
from .base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now)
