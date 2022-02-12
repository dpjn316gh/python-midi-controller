from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, Button, FileBrowser

from src.presentation.models.file_open_dialog_view_data import FileOpenDialogViewData
from src.presentation.presenters.file_open_dialog_presenter import FileOpenDialogPresenter
from src.presentation.presenters.file_open_dialog_presenter_view import FileOpenDialogPresenterView


class FileOpenDialogView(Frame, FileOpenDialogPresenterView):

    def set_root(self, model: FileOpenDialogViewData):
        self.model = model

    def get_selected_file(self) -> FileOpenDialogViewData:
        filebrowser = self.find_widget(self.FILEBROWSER_NAME)
        self.model.selected_file = filebrowser.value
        return self.model

    FILE_OPEN_DIALOG_VIEW_NAME = "performance_view"
    FILE_OPEN_DIALOG_VIEW_TITLE = "Virtual Midi Controller - Select Performance"
    BUTTON_OK = "Select"
    BUTTON_CANCEL = "Cancel"
    FILEBROWSER_NAME = "filebrowser"

    def __init__(self, screen, service):
        super(FileOpenDialogView, self).__init__(screen,
                                                 height=screen.height // 2,
                                                 width=screen.width // 2,
                                                 has_border=True,
                                                 can_scroll=False,
                                                 name=self.FILE_OPEN_DIALOG_VIEW_NAME,
                                                 title=self.FILE_OPEN_DIALOG_VIEW_TITLE)

        self.model = FileOpenDialogViewData()

        self.presenter = FileOpenDialogPresenter(self, service)
        self.presenter.get_root()

        self.set_layout()

    def set_layout(self):
        layout_top = Layout([100], fill_frame=False)
        self.add_layout(layout_top)
        layout_top.add_widget(FileBrowser(name=self.FILEBROWSER_NAME,
                                          height=self.screen.height // 3,
                                          root=self.model.root,
                                          on_select=self._on_select_event
                                          ), 0)

        layout_bottom = Layout([1, 1])
        self.add_layout(layout_bottom)

        layout_bottom.add_widget(Button(self.BUTTON_OK, self._ok_event, add_box=True), 0)
        layout_bottom.add_widget(Button(self.BUTTON_CANCEL, self._cancel_event, add_box=True), 1)

        self.fix()

    @staticmethod
    def _cancel_event():
        raise NextScene("Performance")

    def _ok_event(self):
        self.presenter.set_selected_file()
        self._cancel_event()

    def _on_select_event(self):
        self.presenter.set_selected_file()

    def process_event(self, event):
        if event is not None and isinstance(event, KeyboardEvent):
            if event.key_code in [81, 113]:
                self._cancel_event()

        return super(FileOpenDialogView, self).process_event(event)
