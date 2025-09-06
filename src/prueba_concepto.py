import logging
import queue
import sys
import threading
import time

logging.basicConfig(format="%(name)s: %(levelname)s - %(message)s", level=logging.DEBUG)
log = logging.getLogger("midifilter")


class MidiDispatcher(threading.Thread):
    def __init__(self, name):
        super(MidiDispatcher, self).__init__()
        self._wallclock = time.time()
        self.queue = queue.Queue()
        self.name = name
        self.quit = False
        print(self.is_alive())

    def __call__(self):
        log.debug("Doing something...")
        time.sleep(2)

    def run(self):

        log.debug("Start...")
        n = 0
        while True and n < 100 and not self.quit:
            log.debug(f"Worker {self.name}... {n}")
            time.sleep(2)
            n += 1

    def stop(self):
        self.quit = True
        log.debug(f"Stop... {self.name}")

    def resume(self):
        self.quit = False
        log.debug(f"Resume... {self.name}")

def main():
    dispatcher = MidiDispatcher("1")
    dispatcher1 = MidiDispatcher("2")

    try:
        while True:
            print(".")
            inp = input()
            if inp == 'f':
                if not dispatcher.is_alive():

                    dispatcher.start()
                if not dispatcher1.is_alive():
                    dispatcher1.start()
            if inp == 'p':
                log.debug(f"stopping")
                if dispatcher.is_alive():
                    dispatcher.stop()
                if dispatcher1.is_alive():
                    dispatcher1.stop()
                log.debug(f"stopped")
            if inp == 's':
                if dispatcher.is_alive():
                    dispatcher.stop()
                    dispatcher.join()
                    log.debug(f"Joined")
                if dispatcher1.is_alive():
                    dispatcher1.stop()
                    dispatcher1.join()
                    log.debug(f"Joined 1")

            if inp == 'j':
                log.debug(f"Joining...")
                dispatcher.join()
                dispatcher1.join()
                log.debug(f"Joined")
            if inp == 'i':
                print(dispatcher.is_alive(), dispatcher1.is_alive())
            if inp == 'q':
                break
    except KeyboardInterrupt:
        dispatcher.stop()
        dispatcher.join()
        dispatcher1.stop()
        dispatcher1.join()
    finally:
        print("Exit.")


if __name__ == '__main__':
    sys.exit(main() or 0)


"https://m7i.org/tutorials/python-event-queue-concurrency-modeling/"