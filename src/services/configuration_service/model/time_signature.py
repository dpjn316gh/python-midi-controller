from pydantic import BaseModel


class TimeSignature(BaseModel):
    beats_per_bar: int
    beat_unit: int
