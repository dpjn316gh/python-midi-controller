import threading
from queue import Queue
from typing import List, Callable

import rtmidi
from rtmidi.midiutil import get_api_from_environment, open_midiport

from midifilter.filters import MidiFilter
from services.midi_interface_service.adapters.midi_dispatcher_impl import MidiDispatcherV2
from services.midi_interface_service.model.midi_ports import MidiPorts
from services.midi_interface_service.ports.service import MidiInterfaceService


class MidiInEventConsumer(threading.Thread):

    def __init__(self, queue: Queue, on_midi_in_event_callback: Callable[[str], None]):
        threading.Thread.__init__(self)
        self.halt = False
        self.queue = queue
        self.on_midi_in_event_callback = on_midi_in_event_callback

    def run(self):
        while True and not self.halt:
            event = self.queue.get()
            self.queue.task_done()
            self.on_midi_in_event_callback(event)

    def stop(self):
        self.halt = True
        self.queue.put(None)


class MidiOutEventConsumer(threading.Thread):

    def __init__(self, queue: Queue, on_midi_out_event_callback: Callable[[str], None]):
        threading.Thread.__init__(self)
        self.halt = False
        self.queue = queue
        self.on_midi_out_event_callback = on_midi_out_event_callback

    def run(self):
        while True and not self.halt:
            event = self.queue.get()
            self.queue.task_done()
            self.on_midi_out_event_callback(event)

    def stop(self):
        self.halt = True
        self.queue.put(None)


class MidiInterfaceServiceImpl(MidiInterfaceService):
    dispatcher: MidiDispatcherV2 = None

    def __init__(self):
        self.midi_out_event_listener = None
        self.midi_in_event_listener = None
        self.__controller_running = False
        self.on_midi_in_events_queue = Queue()
        self.on_midi_out_events_queue = Queue()

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

    def run_midi_dispatcher(self,
                            midi_ports: MidiPorts,
                            midi_filters: List[MidiFilter],
                            on_midi_in_event_callback: Callable[[str], None],
                            on_midi_out_event_callback: Callable[[str], None]):
        if len(midi_ports.input_ports) > 0 and len(midi_ports.output_ports) > 0:
            if self.dispatcher is None and not self.__controller_running:
                self.midi_in_event_listener = MidiInEventConsumer(self.on_midi_in_events_queue, on_midi_in_event_callback)
                self.midi_out_event_listener = MidiOutEventConsumer(self.on_midi_out_events_queue, on_midi_out_event_callback)

                self.midi_in_event_listener.start()
                self.midi_out_event_listener.start()
                self.dispatcher = MidiDispatcherV2(midi_ports.input_ports,
                                                   midi_ports.output_ports[0],
                                                   self.on_midi_in_events_queue,
                                                   self.on_midi_out_events_queue,
                                                   *midi_filters)
                self.__controller_running = True
                self.dispatcher.start()

    def stop_midi_dispatcher(self):
        if self.dispatcher and self.dispatcher.is_alive():
            self.dispatcher.stop()
            self.dispatcher.join()
            self.dispatcher = None
            self.midi_in_event_listener.stop()
            self.midi_in_event_listener.join()
            self.midi_out_event_listener.stop()
            self.midi_out_event_listener.join()
            self.midi_in_event_listener = None
            self.midi_out_event_listener = None
            self.__controller_running = False
