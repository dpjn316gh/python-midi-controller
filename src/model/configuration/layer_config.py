from typing import Optional
from confz.confz import ConfZ

from model.configuration.note_range_config import NoteRangeConfig
from model.configuration.velocity_range_config import VelocityRangeConfig


class LayerConfig(ConfZ):
    number: int
    active: bool
    channel: int
    note_range_config: NoteRangeConfig
    velocity_range_config: VelocityRangeConfig
    octave: Optional[int] = 0
    transportation: Optional[int] = 0
    fix_velocity: Optional[int] = 100
