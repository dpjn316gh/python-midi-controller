from typing import List

from services.configuration_service.model.controller_config import ControllerConfig
from services.configuration_service.model.performance_config import PerformanceConfig
from services.configuration_service.ports.controller_config_service import ControllerConfigService
from services.configuration_service.service import ConfigurationService


class ConfigurationServiceImpl(ConfigurationService):

    def __init__(self,
                 controller_confi_service: ControllerConfigService):
        self.controller_confi_service = controller_confi_service

    def get_controller_config(self) -> ControllerConfig:
        return self.controller_confi_service.get_controller_config()

    def get_performances_config(self, controller_config: ControllerConfig) -> List[PerformanceConfig]:
        return self.controller_confi_service.get_performances_config(controller_config)
