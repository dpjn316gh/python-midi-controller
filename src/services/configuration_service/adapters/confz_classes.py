from typing import List, Optional

from confz import ConfZ

ANY_PROGRAM = -1


class ControllerChangeConfigConfZ(ConfZ):
    continues_controller: str
    min: Optional[int] = 0
    max: Optional[int] = 127
    use_global_channel: Optional[bool] = False


class NoteRangeConfigConfZ(ConfZ):
    upper_key: str
    lower_key: str


class TempoRangeConfigConfZ(ConfZ):
    min_bpm: int
    max_bpm: int


class TimeSignatureConfZ(ConfZ):
    beats_per_bar: int
    beat_unit: int


class VelocityRangeConfigConfZ(ConfZ):
    max_velocity: int
    min_velocity: int


class LayerConfigConfZ(ConfZ):
    number: int
    active: bool
    channel: int
    note_range_config: NoteRangeConfigConfZ
    velocity_range_config: VelocityRangeConfigConfZ
    controller_changes: List[ControllerChangeConfigConfZ] = []
    program: Optional[int] = ANY_PROGRAM
    octave: Optional[int] = 0
    transportation: Optional[int] = 0
    fix_velocity: Optional[int] = None
    keep_note_on_until_touch_it_again: Optional[bool] = False


class PerformanceConfigConfZ(ConfZ):
    number: int
    name: str
    tempo_config: TempoRangeConfigConfZ
    time_signature: TimeSignatureConfZ
    layers: List[LayerConfigConfZ]
