from presentation.models.performances.performances_open_dialog_view_data import PerformancesOpenDialogViewData, \
    PerformancesOpenDialogViewDataList
from presentation.presenters.performances.performances_open_dialog_presenter_view import \
    PerformancesOpenDialogPresenterView
from services.midi_controller_service import MidiControllerService


class PerformancesOpenDialogPresenter:
    view: PerformancesOpenDialogPresenterView

    def __init__(self, view: PerformancesOpenDialogPresenterView, service: MidiControllerService):
        self.service = service
        self.view = view

    def get_performances(self):
        controller_config = self.service.get_controller_config()

        p = PerformancesOpenDialogViewDataList(
            performances=[PerformancesOpenDialogViewData(
                name=pc.name,
                number=pc.number,
                layers=len(pc.layers)) for pc in
                self.service.get_performances_config(controller_config)]
        )

        p.performances.sort(key=lambda x: x.number)
        self.view.set_performances_list(p)

    def set_selected_performance_as_current(self):
        performance_id = self.view.get_selected_performance()
        self.service.set_current_performance_by_number(number=performance_id)
