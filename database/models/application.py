from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BigInteger, DateTime
from datetime import datetime
from .base import Base

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    author_id: Mapped[int] = mapped_column(BigInteger())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now)

