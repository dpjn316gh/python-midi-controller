from abc import ABC, abstractmethod

from src.services.configuration_service.model.controller_config import ControllerConfig


class MidiControllerService(ABC):

    @abstractmethod
    def start_service(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_controller_config(self) -> ControllerConfig:
        raise NotImplementedError


