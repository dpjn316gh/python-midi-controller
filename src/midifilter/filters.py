# -*- coding: utf-8 -*-
#
# midifilter/filters.py
#
"""Collection of MIDI filter classes."""

from typing import Any
from rtmidi.midiconstants import (BANK_SELECT_LSB, BANK_SELECT_MSB, CHANNEL_PRESSURE,
                                  CONTROLLER_CHANGE, NOTE_ON, NOTE_OFF, PROGRAM_CHANGE)


__all__ = (
    'CCToBankChange',
    'MapControllerValue',
    'MidiFilter',
    'MonoPressureToCC',
    'Transpose',
    'SendAnotherChannel',
    'NoteRange',
    'VelocityRange',
    'PassThru',
)


class MidiFilter(object):
    """ABC for midi filters."""

    event_types = ()

    def __init__(self, *args, **kwargs):
        self.successor_filter = None
        self.args = args
        self.__dict__.update(kwargs)

    def set_successor_filter(self, successor_filter: Any):
        self.successor_filter = successor_filter

    def process(self, events):
        """Process incoming events.

        Receives a list of MIDI event tuples (message, timestamp).

        Must return an iterable of event tuples.

        """
        raise NotImplementedError("Abstract method 'process()'.")

    def match(self, msg):
        return msg[0] & 0xF0 in self.event_types


class SendAnotherChannel(MidiFilter):
    """Transpose note on/off events."""

    event_types = (NOTE_ON, NOTE_OFF)

    def process(self, events):
        copied_events = []
        for e in events:
            copied_events.append(tuple((e[0].copy(), e[1])))

        for msg, timestamp in copied_events:
            if self.match(msg):
                msg[0] = msg[0] | max(0, min(15, self.channel))

            yield msg, timestamp


class Transpose(MidiFilter):
    """Transpose note on/off events."""

    event_types = (NOTE_ON, NOTE_OFF)

    def process(self, events):
        for msg, timestamp in events:
            if self.match(msg):
                msg[0] = msg[0] | max(0, min(15, self.channel))
                msg[1] = max(0, min(127, msg[1] + self.transpose)) & 0x7F
                if self.successor_filter != None:
                    return self.successor_filter.process([(msg, timestamp)])
                else:
                    return msg, timestamp


class NoteRange(MidiFilter):
    
    event_types = (NOTE_ON, NOTE_OFF)
    
    def process(self, events):
        copied_events = []
        for e in events:
            copied_events.append(tuple((e[0].copy(), e[1])))

        for msg, timestamp in copied_events:
            if self.match(msg):
                if max(0, min(127, self.lower)) & 0x7F <= msg[1] <= max(0, min(127, self.upper)) & 0x7F:
                    msg[0] = msg[0] | max(0, min(15, self.channel))
                    if self.successor_filter != None:
                        return self.successor_filter.process([(msg, timestamp)])                        
                    return msg, timestamp


class VelocityRange(MidiFilter):
    
    event_types = (NOTE_ON, NOTE_OFF)
    
    def process(self, events):
        for msg, timestamp in events:
            if self.match(msg):
                msg[0] = msg[0] | max(0, min(15, self.channel))
                if msg[0] & NOTE_ON == NOTE_ON and max(0, min(127, self.lower)) & 0x7F <= msg[2] <= max(0, min(127, self.upper)) & 0x7F:
                    return msg, timestamp
                if msg[0] & NOTE_OFF == NOTE_OFF and msg[2] & 0x7F == 0x00:
                    return msg, timestamp


class PassThru(MidiFilter):
        
    def process(self, events):
        for msg, timestamp in events:
            msg[0] = msg[0] | max(0, min(15, self.channel))
            yield msg, timestamp


class MapControllerValue(MidiFilter):
    """Map controller values to min/max range."""

    event_types = (CONTROLLER_CHANGE,)

    def __init__(self, cc, min_, max_, *args, **kwargs):
        super(MapControllerValue, self).__init__(*args, **kwargs)
        self.cc = cc
        self.min = min_
        self.max = max_

    def process(self, events):
        for msg, timestamp in events:
            # check controller number
            if self.match(msg) and msg[1] == self.cc:
                # map controller value
                msg[2] = int(self._map(msg[2]))

            yield msg, timestamp

    def _map(self, value):
        return value * (self.max - self.min) / 127. + self.min


class MonoPressureToCC(MidiFilter):
    """Change mono pressure events into controller change events."""

    event_types = (CHANNEL_PRESSURE,)

    def process(self, events):
        for msg, timestamp in events:
            if self.match(msg):
                channel = msg[0] & 0xF
                msg = [CONTROLLER_CHANGE | channel, self.cc, msg[1]]

            yield msg, timestamp


class CCToBankChange(MidiFilter):
    """Map controller change to a bank select, program change sequence."""

    event_types = (CONTROLLER_CHANGE,)

    def process(self, events):
        for msg, timestamp in events:
            channel = msg[0] & 0xF

            # check controller number & channel
            if (self.match(msg) and channel == self.channel and
                    msg[1] == self.cc):
                msb = [CONTROLLER_CHANGE + channel, BANK_SELECT_MSB, self.msb]
                lsb = [CONTROLLER_CHANGE + channel, BANK_SELECT_LSB, self.lsb]
                pc = [PROGRAM_CHANGE + channel, self.program]
                yield msb, timestamp
                yield lsb, timestamp
                yield pc, timestamp
            else:
                yield msg, timestamp
