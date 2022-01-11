from pathlib import Path

from confz import ConfZ
from confz.confz_source import ConfZFileSource
from model.configuration.configuration_constants import CONTROLLER_CONFIG_FILE


class GeneralConfig(ConfZ):
    performance_folder: str

    CONFIG_SOURCES = ConfZFileSource(file=Path(CONTROLLER_CONFIG_FILE))
