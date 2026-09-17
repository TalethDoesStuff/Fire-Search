# === Textual Imports ===
from textual.app import ComposeResult
from textual.widgets import Input, Label
from textual import on


class SearchBar(Input):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # On update apply the filter to the file viewer
    @on(Input.Changed)
    def update_search_filter(self, event: Input.Changed):
        self.app.search_filter = event.value
        self.app.refresh_file_viewers()
        self.app.refresh_info_panels()
    
    def on_mount(self):
        self.border_title = "Search Bar"