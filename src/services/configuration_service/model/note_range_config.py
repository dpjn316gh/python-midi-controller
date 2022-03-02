from pydantic import BaseModel


class NoteRangeConfig(BaseModel):
    upper_key: str
    lower_key: str
