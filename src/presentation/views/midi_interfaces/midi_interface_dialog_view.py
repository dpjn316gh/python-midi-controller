from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, CheckBox, Label, Divider, Button

from presentation.models.midi_interfaces.midi_interface_dialog_view_data import MidiInterfaceViewData
from presentation.presenters.midi_interfaces.midi_interface_dialog_presenter import \
    MidiInterfaceDialogPresenterView, MidiInterfaceDialogPresenter


class MidiInterfaceDialogView(Frame, MidiInterfaceDialogPresenterView):
    FRAME = "midi_interface_dialog"
    FRAME_TITLE = "Midi interfaces..."
    BUTTON_OK = "ok_button"
    BUTTON_OK_TEXT = "Ok"
    BUTTON_CANCEL = "cancel_button"
    BUTTON_CANCEL_TEXT = "Cancel"

    def __init__(self, screen, service):
        self.presenter = MidiInterfaceDialogPresenter(self, service)

        super(MidiInterfaceDialogView, self).__init__(screen,
                                                      height=26,
                                                      width=80,
                                                      has_border=True,
                                                      can_scroll=True,
                                                      name=self.FRAME,
                                                      title=self.FRAME_TITLE,
                                                      on_load=self._reload_frame
                                                      )

        input_ports_info_layout = Layout([1], fill_frame=False)
        self.add_layout(input_ports_info_layout)
        input_ports_info_layout.add_widget(Label("Midi input"))

        self.input_ports_checkbox_layout = Layout([1], fill_frame=False)
        self.add_layout(self.input_ports_checkbox_layout)

        output_ports_info_layout = Layout([1], fill_frame=False)
        self.add_layout(output_ports_info_layout)
        output_ports_info_layout.add_widget(Divider())
        output_ports_info_layout.add_widget(Label("Midi output"))

        self.output_ports_checkbox_layout = Layout([1], fill_frame=False)
        self.add_layout(self.output_ports_checkbox_layout)

        divider_layout = Layout([1], fill_frame=False)
        self.add_layout(divider_layout)
        divider_layout.add_widget(Divider())

        buttons_layout = Layout([1, 1], fill_frame=False)
        self.add_layout(buttons_layout)
        buttons_layout.add_widget(Button(text=self.BUTTON_OK_TEXT,
                                         on_click=self._on_click_ok_button,
                                         add_box=True,
                                         name=self.BUTTON_OK), 0)
        buttons_layout.add_widget(Button(text=self.BUTTON_CANCEL_TEXT,
                                         on_click=self._on_click_cancel_button,
                                         add_box=True,
                                         name=self.BUTTON_CANCEL), 1)

    def _reload_frame(self):
        self.presenter.list_io_ports()
        self.presenter.get_io_ports()
        self.set_layout()

    def set_layout(self):
        self.input_ports_checkbox_layout.clear_widgets()
        self.input_ports_checkbox = []

        self.input_ports_checkbox_layout.update(self)
        for ip in self.model.input_ports:
            cb = CheckBox(text=ip)
            if ip in self.selected_model.input_ports:
                cb.value = True
            self.input_ports_checkbox.append(cb)
            self.input_ports_checkbox_layout.add_widget(cb)

        self.output_ports_checkbox_layout.clear_widgets()
        self.output_ports_checkbox = []

        self.output_ports_checkbox_layout.update(self)
        for op in self.model.output_ports:
            cb = CheckBox(text=op)
            if op in self.selected_model.output_ports:
                cb.value = True
            self.output_ports_checkbox.append(cb)
            self.output_ports_checkbox_layout.add_widget(cb)

        self.fix()

    @staticmethod
    def _on_click_cancel_button():
        raise NextScene("Menu")

    def _on_click_ok_button(self):
        self.presenter.set_io_ports()
        self._on_click_cancel_button()

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent):
            if event.key_code in [81, 113]:
                self._on_click_cancel_button()

        return super(MidiInterfaceDialogView, self).process_event(event)

    def set_list_io_ports(self, midi_interface_view_data: MidiInterfaceViewData):
        self.model = midi_interface_view_data

    def get_io_ports(self) -> MidiInterfaceViewData:
        selected_midi_ports = MidiInterfaceViewData()
        for ip_cb in self.input_ports_checkbox:
            if ip_cb.value:
                selected_midi_ports.input_ports.append(ip_cb._text)

        for op_cb in self.output_ports_checkbox:
            if op_cb.value:
                selected_midi_ports.output_ports.append(op_cb._text)
        return selected_midi_ports

    def set_io_ports(self, midi_interface_view_data: MidiInterfaceViewData):
        self.selected_model = midi_interface_view_data
