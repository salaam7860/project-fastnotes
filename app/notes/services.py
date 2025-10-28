from app.db.config import async_session
from app.notes.models import Note

from sqlalchemy import select

from fastapi import HTTPException, status



# NOTE NOT FOUND 
def note_not_found(note):
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not Found"
        )




# CREATE NOTE
async def create_notes(title: str, content:str):
    async with async_session() as session:

        note = Note(title=title, content=content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note


# GET NOTE 
async def get_note(note_id: int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        note_not_found(note)
        return  note
    
   

# GET ALL NOTES
async def get_all_notes():
    async with async_session() as session:
        stmt= select(Note)
        note = await session.scalars(stmt)
        note_not_found(note)
        return note.all()

# UPDATE THE NOTE
async def update_note(note_id: int, new_title: str, new_content: str):
    async with async_session() as session:
        note  = await session.get(Note, note_id)
        note_not_found(note)
        note.title = new_title
        note.content  = new_content
        await session.commit()
        await session.refresh(note)
        return note

# UPDATE SINGLE ENTRY
async def patch_note(note_id: int, new_title: str | None = None, new_content: str | None = None):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        note_not_found(note)

        # PATCHES
        if new_title is not None:
            note.title = new_title
        if new_content is not None:
            note.content = new_content

        await session.commit()
        await session.refresh(note)
        return note
    

# DELETE SINGLE NOTE
async def delete_note(note_id: int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        note_not_found(note)

        await session.delete(note)
        await session.commit()
        
        return {"message": "DELETED"}




