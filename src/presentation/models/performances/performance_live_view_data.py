from typing import Optional, List

from pydantic import BaseModel

ANY_PROGRAM = -1


class TempoRangeConfigViewData(BaseModel):
    min_bpm: int
    max_bpm: int


class TimeSignatureViewData(BaseModel):
    beats_per_bar: int
    beat_unit: int


class NoteRangeConfigViewData(BaseModel):
    upper_key: str
    lower_key: str


class VelocityRangeConfigViewData(BaseModel):
    max_velocity: int
    min_velocity: int


class ControllerChangeConfigViewData(BaseModel):
    continues_controller: str
    min: Optional[int] = 0
    max: Optional[int] = 127
    use_global_channel: Optional[bool] = False


class LayerConfigViewData(BaseModel):
    number: int
    active: bool
    channel: int
    note_range_config: NoteRangeConfigViewData
    velocity_range_config: VelocityRangeConfigViewData
    controller_changes: List[ControllerChangeConfigViewData] = []
    program: Optional[int] = ANY_PROGRAM
    octave: Optional[int] = 0
    transportation: Optional[int] = 0
    fix_velocity: Optional[int] = None
    keep_note_on_until_touch_it_again: Optional[bool] = False


class PerformanceLiveViewData(BaseModel):
    number: int
    name: str
    tempo_config: TempoRangeConfigViewData
    time_signature: TimeSignatureViewData
    layers: List[LayerConfigViewData]
