from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.notes import services as note_service
#from models import CreateNote




app  = FastAPI()



@app.post("/notes")
async def notes_create(data: dict):
    note = await note_service.create_notes(data["title"], data["content"])
    return note



@app.get("/notes/{note_id}")
async def single_note_get(note_id: int):
    note = await note_service.get_note(note_id)
    return note


@app.get("/notes")
async def note_get():
    note = await note_service.get_all_notes()
    return note


@app.put("/notes/{note_id}")
async def note_update(note_id: int, new_note: dict):
    new_title = new_note.get("title")
    new_content = new_note.get("content")

    note = await note_service.update_note(note_id, new_title, new_content)

    return note


@app.patch("/notes/{note_id}")
async def note_single_update(note_id: int, new_note: dict):
    new_title = new_note.get('title')
    new_content = new_note.get('content')

    note = await note_service.update_note(note_id, new_title, new_content)

    return note


@app.delete("/delete/{note_id}")
async def note_delete(note_id: int):
    response = await note_service.delete_note(note_id)
    return response






























# BACKEND CONFIGS
@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar_api"
    )
