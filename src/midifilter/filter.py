#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# midifilter/__main__.py
#
"""Simple MIDI filter / processor."""

from __future__ import absolute_import

import argparse
import logging
import sys
import threading
import time

try:
    import Queue as queue
except ImportError:  # Python 3
    import queue

from rtmidi.midiutil import open_midiport


log = logging.getLogger("midifilter")


class MidiDispatcher(threading.Thread):
    def __init__(self, midiin, midiout, *filters):
        super(MidiDispatcher, self).__init__()
        self.midiin = midiin
        self.midiout = midiout
        self.filters = filters
        self._wallclock = time.time()
        self.queue = queue.Queue()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        log.debug("IN: @%0.6f %r", self._wallclock, message)
        self.queue.put((message, self._wallclock))

    def run(self):
        log.debug("Attaching MIDI input callback handler.")
        self.midiin.set_callback(self)

        prev_time = 0
        curr_time = 0
        while True:
            event = self.queue.get()

            if event is None:
                break

            events = [event]
            processed_events = []

            for filter_ in self.filters:
                processed_events = processed_events + list(filter_.process(events))
            
            for event in processed_events:

                if event[0][0] == 144 and event[0][2] !=0:
                    if prev_time == 0:
                        prev_time = event[1]
                        curr_time = event[1]
                    else:
                        prev_time = curr_time
                        curr_time = event[1]
                    if curr_time - prev_time != 0:
                        log.debug("Delta: @%0.6f", 60. / (curr_time - prev_time))    

                log.debug("Out: @%0.6f %r", event[1], event[0])
                self.midiout.send_message(event[0])

    def stop(self):
        self.queue.put(None)

