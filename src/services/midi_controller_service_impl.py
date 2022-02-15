from typing import List

from services.configuration_service.model.controller_config import ControllerConfig
from services.configuration_service.model.performance_config import PerformanceConfig
from services.configuration_service.service import ConfigurationService
from services.midi_controller_service import MidiControllerService


class MidiControllerServiceImpl(MidiControllerService):
    controller_config: ControllerConfig
    performances_config: List[PerformanceConfig] = None
    current_performance: PerformanceConfig = None

    def __init__(self,
                 configuration_service: ConfigurationService):
        self.configuration_service = configuration_service

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

    def set_current_performance_by_number_and_name(self, number: int) -> None:
        if self.performances_config is not None:
            result = [pc for pc in self.performances_config if pc.number == number]
            if len(result) > 0:
                self.current_performance = result[0]
