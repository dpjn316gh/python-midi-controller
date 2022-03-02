from pydantic import BaseModel


class VelocityRangeConfig(BaseModel):
    max_velocity: int
    min_velocity: int
