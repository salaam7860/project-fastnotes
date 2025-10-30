from pydantic import BaseModel, ConfigDict, Field





# SHARED BASE
class NotesBase(BaseModel):
    title:     str         = Field(description="Title of the note")
    content:   str         = Field(description="Content of the note")

# NOTE CREATION 
class NoteCreate(NotesBase):
    pass

# READ AND UPDATE
class NoteUpdate(NotesBase):
    pass

# PARTIAL UPDATE
class NoteParialUpdate(BaseModel):
    title:     str | None  = Field(default=None, description="Title of the note and default value is None")
    content:   str | None  = Field(default=None, description="Content of the note and default value is None")

# RETURN VALUE -- OUTPUT
class NoteOut(NotesBase):
    id:         int
    model_config            = ConfigDict(from_attributes=True)




