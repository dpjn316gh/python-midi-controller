import logging
import sys
import time

from rtmidi.midiutil import open_midiport
from midifilter.filter_prueba_concepto import MidiDispatcherConcepto


def ask_yesno(question, default=True):

    yes = {'yes', 'y'}
    no = {'no', 'n'}  # pylint: disable=invalid-name

    done = False
    print(question)
    while not done:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        elif choice in '':
            return default
        else:
            print("Please respond by yes or no.")

# open a file
def main():

    level =logging.DEBUG if True else logging.INFO
    logging.basicConfig(format="%(name)s: %(levelname)s - %(message)s", level=level)

    try:
        midiins = []
        while True:
            midiin, inport_name = open_midiport(None, "input")
            midiins.append(midiin)
            if not ask_yesno("Would you like to add another input port (y/N)?", False):
                break
        midiout, outport_name = open_midiport(None, "output")
    except IOError as exc:
        print(exc)
        return 1
    except (EOFError, KeyboardInterrupt):
        return 0


    dispatcher = MidiDispatcherConcepto(midiins, midiout)

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


