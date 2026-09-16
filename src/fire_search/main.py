# === Textual Imports ===
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, OptionList, Input, Static
from textual.containers import Vertical, Horizontal

# === Project Imports ===
from fire_search.widgets.file_viewer import FileViewer
from fire_search.widgets.info_panel import InfoPanel


class Application(App):
    def __init__(self, *args, **kwargs):
        self.show_hidden = False
        self.selected_item_info = {}
        super().__init__(*args, **kwargs)

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()

        viewer = FileViewer(id="file_viewer")
        viewer.styles.width = "70%"
        viewer.styles.height = "100%"

        panel = InfoPanel(id="information_panel")
        panel.styles.width = "30%"
        panel.styles.height = "100%"

        action_panel = Static(id="action_panel")
        action_panel.styles.width = "100%"
        action_panel.styles.height = "20%"

        f = Horizontal(viewer, panel)
        f.styles.height = "1fr"

        yield Vertical(f, action_panel)

        yield Footer()

    def refresh_info_panels(self):
        for panel in self.query(InfoPanel):
            panel.update_content()
