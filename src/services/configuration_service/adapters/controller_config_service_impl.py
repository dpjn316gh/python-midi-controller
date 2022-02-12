import os
from pathlib import Path
from typing import List

from confz import ConfZFileSource

from src.services.configuration_service.adapters.confz_classes import PerformanceConfigConfZ
from src.services.configuration_service.adapters.env_confz_classes import ControllerConfigConfZ
from src.services.configuration_service.model.controller_config import ControllerConfig
from src.services.configuration_service.model.performance_config import PerformanceConfig
from src.services.configuration_service.ports.controller_config_service import ControllerConfigService


def controller_config_confz_to_controller_config(controller_config_confz: ControllerConfigConfZ) -> ControllerConfig:
    cc = controller_config_confz
    d = cc.dict()
    d.update({'config_folder': cc.get_config_folder()})
    d.update({'performances_folder_path': os.path.join(cc.get_config_folder(), cc.performance_folder)})
    return ControllerConfig(**d)


def performance_config_confz_to_performance_config(
        performance_config_confz: PerformanceConfigConfZ) -> PerformanceConfig:
    return PerformanceConfig(**performance_config_confz.dict())


class ControllerConfigServiceConfZ(ControllerConfigService):

    def get_controller_config(self) -> ControllerConfig:
        return controller_config_confz_to_controller_config(ControllerConfigConfZ())

    def get_performances_config(self, controller_config: ControllerConfig) -> List[PerformanceConfig]:

        performances_config_confz = []
        for file in os.listdir(os.path.join(controller_config.config_folder, controller_config.performance_folder)):
            if file.endswith("yml") or file.endswith("yaml"):
                performance_config_file_path = os.path.join(controller_config.config_folder,
                                                            controller_config.performance_folder, file)
                performances_config_confz.append(
                    PerformanceConfigConfZ(config_sources=ConfZFileSource(file=Path(performance_config_file_path))))
        return [performance_config_confz_to_performance_config(pcc) for pcc in performances_config_confz]

    def save_performance_config(self, controller_config: ControllerConfig,
                                performance_config: PerformanceConfig) -> None:
        raise NotImplementedError

    def get_performance_config(self, controller_config: ControllerConfig) -> PerformanceConfig:
        raise NotImplementedError
