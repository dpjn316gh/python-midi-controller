from __future__ import absolute_import

import logging
import queue
import threading
import time

log = logging.getLogger("midifilter")


class MidiDispatcherV2(threading.Thread):
    def __init__(self, midiins, midiout, *filters):
        super(MidiDispatcherV2, self).__init__()
        # Hacer mejora
        self.midiins = [e[0] for e in midiins]
        self.midiout = midiout[0]
        self.filters = filters
        self._wallclock = time.time()
        self.queue = queue.Queue()
        self.halt = False

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        log.debug("IN: @%0.6f %r", self._wallclock, message)
        self.queue.put((message, self._wallclock))

    def run(self):
        self.halt = False
        log.debug("Attaching MIDI input callback handler.")
        for mi in self.midiins:
            mi.set_callback(self)

        prev_time = 0
        curr_time = 0
        while True and not self.halt:
            event = self.queue.get()

            if event is None:
                break

            events = [event]
            processed_events = []

            for filter_ in self.filters:
                processed_event = filter_.process(events)
                if processed_event != None:
                    processed_events.append(processed_event)

            for event in processed_events:
                log.debug("Out: @%0.6f %r", event[1], event[0])
                self.midiout.send_message(event[0])

    def stop(self):
        self.halt = True
        self.queue.put(None)
