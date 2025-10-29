from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import List

from app.notes.schemas import NoteCreate,NoteUpdate,NotePatch,NoteOut
from app.notes import services as note_services 


app = FastAPI()



# CREATE NOTE
@app.post("/note", response_model=NoteOut)
async def note_create(new_note: NoteCreate) -> NoteOut:
    note = await note_services.create_note(new_note)
    return note

# GET ALL NOTES
@app.get("/note", response_model=List[NoteOut])
async def note_get():
    note = await note_services.get_all_notes()
    return note

# GET SINGLE NOTE 
@app.get("/note/{note_id}", response_model=NoteOut)
async def single_note_get(note_id: int) -> NoteOut:
    note = await note_services.get_single_note(note_id)
    return note

# UPDATE COMPLETELY 
@app.put("/note/{note_id}", response_model=NoteOut)
async def completely_update(note_id: int, new_note: NoteUpdate) -> NoteOut:
    # new_title = new_note.get("title")
    # new_content = new_note.get("content")

    note = await note_services.update_completely(note_id, new_note)
    return note

# UPDATE PARTIALLY
@app.patch("/note/{note_id", response_model=NoteOut)
async def partially_update(note_id, new_note: NotePatch) -> NoteOut:
    # new_title = new_note.get("title")
    # new_content = new_note.get("content")

    note = await note_services.update_partially(note_id, new_note)

    return note

# DELETE NOTE
@app.delete("/note/{note_id}")
async def note_delete(note_id:int):
    response = await note_services.delete_note(note_id)
    return response






















































# BACKEND CONGIF
@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url= app.openapi_url,
        title="Scalar_API"
    )