import logging
import sys
import time
from pathlib import Path
from adapters.mappers.filters_builder import FiltersBuilder

from rtmidi.midiutil import open_midiport
from midifilter.filter import MidiDispatcher

from model.configuration.configuration_manager import load_performances_config
from model.configuration.controller_config import ControllerConfig
from confz import validate_all_configs


validate_all_configs()

general_config = ControllerConfig()
pc1 = load_performances_config()

default_performance = next(filter(lambda x: x.number == 3, pc1))

filters_builder = FiltersBuilder()

filters = filters_builder.build_filters_from_performance(default_performance)

print(filters)

# open a file
def main():

    level =logging.DEBUG if True else logging.INFO
    logging.basicConfig(format="%(name)s: %(levelname)s - %(message)s", level=level)

    try:
        midiin, inport_name = open_midiport(None, "input")
        midiout, outport_name = open_midiport(None, "output")
    except IOError as exc:
        print(exc)
        return 1
    except (EOFError, KeyboardInterrupt):
        return 0


    dispatcher = MidiDispatcher(midiin, midiout, *filters)

    print("Entering main loop. Press Control-C to exit.")
    try:
        dispatcher.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        dispatcher.stop()
        dispatcher.join()
        print('')
    finally:
        print("Exit.")

        midiin.close_port()
        midiout.close_port()

        del midiin
        del midiout

    return 0


if __name__ == '__main__':
    sys.exit(main() or 0)


