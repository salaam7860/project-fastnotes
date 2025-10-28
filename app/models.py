from pydantic import BaseModel, Field




class CreateNote(BaseModel):

    title: str = Field(min_length=3, description="Title of the note")
    content: str = Field(min_length=3, description="Content of the note")
    