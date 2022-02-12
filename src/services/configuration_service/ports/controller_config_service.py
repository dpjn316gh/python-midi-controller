from abc import ABC, abstractmethod
from typing import List

from services.configuration_service.model.controller_config import ControllerConfig
from services.configuration_service.model.performance_config import PerformanceConfig


class ControllerConfigService(ABC):

    @abstractmethod
    def get_controller_config(self) -> ControllerConfig:
        raise NotImplementedError

    @abstractmethod
    def get_performances_config(self, controller_config: ControllerConfig) -> List[PerformanceConfig]:
        raise NotImplementedError

    @abstractmethod
    def get_performance_config(self, controller_config: ControllerConfig) -> PerformanceConfig:
        raise NotImplementedError

    @abstractmethod
    def save_performance_config(self, controller_config: ControllerConfig, performance_config: PerformanceConfig) -> None:
        raise NotImplementedError
