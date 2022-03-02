from abc import ABC, abstractmethod

from presentation.models.midi_interfaces.midi_interface_dialog_view_data import MidiInterfaceViewData


class MidiInterfaceDialogPresenterView(ABC):

    @abstractmethod
    def set_list_io_ports(self, midi_interface_view_data: MidiInterfaceViewData):
        raise NotImplementedError

    @abstractmethod
    def get_io_ports(self) -> MidiInterfaceViewData:
        raise NotImplementedError

    def set_io_ports(self, midi_interface_view_data: MidiInterfaceViewData):
        raise NotImplementedError
