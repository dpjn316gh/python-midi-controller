from abc import ABC, abstractmethod
from typing import List

from services.configuration_service.model.controller_config import ControllerConfig
from services.configuration_service.model.performance_config import PerformanceConfig


class ConfigurationService(ABC):

    @abstractmethod
    def get_controller_config(self) -> ControllerConfig:
        raise NotImplementedError

    @abstractmethod
    def get_performances_config(self, controller_config: ControllerConfig) -> List[PerformanceConfig]:
        raise NotImplementedError
