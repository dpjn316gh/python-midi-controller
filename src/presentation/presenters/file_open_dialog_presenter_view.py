from abc import abstractmethod, ABC

from src.presentation.models.file_open_dialog_view_data import FileOpenDialogViewData


class FileOpenDialogPresenterView(ABC):
    @abstractmethod
    def set_root(self, model: FileOpenDialogViewData):
        raise NotImplementedError

    @abstractmethod
    def get_selected_file(self) -> FileOpenDialogViewData:
        raise NotImplementedError
