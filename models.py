from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Medicine(Base):
    
    __tablename__ = "medicines"
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(nullable=False)
    quantity : Mapped[int] = mapped_column(nullable=False)
    ndc : Mapped[str] = mapped_column(nullable=False, unique=True)
