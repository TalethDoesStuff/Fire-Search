# === Textual Imports ===
from textual.widgets import Static


class InfoPanel(Static):
    # Make look like the option list
    DEFAULT_CSS = """
    InformationPanel {
        background: $surface;
        padding: 1;
        height: 100%;
        InformationPanel {
        border: solid $foreground;
        }

        InformationPanel:focus {
            border: solid $accent;
        }
    }
    """

    def update_content(self):
        # Empty string
        content: str = ""

        # Refrence the application selected file infomation for conciseness
        values = self.app.selected_item_info

        # Add each key value pair as a line in content string
        for value in values.keys():
            content += f"{value}: {values[value]}\n"

        # Apply changes
        self.update(content)

    # Sets border
    def on_mount(self):
        self.border_title = "File Info"
