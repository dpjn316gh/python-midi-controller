from src.services.configuration_service.model.controller_config import ControllerConfig
from src.services.configuration_service.service import ConfigurationService
from src.services.midi_controller_service import MidiControllerService


class MidiControllerServiceImpl(MidiControllerService):
    controller_config: ControllerConfig

    def __init__(self,
                 configuration_service: ConfigurationService):
        self.configuration_service = configuration_service

    def start_service(self) -> None:
        self.controller_config = self.configuration_service.get_controller_config()

    def get_controller_config(self) -> ControllerConfig:
        return self.controller_config


