# === Textual Imports ===
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, OptionList, Input, Static
from textual.containers import Vertical, Horizontal

# === Project Imports ===
from fire_search.widgets.file_viewer import FileViewer
from fire_search.widgets.info_panel import InfoPanel
from fire_search.widgets.search_bar import SearchBar

# === Other Imports ===
import os, sys, subprocess
from pathlib import Path

class Application(App):
    def __init__(self, *args, **kwargs):
        self.show_hidden = False
        self.search_filter = ""
        self.selected_item_info = {}
        super().__init__(*args, **kwargs)

    BINDINGS = [
        ('q', "quit", "Quit"),
        ('h', "toggle_hidden", "Show Hidden"),
        ('`', "go_home", "Go Home"),
        ('/', "go_root", "Go Root"),
        ('u', "go_up", "Go Up")
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
        """Updates the infomation panel(s)"""
        for panel in self.query(InfoPanel):
            panel.update_content()

    def refresh_file_viewers(self):
        """Updates the file viewer(s)"""
        for viewr in self.query(FileViewer):
            viewr.update_content()
    
    def action_toggle_hidden(self) -> None:
        """Toggles the visibility of hidden files"""
        self.show_hidden = not self.show_hidden
        self.refresh_file_viewers()
    
    def move_to(self, path) -> None:
        """Moves to a folder/dir"""
        try:
            os.chdir(path)
            self.refresh_file_viewers()
        except PermissionError:
            self.title = "   Permission Denied!  "
    def action_go_home(self) -> None:
        """Go to the home directory"""
        self.move_to(Path.home())
    def action_go_root(self) -> None:
        """Go to the root directory"""
        self.move_to(Path(Path.cwd().anchor))
    def action_go_up(self) -> None:
        """Goes up one dir"""
        try:
            self.move_to(Path.cwd().parent)
        except:
            self.title = "Cannot go up any further"

    def open_file(self, path):
        """Open a file"""

        if sys.stdin.isatty():
            with self.suspend():
                subprocess.run(["vim", str(path)])

            return

        if sys.platform == "win32":
            os.startfile(path)

        elif sys.platform == "darwin":
            result = subprocess.run(
                ["open", str(path)],
                capture_output=True,
                text=True,
            )

            if result.stderr:
                self.title = "Failed to open file!"

        else:
            result = subprocess.run(
                ["xdg-open", str(path)],
                capture_output=True,
                text=True,
            )

            if result.stderr:
                self.title = "Failed to open file!"
