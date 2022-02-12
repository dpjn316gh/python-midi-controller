from pydantic import BaseModel


class TempoRangeConfig(BaseModel):
    min_bpm: int
    max_bpm: int
