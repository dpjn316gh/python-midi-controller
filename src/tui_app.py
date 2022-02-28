from asciimatics.effects import Background
from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from presentation.views.menu_frame import MenuFrame
from presentation.views.midi_interfaces.midi_interface_dialog_view import MidiInterfaceDialogView
from presentation.views.performances.performance_live_view import PerformanceLiveView
from presentation.views.performances.performances_open_dialog_view import PerformancesOpenDialogView
from services.configuration_service.adapters.controller_config_service_impl import ControllerConfigServiceConfZ
from services.configuration_service.service_impl import ConfigurationServiceImpl
from services.midi_controller_service_impl import MidiControllerServiceImpl
from services.midi_filter_builder_service.adapters.service_impl import MidiFilterBuilderServiceImpl
from services.midi_interface_service.adapters.service_impl import MidiInterfaceServiceImpl

controller_configuration_service = ControllerConfigServiceConfZ()
configuration_service = ConfigurationServiceImpl(controller_configuration_service)
midi_interface_service = MidiInterfaceServiceImpl()
midi_filter_builder_service=MidiFilterBuilderServiceImpl()
service = MidiControllerServiceImpl(configuration_service=configuration_service,
                                    midi_interface_service=midi_interface_service,
                                    midi_filter_builder_service=midi_filter_builder_service)

service.start_service()


def demo(screen, scene):
    scenes = [
        Scene([Background(screen), MenuFrame(screen)], -1, name="Main"),
        Scene([MenuFrame(screen)], -1, name="Menu"),
        Scene([PerformanceLiveView(screen, service)], -1, name="PerformanceLive"),
        Scene([PerformancesOpenDialogView(screen, service)], -1, name="PerformancesOpenDialog"),
        Scene([MidiInterfaceDialogView(screen, service)], -1, name="MidiInterfaceDialog")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
        # print(service.get_current_performance().name)
        quit()
    except ResizeScreenError as e:
        last_scene = e.scene
