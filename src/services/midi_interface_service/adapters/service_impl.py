from typing import List

import rtmidi
from rtmidi.midiutil import get_api_from_environment

from services.midi_interface_service.ports.service import MidiInterfaceService


class MidiInterfaceServiceImpl(MidiInterfaceService):
    def list_input_ports(self) -> List[str]:
        api = get_api_from_environment(rtmidi.API_UNSPECIFIED)
        midiin = rtmidi.MidiIn(api)
        return midiin.get_ports()

    def list_output_ports(self) -> List[str]:
        api = get_api_from_environment(rtmidi.API_UNSPECIFIED)
        midiout = rtmidi.MidiOut(api)
        return midiout.get_ports()
