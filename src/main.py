from pathlib import Path

from model.configuration.configuration_manager import load_performances_config
from model.configuration.general_config import GeneralConfig
from confz import validate_all_configs


validate_all_configs()

general_config = GeneralConfig()
pc1 = load_performances_config()
pc2 = load_performances_config()

    

print(pc1[0] is pc2[0])
print(id(pc1[0]), id(pc2[0]))


# open a file
