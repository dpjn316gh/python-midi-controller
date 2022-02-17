from abc import ABC, abstractmethod
from typing import List

from services.configuration_service.model.controller_config import ControllerConfig
from services.configuration_service.model.performance_config import PerformanceConfig
from services.midi_interface_service.model.midi_ports import MidiPorts


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
    def set_current_performance_by_number(self, number: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_current_performance(self,
                                controller_config: ControllerConfig) -> PerformanceConfig:
        raise NotImplementedError

    @abstractmethod
    def list_input_ports(self):
        raise NotImplementedError

    @abstractmethod
    def list_output_ports(self):
        raise NotImplementedError

    @abstractmethod
    def set_midi_ports(self, midi_ports: MidiPorts):
        raise NotImplementedError

    @abstractmethod
    def get_midi_ports(self) -> MidiPorts:
        raise NotImplementedError


