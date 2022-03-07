from abc import ABC, abstractmethod
from typing import List, Callable

from midifilter.filters import MidiFilter
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
    def get_filters_for_current_performance(self) -> List[MidiFilter]:
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

    @abstractmethod
    def open_midi_ports(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def close_midi_ports(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def run_controller(self,
                       on_midi_in_event_callback: Callable[[str], None],
                       on_midi_out_event_callback: Callable[[str], None]
                       ) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop_controller(self) -> None:
        raise NotImplementedError
