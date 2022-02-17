from asciimatics.effects import Background
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError
from asciimatics.exceptions import StopApplication
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Button, ListBox, Label, Divider
from rtmidi.midiutil import open_midiport, list_output_ports, list_input_ports, list_available_ports


class MidiInterfaceDialogView(Frame):
    opciones = [("Piano", 1),
                ("Piano y String", 2),
                ("Sintetizador", 3),
                ("Coro Gospel", 4),
                ("Bluse Band", 5),
                ("ACDC", 6),
                ("Amanecer de nuevo", 7),
                ("Colombiana", 8),
                ("Salsa", 9),
                ("Merengue", 10),
                ("Reguee", 11),
                ("Funk!", 12),
                ]

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
                                         height=26,
                                         width=80,
                                         has_border=True,
                                         can_scroll=False,
                                         name=self.FRAME,
                                         title=self.FRAME_TITLE)
        self.set_layout()

    def set_layout(self):

        result = list_input_ports()

        layout_top = Layout([1], fill_frame=False)
        self.add_layout(layout_top)
        layout_top.add_widget(ListBox(height=10,
                                      options=self.opciones,
                                      name=self.LISTBOX_PERFORMANCES,
                                      add_scroll_bar=True,
                                      on_change=self._on_change_performances_listbox), 0)

        layout_middle = Layout([1])
        self.add_layout(layout_middle)
        layout_middle.add_widget(Divider(), 0)
        layout_middle.add_widget(Label(height=10, label="", name=self.LABEL_DESCRIPTION), 0)
        layout_middle.add_widget(Divider(), 0)

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

        layout_bottom_1 = Layout([1])
        self.add_layout(layout_bottom_1)

        layout_bottom_1.add_widget(Label(height=10, label=self.LABEL_INFO_TEXT, name=self.LABEL_INFO), 0)

        self.fix()



    @staticmethod
    def _on_click_cancel_button():
        raise StopApplication("User requested exit")

    def _on_click_ok_button(self):
        # salvar elemento
        self._on_click_cancel_button()

    def _on_change_performances_listbox(self):
        listbox_performances = self.find_widget(self.LISTBOX_PERFORMANCES)
        label_description = self.find_widget(self.LABEL_DESCRIPTION)

        for e in self.opciones:
            if e[1] == listbox_performances.value:
                label_description.text = str(e[0]) + "DESCRIPTION"
                break

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent):
            if event.key_code in [81, 113]:
                self._on_click_cancel_button()

        return super(MidiInterfaceDialogView, self).process_event(event)





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
