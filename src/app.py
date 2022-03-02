from services.configuration_service.adapters.controller_config_service_impl import ControllerConfigServiceConfZ
from services.configuration_service.service_impl import ConfigurationServiceImpl
from services.midi_controller_service_impl import MidiControllerServiceImpl
from services.midi_filter_builder_service.adapters.service_impl import MidiFilterBuilderServiceImpl
from services.midi_interface_service.adapters.service_impl import MidiInterfaceServiceImpl

controller_configuration_service = ControllerConfigServiceConfZ()
configuration_service = ConfigurationServiceImpl(controller_configuration_service)
midi_interface_service = MidiInterfaceServiceImpl()
midi_filter_builder_service=MidiFilterBuilderServiceImpl()

cc = configuration_service.get_controller_config()
print(cc)
pc = configuration_service.get_performances_config(cc)
print(pc)

m = MidiControllerServiceImpl(configuration_service=configuration_service,
                              midi_interface_service=midi_interface_service,
                              midi_filter_builder_service=midi_filter_builder_service)
m.start_service()

print(m.controller_config)
print(m.list_output_ports())
