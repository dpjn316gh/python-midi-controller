import logging
import queue
import sys
import threading
import time

from asciimatics.constants import COLOUR_GREEN, A_BOLD
from asciimatics.effects import Background
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError
from asciimatics.exceptions import StopApplication
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Button, Label, Divider

log = logging.getLogger("midifilter")


class MidiDispatcher(threading.Thread):
    def __init__(self):
        super(MidiDispatcher, self).__init__()
        self._wallclock = time.time()
        self.queue = queue.Queue()
        self.halt = False

    def run(self):
        log.debug("Start...")
        while True and not self.halt:
            log.debug("Start...")
            # time.sleep(1000)

    def stop(self):
        self.halt = True
        log.debug("Stop...")


class MidiInterfaceDialogView(Frame):
    FRAME = "selectPerformanceDialog"
    FRAME_TITLE = "Select performance..."
    LISTBOX_PERFORMANCES = "performances_listbox"
    LABEL_DESCRIPTION = "description_label"
    BUTTON_OK = "ok_button"
    BUTTON_OK_TEXT = "Ok"
    BUTTON_CANCEL = "cancel_button"
    BUTTON_CANCEL_TEXT = "Cancel"
    LABEL_INFO = "info_label"
    LABEL_INFO_TEXT = "(q) Close window, (TAB) Switch controls, (Up/Down key) - Select performance"

    def __init__(self, screen, service):
        super(MidiInterfaceDialogView, self).__init__(screen,
                                                      height=10,
                                                      width=150,
                                                      has_border=True,
                                                      can_scroll=False,
                                                      name=self.FRAME,
                                                      title=self.FRAME_TITLE, reduce_cpu=False)

        self.set_layout()
        self.dispatcher = MidiDispatcher()

        self.tempo_clock = time.time()
        self.tempo_thread = threading.Thread(target=self.update_tempo_widget)
        self.stop_tempo_thread = True
        self.tempo_thread_lock = threading.Lock()
        self.bmp = 60
        self.tap_tempo_stats = []

    def set_layout(self):

        self.layout_middle = Layout([1])
        self.add_layout(self.layout_middle)

        self.status_label_1 = Label(height=1, label="", )

        self.user_tempo_label = Label(height=1, label="")
        self.status_tempo_label = Label(height=1, label="", name=self.LABEL_DESCRIPTION)

        self.layout_middle.add_widget(self.user_tempo_label, 0)
        self.layout_middle.add_widget(self.status_label_1, 0)
        self.layout_middle.add_widget(self.status_tempo_label, 0)
        self.layout_middle.add_widget(Divider(), 0)

        layout_bottom = Layout([2, 2])
        self.add_layout(layout_bottom)
        layout_bottom.add_widget(Button(text=self.BUTTON_OK_TEXT,
                                        on_click=self._on_click_ok_button,
                                        add_box=True,
                                        name=self.BUTTON_OK), 0)
        layout_bottom.add_widget(Button(text=self.BUTTON_CANCEL_TEXT,
                                        on_click=self._on_click_cancel_button,
                                        add_box=True,
                                        name=self.BUTTON_CANCEL), 1)
        self.fix()

    def update_tempo_widget(self):
        with self.tempo_thread_lock:
            self.stop_tempo_thread = False

            count = 1
            sub_divisions = 2
            while True:
                if count > 4 * sub_divisions:
                    count = 1
                    msg = ""
                if (count - 1) % sub_divisions == 0:
                    new_time = time.time()
                    current_bmp = 60. / (new_time - self.tempo_clock)
                    msg = f"{count // sub_divisions + 1}"
                else:
                    msg += "."
                self.status_tempo_label.text = f"Real BPM:{current_bmp:.2f}   {msg:>{count}}"
                count += 1
                self.tempo_clock = new_time

                if self.stop_tempo_thread:
                    return

                w = 60.0 / self.bmp / sub_divisions
                time.sleep(w)

    @staticmethod
    def _on_click_cancel_button():
        raise StopApplication("User requested exit")

    def _on_click_ok_button(self):
        self._on_click_cancel_button()

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent):
            if event.key_code in [81, 113]:  # Q
                if self.tempo_thread.is_alive():
                    self.stop_tempo_thread = True
                    self.tempo_thread.join()
                self._on_click_cancel_button()
            if event.key_code in [82, 114]:  # R

                if not self.tempo_thread.is_alive():
                    self.tempo_thread = threading.Thread(target=self.update_tempo_widget)
                    self.tempo_thread.start()
                # if not self.dispatcher.is_alive():
                #     self.dispatcher.start()
            if event.key_code in [83, 115]:  # R
                if self.tempo_thread.is_alive():
                    self.stop_tempo_thread = True
                    self.tempo_thread.join()
                # self.dispatcher.stop()
                # self.dispatcher.join()

            if event.key_code == 49:  # 1
                self.bmp = min(250, max(30, int(self.bmp) - 1))
                self.user_tempo_label.text = f"BMP: {self.bmp}"
            if event.key_code == 50:  # 2
                self.bmp = min(250, max(30, int(self.bmp) + 1))
                self.user_tempo_label.text = f"BMP: {self.bmp}"

            if event.key_code in [84, 116]:  # t
                current_time = time.time()
                self.tap_tempo_stats.append(current_time)
                if len(self.tap_tempo_stats) > 1:
                    seconds_per_pulse_sum = 0
                    bmp_sum = 0
                    min_diff = sys.maxsize
                    max_diff = 0
                    for i in range(len(self.tap_tempo_stats) - 1):
                        diff = abs(self.tap_tempo_stats[i] - self.tap_tempo_stats[i + 1])
                        if diff > max_diff:
                            max_diff = diff
                        if diff < min_diff:
                            min_diff = diff
                        seconds_per_pulse_sum += diff
                        bmp_sum += 60 / abs(self.tap_tempo_stats[i] - self.tap_tempo_stats[i + 1])

                    seconds_per_pulse_avg = 60 * (len(self.tap_tempo_stats) - 1) / seconds_per_pulse_sum
                    bmp_avg = bmp_sum / (len(self.tap_tempo_stats) - 1)
                    seconds_per_pulse_and_bmp_avg = (seconds_per_pulse_avg + bmp_avg) / 2

                    self.user_tempo_label.text = f"Seconds per pulse avg: {seconds_per_pulse_avg:.2f}. BPM avg: {bmp_avg:.2f}. {seconds_per_pulse_and_bmp_avg:.2f}. [{len(self.tap_tempo_stats)}] " \
                                                 f"Min: {min_diff:.2f}. Max: {max_diff:.2f}. {self.tap_tempo_stats[-2]:.2f} {self.tap_tempo_stats[-1]:.2f} "
                    self.bmp = bmp_avg

                if len(self.tap_tempo_stats) >= 10:
                    self.tap_tempo_stats = self.tap_tempo_stats[1:]

                percentage = 0
                if len(self.tap_tempo_stats) >= 8:
                    if not abs(self.tap_tempo_stats[-2] - current_time) < max_diff * (1 + percentage):
                        self.tap_tempo_stats.clear()
                        # self.tap_tempo_stats.append(current_time)

        return super(MidiInterfaceDialogView, self).process_event(event)

    @property
    def frame_update_count(self):
        # Refresh once every 2 seconds by default.
        return 1


def demo(screen, scene):
    scenes = [
        Scene([Background(screen), MidiInterfaceDialogView(screen, None)], -1, name="Main"),

    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])

        quit()
    except ResizeScreenError as e:
        last_scene = e.scene
