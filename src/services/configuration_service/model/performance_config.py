from typing import List

from pydantic import BaseModel

from services.configuration_service.model.layer_config import LayerConfig
from services.configuration_service.model.tempo_range_config import TempoRangeConfig
from services.configuration_service.model.time_signature import TimeSignature


class PerformanceConfig(BaseModel):
    number: int
    name: str
    tempo_config: TempoRangeConfig
    time_signature: TimeSignature
    layers: List[LayerConfig]
