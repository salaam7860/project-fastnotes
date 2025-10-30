from fastapi import HTTPException, status
from sqlalchemy import select

from app.notes.schemas import NoteCreate, NoteOut, NoteParialUpdate, NoteUpdate
from app.db.config import async_session
from app.notes.models import Notes
from sqlalchemy.ext.asyncio import AsyncSession




# VALIDATION CHECK
def note_not_found(note):
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="NOT FOUND"
        )

# NOTE CREATION 
async def create_note(session: AsyncSession, new_note: NoteCreate)-> NoteOut:
    
        note = Notes(title= new_note.title, content= new_note.content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note

# GET ALL NOTES
async def get_all_notes(session: AsyncSession) -> NoteOut:

        stmt = select(Notes)
        note = await session.scalars(stmt)
        return note.all()
    
# GET SINGLE NOTE
async def get_single_note(session: AsyncSession, id: int)->NoteOut:

        note = await session.get(Notes,id)
        note_not_found(note)
        return note

# UPDATE COMPLETELY
async def update_completely(session: AsyncSession, id: int, note_update: NoteUpdate)->NoteOut:

        note = await session.get(Notes, id)
        note_not_found(note)
        note.title = note_update.title
        note.content = note_update.content
        await session.commit()
        await session.refresh(note)
        return note

# UPDATE PARTIALLY
async def update_partially(session: AsyncSession, id: int, note_update: NoteParialUpdate)->NoteOut:

        note = await session.get(Notes, id)
        note_not_found(note)
        if note_update.title is not None:
            note.title = note_update.title
        if note_update.content is not None:
            note.content = note_update.content
        await session.commit()
        await session.refresh(note)
        return note

# DELETE NOTE 
async def delete_note(session: AsyncSession, id: int):

        note = await session.get(Notes, id)
        note_not_found(note)
        await session.delete(note)
        await session.commit()

        return {"message": "DELETED"}
