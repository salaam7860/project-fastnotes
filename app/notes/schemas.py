from pydantic import BaseModel, ConfigDict, Field




# SHARED BASE FIELD 
class NoteBase(BaseModel):
    title: str = Field(description="Title of Notes")
    content: str = Field(description="content of Notes")


# NOTE CREATION 
class NoteCreate(NoteBase):
    pass


# NOTE UPDATE
class NoteUpdate(NoteBase):
    pass

# NOTE PARTIAL UPDATE
class NotePatch(BaseModel):
   
    title: str | None = Field(default=None, description="Title of Notes")
    content: str | None = Field(default=None, description="content of Notes")


# NOTE RESPONSE SERIALIZATION 
class NoteOut(NoteBase):
    id : int
    model_config = ConfigDict(from_attributes=True)