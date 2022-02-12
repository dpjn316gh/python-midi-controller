from src.presentation.models.file_open_dialog_view_data import FileOpenDialogViewData
from src.presentation.presenters.file_open_dialog_presenter_view import FileOpenDialogPresenterView
from src.services.midi_controller_service import MidiControllerService


class FileOpenDialogPresenter:
    view: FileOpenDialogPresenterView

    def __init__(self, view: FileOpenDialogPresenterView, service: MidiControllerService):
        self.service = service
        self.view = view

    def get_root(self):
        controller_config = self.service.get_controller_config()

        file_open_data = FileOpenDialogViewData(
            root=controller_config.performances_folder_path,
            selected_file=controller_config.default_performance)

        self.view.set_root(file_open_data)

    def set_selected_file(self):
        model = self.view.get_selected_file()

        # performance = self.service.get_performance(model.selected_file)
        self.service.set_current_performance(performance)

