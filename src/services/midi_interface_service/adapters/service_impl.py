from typing import List

import rtmidi
from rtmidi.midiutil import get_api_from_environment, open_midiport

from midifilter.filters import MidiFilter
from services.midi_interface_service.adapters.midi_dispatcher_impl import MidiDispatcherV2
from services.midi_interface_service.model.midi_ports import MidiPorts
from services.midi_interface_service.ports.service import MidiInterfaceService


class MidiInterfaceServiceImpl(MidiInterfaceService):
    dispatcher: MidiDispatcherV2 = None

    def list_input_ports(self) -> List[str]:
        api = get_api_from_environment(rtmidi.API_UNSPECIFIED)
        midiin = rtmidi.MidiIn(api)
        return midiin.get_ports()

    def list_output_ports(self) -> List[str]:
        api = get_api_from_environment(rtmidi.API_UNSPECIFIED)
        midiout = rtmidi.MidiOut(api)
        return midiout.get_ports()

    def open_midi_ports(self, midi_ports: MidiPorts):
        for in_port in midi_ports.input_ports_names:
            midiin, inport_name = open_midiport(port=in_port, type_="input", interactive=False)
            midi_ports.input_ports.append((midiin, inport_name))

        for out_port in midi_ports.output_ports_names:
            midiout, outport_name = open_midiport(port=out_port, type_="output", interactive=False)
            midi_ports.output_ports.append((midiout, outport_name))

    def close_midi_ports(self, midi_ports: MidiPorts):
        for midiin, inport_name in midi_ports.input_ports:
            midiin.close_port()
            del midiin

        midi_ports.input_ports = []

        for midiout, outport_name in midi_ports.output_ports:
            midiout.close_port()
            del midiout

        midi_ports.output_ports = []

    def run_midi_dispatcher(self, midi_ports: MidiPorts, midi_filters: List[MidiFilter]):
        if len(midi_ports.input_ports) > 0 and len(midi_ports.output_ports) > 0:
            if self.dispatcher is None:
                self.dispatcher = MidiDispatcherV2(midi_ports.input_ports, midi_ports.output_ports[0], *midi_filters)
                self.dispatcher.start()

    def stop_midi_dispatcher(self):
        if self.dispatcher and self.dispatcher.is_alive():
            self.dispatcher.stop()
            self.dispatcher.join()
            self.dispatcher = None
