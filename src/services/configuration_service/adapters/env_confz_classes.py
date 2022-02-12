import os
from pathlib import Path

from confz import ConfZ, ConfZFileSource
from pydantic import BaseSettings


class GlobalSettings(BaseSettings):
    CONFIG_FOLDER: str = ""


global_settings = GlobalSettings()


class ControllerConfigConfZ(ConfZ):
    performance_folder: str
    default_performance: int

    if global_settings.CONFIG_FOLDER:
        CONFIG_SOURCES = ConfZFileSource(file=Path(os.path.join(global_settings.CONFIG_FOLDER, 'controller.yml')))
    else:
        raise FileNotFoundError("Must declare and assign a path for CONFIG_FOLDER env variable")

    def get_config_folder(sefl) -> str:
        return global_settings.CONFIG_FOLDER
