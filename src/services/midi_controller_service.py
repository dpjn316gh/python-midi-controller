from abc import ABC, abstractmethod
from typing import List

from services.configuration_service.model.controller_config import ControllerConfig
from services.configuration_service.model.performance_config import PerformanceConfig


class MidiControllerService(ABC):

    @abstractmethod
    def start_service(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_controller_config(self) -> ControllerConfig:
        raise NotImplementedError

    @abstractmethod
    def get_performances_config(self,
                                controller_config: ControllerConfig,
                                reload_from_disk: bool) -> List[PerformanceConfig]:
        raise NotImplementedError

    @abstractmethod
    def set_current_performance_by_number_and_name(self, number: int) -> None:
        raise NotImplementedError
