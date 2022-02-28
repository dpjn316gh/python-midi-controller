from abc import ABC, abstractmethod
from typing import List

from midifilter.filters import MidiFilter
from services.configuration_service.model.performance_config import PerformanceConfig


class MidiFilterBuilderService(ABC):

    @abstractmethod
    def build_filters_from_performance(self, performance_config: PerformanceConfig) -> List[MidiFilter]:
        raise NotImplementedError
