import os
from pathlib import Path

from confz.confz_source import ConfZFileSource
from model.configuration.configuration_constants import CONFIG_FOLDER
from model.configuration.controller_config import ControllerConfig
from model.configuration.performance_config import PerformanceConfig


def load_performances_config():
    # TODO SINGLETON
    performances_config = []
    for file in os.listdir(os.path.join(CONFIG_FOLDER, ControllerConfig().performance_folder)):
        if file.endswith("yml") or file.endswith("yaml"):
            performance_config_file_path = os.path.join(CONFIG_FOLDER,  ControllerConfig().performance_folder, file)  
            performances_config.append(PerformanceConfig(config_sources=ConfZFileSource(file=Path(performance_config_file_path))))
    return performances_config