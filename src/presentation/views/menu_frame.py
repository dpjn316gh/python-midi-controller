from asciimatics.exceptions import NextScene, StopApplication
from asciimatics.widgets import Frame, Layout, Button, PopUpDialog, PopupMenu


class MenuFrame(Frame):
    def __init__(self, screen):
        super(MenuFrame, self).__init__(screen,
                                        height=3,
                                        width=screen.width,
                                        y=0,
                                        has_border=True,
                                        can_scroll=False,
                                        name="Menu Form",
                                        title="Virtual Midi Controller - Menu")
        layout = Layout([1, 1, 1, 1, 1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("Configuration", self._open_configuration, add_box=False), 0)
        layout.add_widget(Button("Midi Interfaces", self._open_midi_interfaces, add_box=False), 1)
        layout.add_widget(Button("Performances", self._open_performance, add_box=False), 2)
        layout.add_widget(Button("Virtual Controller", self._quit, add_box=False), 3)
        layout.add_widget(Button("Exit", self._quit, add_box=False), 4)

        self.fix()

    def _open_configuration(self):
        raise NextScene("Configuration")

    def _open_file_menu(self):
        raise NextScene("Files")

    def _open_performance(self):
        raise NextScene("Performance")

    def _quit(self):
        popup = PopUpDialog(self._screen, "Are you sure?", ["Yes", "No"],
                    has_shadow=True, on_close=self._quit_on_yes)
        self._scene.add_effect(popup)

    def _open_midi_interfaces(self):
        popup = PopupMenu(self._screen,[('elemento 1', self._menu_1), ('elemento 2', self._menu_2)], 5, 5)
        self._scene.add_effect(popup)

    def _menu_1(self):
        self.screen.refresh()

    def _menu_2(self):
        self.screen.refresh()

    def _quit_on_yes(self, selected):
        # Yes is the first button
        if selected == 0:
            raise StopApplication("User requested exit")
        else:
            raise NextScene("Menu")