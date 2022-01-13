from pathlib import Path

from confz import ConfZ
from confz.confz_source import ConfZFileSource
from model.configuration.configuration_constants import CONTROLLER_CONFIG_FILE


class ControllerConfig(ConfZ):
    performance_folder: str
    default_performance: int

    CONFIG_SOURCES = ConfZFileSource(file=Path(CONTROLLER_CONFIG_FILE))
