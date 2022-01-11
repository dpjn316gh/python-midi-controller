from pathlib import Path

from model.configuration.configuration_manager import load_performances_config
from model.configuration.general_config import GeneralConfig
from confz import validate_all_configs


# validate_all_configs()

general_config = GeneralConfig()


pc1 = load_performances_config()
pc2 = load_performances_config()

    
general_config1 = GeneralConfig()
print(general_config is general_config1)
print(id(general_config), id(general_config1))
print(pc1[0] is pc1[0])
print(id(pc1[0]), id(pc1[0]))


# open a file
