from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs



class Base(DeclarativeBase, AsyncAttrs):
    pass

from app.notes import models as note_models