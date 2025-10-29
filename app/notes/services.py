from app.db.config import async_session
from app.notes.models import Notes
from app.notes.schemas import *

from sqlalchemy import select

from fastapi  import HTTPException, status

from typing import List


# VALIDATION 
def note_not_found(note):
    if note is None: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NOT FOUND"
        )



# CREATE NOTE
async def create_note(new_note: NoteCreate) -> NoteOut:
    async with async_session() as session:
        note = Notes(title= new_note.title, content=new_note.content)
        session.add(note)
        await session.commit()
        await session.refresh(note)

        return note


# GET ALL NOTES
async def get_all_notes() -> List[NoteOut]: 
    async with async_session() as session:
        stmt  = select(Notes)
        note = await session.scalars(stmt)
        note_not_found(note)
        return note.all()


# GET SINGLE NOTE
async def get_single_note(id: int) -> NoteOut:
    async with async_session() as session:
        note = await session.get(Notes, id)
        note_not_found(note)
        return note

# UPDATE COMPLETELY
async def update_completely(id: int, new_note: NoteUpdate) -> NoteOut:
    async with async_session() as session:
        note = await session.get(Notes, id)
        note_not_found(note)
        note.title = new_note.title
        note.content = new_note.content
        await session.commit()
        await session.refresh(note)

        return note

# UPDATE PATIALLY 
async def update_partially(id: int, new_note: NotePatch) -> NoteOut:
    async with async_session() as session:
        note = await session.get(Notes, id)
        note_not_found(note)
        if new_note.title is not None: 
            note.title = new_note.title
        if new_note.content is not None: 
            note.content = new_note.content
        await session.commit()
        await session.refresh(note)
        return note


# DELETE NOTE
async def delete_note(id: int):
    async with async_session() as session:
        note = await session.get(Notes, id)
        note_not_found(note)
        await session.delete(note)
        await session.commit()

        return {"message":"DELETED"}

















