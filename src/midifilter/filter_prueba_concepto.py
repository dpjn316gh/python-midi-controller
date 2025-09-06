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
import queue


log = logging.getLogger("midifilter")


class MidiDispatcherConcepto(threading.Thread):
    def __init__(self, midiins, midiout):
        super(MidiDispatcherConcepto, self).__init__()
        self.midiins = midiins

        self.midiout = midiout
        self._wallclock = time.time()
        self.queue = queue.Queue()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        log.debug("IN: @%0.6f %r", self._wallclock, message)
        self.queue.put((message, self._wallclock))

    def run(self):
        log.debug("Attaching MIDI input callback handler.")
        for mi in self.midiins:
            mi.set_callback(self)

        while True:
            event = self.queue.get()

            if event is None:
                break

            events = [event]
            
            for event in events:
                log.debug("Out: @%0.6f %r", event[1], event[0])
                self.midiout.send_message(event[0])

    def stop(self):
        self.queue.put(None)

