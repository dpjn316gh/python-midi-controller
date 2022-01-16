from typing import List, Optional
from confz.confz import ConfZ
from model.configuration.controller_change_config import ControllerChange

from model.configuration.note_range_config import NoteRangeConfig
from model.configuration.velocity_range_config import VelocityRangeConfig


class LayerConfig(ConfZ):
    number: int
    active: bool
    channel: int
    note_range_config: NoteRangeConfig
    velocity_range_config: VelocityRangeConfig
    controller_changes: List[ControllerChange] = []
    octave: Optional[int] = 0
    transportation: Optional[int] = 0
    fix_velocity: Optional[int] = 100
    
