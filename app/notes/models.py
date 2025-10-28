from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text

from app.db.base import Base



class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(Text)

    def __repr__(self):
        return f"<id: {self.id}, title: {self.title}, content: {self.content}>"
    