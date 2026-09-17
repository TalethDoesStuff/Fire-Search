from textual.widgets import OptionList
from textual.widgets.option_list import Option


class InfoPanel(OptionList):
    def update_content(self):
        self.clear_options()

        values = self.app.selected_item_info

        for key, value in values.items():
            self.add_option(
                Option(f"{key}: {value}")
            )

    def on_mount(self):
        self.border_title = "File Info"
