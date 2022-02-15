from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, Button, ListBox, Label, Divider

from presentation.models.performances.performances_open_dialog_view_data import PerformancesOpenDialogViewDataList
from presentation.presenters.performances.performances_open_dialog_presenter import PerformancesOpenDialogPresenter
from presentation.presenters.performances.performances_open_dialog_presenter_view import \
    PerformancesOpenDialogPresenterView


class PerformancesOpenDialogView(Frame, PerformancesOpenDialogPresenterView):
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
        super(PerformancesOpenDialogView, self).__init__(screen,
                                                         height=26,
                                                         width=80,
                                                         has_border=True,
                                                         can_scroll=False,
                                                         name=self.FRAME,
                                                         title=self.FRAME_TITLE)

        self.presenter = PerformancesOpenDialogPresenter(self, service)
        self.presenter.get_performances()

        self.set_layout()

    def set_layout(self):
        listbox_layout = Layout([1], fill_frame=False)
        self.add_layout(listbox_layout)
        listbox_layout.add_widget(ListBox(height=10,
                                          options=[(p.name, p.number) for p in self.models.performances],
                                          name=self.LISTBOX_PERFORMANCES,
                                          add_scroll_bar=True,
                                          on_change=self._on_change_performances_listbox), 0)

        performance_information_layout = Layout([1])
        self.add_layout(performance_information_layout)
        performance_information_layout.add_widget(Divider(), 0)
        performance_information_layout.add_widget(Label(height=10, label="", name=self.LABEL_DESCRIPTION), 0)
        performance_information_layout.add_widget(Divider(), 0)

        buttons_layout = Layout([2, 2])
        self.add_layout(buttons_layout)
        buttons_layout.add_widget(Button(text=self.BUTTON_OK_TEXT,
                                         on_click=self._on_click_ok_button,
                                         add_box=True,
                                         name=self.BUTTON_OK), 0)
        buttons_layout.add_widget(Button(text=self.BUTTON_CANCEL_TEXT,
                                         on_click=self._on_click_cancel_button,
                                         add_box=True,
                                         name=self.BUTTON_CANCEL), 1)

        window_information_layout = Layout([1])
        self.add_layout(window_information_layout)

        window_information_layout.add_widget(Label(height=10, label=self.LABEL_INFO_TEXT, name=self.LABEL_INFO), 0)

        self.fix()

    @staticmethod
    def _on_click_cancel_button():
        raise NextScene("Performance")

    def _on_click_ok_button(self):
        self.presenter.set_selected_performance_as_current()
        self._on_click_cancel_button()

    def _on_change_performances_listbox(self):
        performances_listbox = self.find_widget(self.LISTBOX_PERFORMANCES)
        description_label = self.find_widget(self.LABEL_DESCRIPTION)

        for p in self.models.performances:
            if p.number == performances_listbox.value:
                description_label.text = f"{p.name}\nLayers: {p.layers}"
                break

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent):
            if event.key_code in [81, 113]:
                self._on_click_cancel_button()

        return super(PerformancesOpenDialogView, self).process_event(event)

    def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        super(PerformancesOpenDialogView, self).reset()
        self.data = None

    def set_performances_list(self, models: PerformancesOpenDialogViewDataList):
        self.models = models

    def get_selected_performance(self) -> int:
        performances_listbox = self.find_widget(self.LISTBOX_PERFORMANCES)
        return performances_listbox.value
