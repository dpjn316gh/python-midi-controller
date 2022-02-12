from src.services.configuration_service.adapters.controller_config_service_impl import ControllerConfigServiceConfZ
from src.services.configuration_service.service_impl import ConfigurationServiceImpl
from src.services.midi_controller_service_impl import MidiControllerServiceImpl

controller_configuration_service = ControllerConfigServiceConfZ()
configuration_service = ConfigurationServiceImpl(controller_configuration_service)

cc = configuration_service.get_controller_config()
print(cc)
pc = configuration_service.get_performances_config(cc)
print(pc)

m = MidiControllerServiceImpl(configuration_service)

m.start_service()

print(m.controller_config)