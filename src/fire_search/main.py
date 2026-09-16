# === Textual Imports ===
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, OptionList, Input, Static
from textual.containers import Vertical, Horizontal

# === Project Imports ===
from fire_search.widgets.file_viewer import FileViewer
from fire_search.widgets.info_panel import InfoPanel
from fire_search.widgets.search_bar import SearchBar

# === Other Imports ===
import os


class Application(App):
    def __init__(self, *args, **kwargs):
        self.show_hidden = False
        self.search_filter = ""
        self.selected_item_info = {}
        super().__init__(*args, **kwargs)

    BINDINGS = [
        ('q', "quit", "Quit"),
        ('h', "toggle_hidden", "Show Hidden")
    ]

    def compose(self) -> ComposeResult:
        yield Header()

        viewer = FileViewer(id="file_viewer")
        viewer.styles.width = "70%"
        viewer.styles.height = "100%"

        panel = InfoPanel(id="information_panel")
        panel.styles.width = "30%"
        panel.styles.height = "100%"

        search_bar = SearchBar(id="search_bar")
        search_bar.styles.width = "100%"

        main_content = Horizontal(viewer, panel)
        main_content.styles.height = "1fr"

        yield Vertical(search_bar, main_content)

        yield Footer()

    def refresh_info_panels(self):
        for panel in self.query(InfoPanel):
            panel.update_content()
    def refresh_file_viewers(self):
        for viewr in self.query(FileViewer):
            viewr.update_content()
    def action_toggle_hidden(self) -> None:
        self.show_hidden = not self.show_hidden
        self.refresh_file_viewers()
    def move_to(self, path) -> None:
        try:
            os.chdir(path)
            self.refresh_file_viewers()
        except PermissionError:
            self.title = "   Permission Denied!  "
