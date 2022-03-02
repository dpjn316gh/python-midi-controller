from abc import ABC, abstractmethod
from typing import List

from midifilter.filters import MidiFilter
from services.midi_interface_service.model.midi_ports import MidiPorts


class MidiInterfaceService(ABC):

    @abstractmethod
    def list_input_ports(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def list_output_ports(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def open_midi_ports(self, midi_ports: MidiPorts):
        raise NotImplementedError

    @abstractmethod
    def close_midi_ports(self, midi_ports: MidiPorts):
        raise NotImplementedError

    @abstractmethod
    def run_midi_dispatcher(self, midi_ports: MidiPorts, midi_filters: List[MidiFilter]):
        raise NotImplementedError

    @abstractmethod
    def stop_midi_dispatcher(self):
        raise NotImplementedError
