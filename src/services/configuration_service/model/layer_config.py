from typing import Optional, List

from pydantic import BaseModel

from src.services.configuration_service.model.controller_change_config import ControllerChangeConfig
from src.services.configuration_service.model.note_range_config import NoteRangeConfig
from src.services.configuration_service.model.velocity_range_config import VelocityRangeConfig

ANY_PROGRAM = -1


class LayerConfig(BaseModel):
    number: int
    active: bool
    channel: int
    note_range_config: NoteRangeConfig
    velocity_range_config: VelocityRangeConfig
    controller_changes: List[ControllerChangeConfig] = []
    program: Optional[int] = ANY_PROGRAM
    octave: Optional[int] = 0
    transportation: Optional[int] = 0
    fix_velocity: Optional[int] = None
    keep_note_on_until_touch_it_again: Optional[bool] = False
