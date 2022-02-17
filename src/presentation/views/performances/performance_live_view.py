from typing import List, Tuple

from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, MultiColumnListBox, Button, Divider, Label

from presentation.models.performances.performance_live_view_data import PerformanceLiveViewData
from presentation.presenters.performances.performance_live_view_presenter import PerformanceLivePresenter
from presentation.presenters.performances.performance_live_view_presenter_view import PerformanceLivePresenterView


class PerformanceLiveView(Frame, PerformanceLivePresenterView):
    FRAME = "performance_live"
    FRAME_TITLE = "Performance"
    LISTBOX_LAYERS = "layers_listbox"
    LABEL_DESCRIPTION = "description_label"
    BUTTON_OK = "ok_button"
    BUTTON_OK_TEXT = "Ok"
    BUTTON_CANCEL = "cancel_button"
    BUTTON_CANCEL_TEXT = "Cancel"
    LABEL_PERFORMANCE_INFO = "performance_info_label"
    LABEL_INFO = "info_label"
    LABEL_INFO_TEXT = "(q) Close window, \n(TAB) Switch controls, (Up/Down key) - Select performance"
    BUTTON_LOAD_PERFORMANCE = "load_performance_button"
    BUTTON_LOAD_PERFORMANCE_TEXT = "Load Performance..."

    def __init__(self, screen, service):
        self.presenter = PerformanceLivePresenter(self, service)
        self.presenter.get_current_performance()

        super(PerformanceLiveView, self).__init__(screen,
                                                  height=screen.height,
                                                  width=screen.width,
                                                  y=0,
                                                  has_border=True,
                                                  can_scroll=False,
                                                  name=self.FRAME,
                                                  on_load=self._reload_frame)

        self.set_layout()

    def set_layout(self):

        layout_top = Layout([1, 1, 1, 1], fill_frame=False)
        self.add_layout(layout_top)
        layout_top.add_widget(Button(text=self.BUTTON_LOAD_PERFORMANCE,
                                     on_click=self._open_file,
                                     add_box=True,
                                     name=self.BUTTON_LOAD_PERFORMANCE_TEXT), 0)

        layers_layout = Layout([1], fill_frame=False)
        self.add_layout(layers_layout)

        self.layers_listbox = MultiColumnListBox(height=15,
                                                 columns=[">2", ">4", "^5", ">4", ">6", ">6", ">6", ">4", ">5", "^5",
                                                          "^4", ">3", ">6q"],
                                                 options=self.render_layers_for_listbox(self.model),
                                                 titles=["#", "Cha", "Ena", "L.Key", "U.Key", "L.Vel", "U.Vel",
                                                         "Oct", "Tran", "F.V", "K.N", "Pro", "C.C."],
                                                 on_change=self._on_change_layers_listbox
                                                 )

        layers_layout.add_widget(Divider())
        self.performance_info_label = Label(height=4, label="", name=self.LABEL_PERFORMANCE_INFO)

        layers_layout.add_widget(self.performance_info_label)

        layers_details_layout = Layout([65, 5, 30], fill_frame=True)
        self.add_layout(layers_details_layout)

        layers_details_layout.add_widget(self.layers_listbox, 0)

        self.continuous_controller_layer_listbox = MultiColumnListBox(height=15,
                                                                      columns=["^7", "^18", "^5", "^5", "^8"],
                                                                      options=self.render_continuous_controller_layer_for_listbox(
                                                                          self.model, 1),
                                                                      titles=["Layer", "Controller change", "Min",
                                                                              "Max", "Glo. Ch."],
                                                                      add_scroll_bar=True
                                                                      )
        self.continuous_controller_layer_listbox.disabled = True
        layers_details_layout.add_widget(self.continuous_controller_layer_listbox, 2)

        self.fix()

    @staticmethod
    def _open_file():
        raise NextScene("PerformancesOpenDialog")

    def _on_change_layers_listbox(self):
        self._reload_continuous_controller_layer_listbox(self.layers_listbox.value)

    def _reload_frame(self, new_value=None):
        self.presenter.get_current_performance()

        self._reload_performance_info()
        self._reload_listbox()
        self._reload_continuous_controller_layer_listbox(1)
        self._set_title_frame()

    def _reload_performance_info(self):
        self.performance_info_label.text = f"{self.model.number}: {self.model.name}\n" \
                                           f"Min BMP: {self.model.tempo_config.min_bpm} ~ Max BMP: {self.model.tempo_config.max_bpm}\n" \
                                           f"{self.model.time_signature.beats_per_bar}/{self.model.time_signature.beat_unit}"

    def _reload_listbox(self):
        self.layers_listbox.options = self.render_layers_for_listbox(self.model)

    def _reload_continuous_controller_layer_listbox(self, layer_number: int):
        self.continuous_controller_layer_listbox.options = self.render_continuous_controller_layer_for_listbox(
            self.model, layer_number)

    def _set_title_frame(self):
        self.title = f"{self.FRAME_TITLE} - {self.model.name}"

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent):
            if event.key_code in [81, 113]:
                raise NextScene("Menu")

        return super(PerformanceLiveView, self).process_event(event)

    def set_current_performance(self, model: PerformanceLiveViewData) -> None:
        self.model = model

    def render_layers_for_listbox(self, model: PerformanceLiveViewData) -> List[Tuple]:
        result = []

        for l in model.layers:
            result.append(
                (
                    [str(l.number),
                     str(l.channel),
                     "Y" if l.active else "N",
                     l.note_range_config.lower_key,
                     l.note_range_config.upper_key,
                     str(l.velocity_range_config.min_velocity),
                     str(l.velocity_range_config.max_velocity),
                     str(l.octave),
                     str(l.transportation),
                     str(l.fix_velocity) if l.fix_velocity else "N",
                     "Y" if l.keep_note_on_until_touch_it_again else "N",
                     str(l.program),
                     str(len(l.controller_changes))
                     ],
                    l.number
                )
            )
        return result

    def render_continuous_controller_layer_for_listbox(self, model: PerformanceLiveViewData, layer_number: int) -> List[
        Tuple]:
        result = []

        for l in model.layers:
            if l.number == layer_number:
                for i, cc in enumerate(l.controller_changes):
                    result.append(
                        ([str(l.number),
                          cc.continues_controller,
                          str(cc.min),
                          str(cc.max),
                          str(cc.use_global_channel)
                          ], i))
                break
        return result
