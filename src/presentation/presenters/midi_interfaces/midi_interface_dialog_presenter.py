from presentation.models.midi_interfaces.midi_interface_dialog_view_data import MidiInterfaceViewData
from presentation.presenters.midi_interfaces.midi_interface_dialog_presenter_view import \
    MidiInterfaceDialogPresenterView
from services.midi_controller_service import MidiControllerService
from services.midi_interface_service.model.midi_ports import MidiPorts


class MidiInterfaceDialogPresenter:
    view: MidiInterfaceDialogPresenterView

    def __init__(self, view: MidiInterfaceDialogPresenterView, service: MidiControllerService):
        self.service = service
        self.view = view

    def list_io_ports(self):
        input_ports = self.service.list_input_ports()
        output_ports = self.service.list_output_ports()
        midi_io_ports = MidiInterfaceViewData(input_ports=input_ports, output_ports=output_ports)
        self.view.set_list_io_ports(midi_io_ports)

    def set_io_ports(self):
        selected_io_ports = self.view.get_io_ports()
        midi_ports = MidiPorts(input_ports_names=selected_io_ports.input_ports, output_ports_names=selected_io_ports.output_ports)
        self.service.set_midi_ports(midi_ports)

    def get_io_ports(self):
        midi_ports = self.service.get_midi_ports()
        selected_io_ports = MidiInterfaceViewData(input_ports=midi_ports.input_ports_names,
                                                  output_ports=midi_ports.output_ports_names)
        self.view.set_io_ports(selected_io_ports)
