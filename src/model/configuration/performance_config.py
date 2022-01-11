from confz.confz import ConfZ
from model.tempo.tempo_range import TempoRangeConfig
from model.tempo.time_signature import TimeSignature


class PerformanceConfig(ConfZ):
    number: int
    name: str
    tempo_config: TempoRangeConfig
    time_signature: TimeSignature
