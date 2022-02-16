from presentation.models.performances.performance_live_view_data import PerformanceLiveViewData
from presentation.presenters.performances.performance_live_view_presenter_view import PerformanceLivePresenterView
from services.midi_controller_service import MidiControllerService


class PerformanceLivePresenter:
    view: PerformanceLivePresenterView

    def __init__(self, view: PerformanceLivePresenterView, service: MidiControllerService):
        self.service = service
        self.view = view

    def get_current_performance(self):
        controller_config = self.service.get_controller_config()
        performance_config = self.service.get_current_performance(controller_config)
        current_performance = PerformanceLiveViewData(**performance_config.dict())
        self.view.set_current_performance(current_performance)
