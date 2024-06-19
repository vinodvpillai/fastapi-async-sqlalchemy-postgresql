from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Article(Base):
    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(index=True)
    content: Mapped[str] = mapped_column(index=True)
    temp: Mapped[str] = mapped_column(nullable=True)