from abc import abstractmethod, ABC

from presentation.models.performances.performances_open_dialog_view_data import PerformancesOpenDialogViewDataList, \
    PerformancesOpenDialogViewData


class PerformancesOpenDialogPresenterView(ABC):
    @abstractmethod
    def set_performances_list(self, model: PerformancesOpenDialogViewDataList):
        raise NotImplementedError

    @abstractmethod
    def get_selected_performance(self) -> int:
        raise NotImplementedError
