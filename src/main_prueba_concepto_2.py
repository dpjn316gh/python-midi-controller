import logging

import rtmidi
from rtmidi.midiutil import open_midiport, get_api_from_environment

logging.basicConfig(format="%(name)s: %(levelname)s - %(message)s", level=logging.DEBUG)

api = get_api_from_environment(rtmidi.API_UNSPECIFIED)
midiin = rtmidi.MidiIn(api)
in_ports = midiin.get_ports()
print(in_ports)

midiout = rtmidi.MidiOut(api)
out_ports = midiout.get_ports()
print(out_ports)

midiin, inport_name = open_midiport(
    port='E-MU XMidi2X2:E-MU XMidi2X2 Midi Out 2  28:1',
    type_="input",
    interactive=False
)
print('MIDI IN:', inport_name)