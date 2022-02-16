from abc import ABC, abstractmethod

from presentation.models.performances.performance_live_view_data import PerformanceLiveViewData


class PerformanceLivePresenterView(ABC):
    @abstractmethod
    def set_current_performance(self, performance: PerformanceLiveViewData) -> None:
        raise NotImplementedError
