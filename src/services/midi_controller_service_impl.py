from typing import List

from services.configuration_service.model.controller_config import ControllerConfig
from services.configuration_service.model.performance_config import PerformanceConfig
from services.configuration_service.service import ConfigurationService
from services.midi_controller_service import MidiControllerService
from services.midi_interface_service.model.midi_ports import MidiPorts
from services.midi_interface_service.ports.service import MidiInterfaceService


class MidiControllerServiceImpl(MidiControllerService):
    controller_config: ControllerConfig
    performances_config: List[PerformanceConfig] = None
    current_performance: PerformanceConfig = None
    midi_ports: MidiPorts = MidiPorts()

    def __init__(self,
                 configuration_service: ConfigurationService,
                 midi_interface_service: MidiInterfaceService):
        self.configuration_service = configuration_service
        self.midi_interface_service = midi_interface_service

    def start_service(self) -> None:
        self.controller_config = self.configuration_service.get_controller_config()

    def get_controller_config(self) -> ControllerConfig:
        return self.controller_config

    def get_performances_config(self,
                                controller_config: ControllerConfig,
                                reload_from_disk: bool = False) -> List[PerformanceConfig]:
        if self.performances_config is None or reload_from_disk:
            self.performances_config = self.configuration_service.get_performances_config(controller_config)
        return self.performances_config

    def set_current_performance_by_number(self, number: int) -> None:
        if self.performances_config is not None:
            result = [pc for pc in self.performances_config if pc.number == number]
            if len(result) > 0:
                self.current_performance = result[0]

    def get_current_performance(self,
                                controller_config: ControllerConfig) -> PerformanceConfig:
        if self.current_performance is not None:
            return self.current_performance
        else:
            self.get_performances_config(controller_config)
            result = [pc for pc in self.performances_config if pc.number == controller_config.default_performance]
            if len(result) > 0:
                self.current_performance = result[0]
                return self.current_performance
            raise ValueError("Current performance not found")

    def list_input_ports(self):
        return self.midi_interface_service.list_input_ports()

    def list_output_ports(self):
        return self.midi_interface_service.list_output_ports()

    def set_midi_ports(self, midi_ports: MidiPorts):
        self.midi_ports = midi_ports

    def get_midi_ports(self) -> MidiPorts:
        return self.midi_ports
