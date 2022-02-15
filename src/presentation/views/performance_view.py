from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, MultiColumnListBox, Text, RadioButtons, Button, Divider, Label


class PerformanceView(Frame):

    PERFORMANCE_VIEW_NAME = "performance_view"
    PERFORMANCE_VIEW_TITLE = "Virtual Midi Controller - Performance Mode"
    BUTTON_LOAD_PERFORMANCE = "Load Performance..."

    def __init__(self, screen):
        super(PerformanceView, self).__init__(screen,
                                              height=screen.height,
                                              width=screen.width,
                                              y=0,
                                              has_border=True,
                                              can_scroll=False,
                                              name=self.PERFORMANCE_VIEW_NAME,
                                              title=self.PERFORMANCE_VIEW_TITLE)
        self.set_layout()

    def set_layout(self):
        layout_top = Layout([2,2,2,2,2,2,2,2], fill_frame=False)
        self.add_layout(layout_top)
        layout_top.add_widget(Button(self.BUTTON_LOAD_PERFORMANCE, self._open_file, add_box=True), 0)
        layout_top.add_widget(Label("Signature"), 1)
        layout_top.add_widget(Label("BPM"), 1)
        layout_top.add_widget(Label("[ ]"), 2)
        layout_top.add_widget(Label("[ ]"), 3)
        layout_top.add_widget(Label("[ ]"), 4)
        layout_top.add_widget(Label("[ ]"), 5)
        layout_top.add_widget(Label("[ ]"), 6)
        layout_top.add_widget(Label("[ ]"), 7)

        layout_layers = Layout([1], fill_frame=True)

        self.add_layout(layout_layers)
        l = [(["1", "1", "O", "C1", "C5", "0", "127", "-1", "0", "X", "X", "0", "8"], 1),
             (["2", "2", "O", "C6", "C9", "50", "127", "-1", "+12", "X", "X", "0", "6"], 2)]

        layout_layers.add_widget(Divider())
        layout_layers.add_widget(MultiColumnListBox(16,
                                             [">2", ">4", "^5", ">4", ">6", ">6", ">6", ">4", ">5", "^5",
                                              "^4", ">3", ">6q"],
                                             l,
                                             titles=["#", "Cha", "Ena", "L.Key", "U.Key", "L.Vel", "U.Vel",
                                                     "Oct", "Tran", "F.V", "K.N", "Pro", "C.C."],
                                             ))
        layout_layers.add_widget(Divider())
        layout_layers.add_widget(RadioButtons([("Option 1", 1),
                                        ("Option 2", 2),
                                        ("Option 3", 3)],
                                       label="A Longer Selection:",
                                       name="Things"), 0)

        self.fix()

    @staticmethod
    def _open_file():
        raise NextScene("PerformancesOpenDialog")

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent):
            if event.key_code in [81, 113]:
                raise NextScene("Menu")

        return super(PerformanceView, self).process_event(event)
