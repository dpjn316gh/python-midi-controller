from asciimatics.effects import Background
from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from presentation.views.file_open_dialog_view import FileOpenDialogView
from presentation.views.performance_view import PerformanceView
from presentation.views.menu_frame import MenuFrame
from services.configuration_service.adapters.controller_config_service_impl import ControllerConfigServiceConfZ
from services.configuration_service.service_impl import ConfigurationServiceImpl
from services.midi_controller_service_impl import MidiControllerServiceImpl

controller_configuration_service = ControllerConfigServiceConfZ()
configuration_service = ConfigurationServiceImpl(controller_configuration_service)
service = MidiControllerServiceImpl(configuration_service)

service.start_service()

def demo(screen, scene):
    scenes = [
        Scene([Background(screen), MenuFrame(screen)], -1, name="Main"),
        Scene([MenuFrame(screen)], -1, name="Menu"),
        Scene([PerformanceView(screen)], -1, name="Performance"),
        Scene([FileOpenDialogView(screen, service)], -1, name="FileOpenDialogPerformance")

    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
        #print(service.get_current_performance().name)
        quit()
    except ResizeScreenError as e:
        last_scene = e.scene

