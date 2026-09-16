# === Textual Imports ===
from textual.widgets import OptionList
from textual.widgets.option_list import Option

# === Project Imports ===
from fire_search.constants import ICONS, MIMETYPES, MISSING_ICON, PROJECT_NAME
from fire_search.functions import get_icon, get_mimetype, open_file

# === Other Imports ===
from pathlib import Path
import os


class FileViewer(OptionList):
    def on_mount(self) -> None:
        self.update_content()

    def update_content(self) -> None:

        # Remove options before adding more.
        self.clear_options()

        # If cannot go up do not show ../
        if Path.cwd() != Path.cwd().parent:
            self.add_option(Option("󱧪  ..", id=".."))

        try:
            # Try to sort the list then add a message if it failed.
            entries = sorted(
                Path.cwd().iterdir(),
                key=lambda path: (not path.is_dir(), path.name.lower()),
            )
        except PermissionError:
            self.add_option(Option("󰉘  Permission denied", id="error"))
            return

        for entry in entries:
            # Skip this item if show_hidden is not enabled and is this file is hidden
            if entry.name.startswith(".") and not self.app.show_hidden:
                continue

            # If dir then add 󰉋 and / else searh mimetype and get icon
            if entry.is_dir():
                self.add_option(Option(f"󰉋  {entry.name}/", id=str(entry)))
            else:
                self.add_option(
                    Option(f"{get_icon(entry)} {entry.name}", id=str(entry))
                )
        # Update the title to this dir
        self.app.title = f"{PROJECT_NAME} — {Path.cwd()}/"

    # Update info panel and title when highlighted item
    def on_option_list_option_highlighted(
        self, event: OptionList.OptionHighlighted
    ) -> None:

        # Get selected option infomation
        option = event.option
        option_id = event.option.id
        path = Path(option_id)

        # Set app title
        self.app.title = f"{PROJECT_NAME} — {Path.cwd()}/{option.prompt[2:]}"

        # Update selected info in app
        info = self.app.selected_item_info

        info["file"] = option.prompt[2:]
        info["location"] = (
            str(path.parent.absolute()).replace(str(Path.home()), "~") + "/"
        )
        info["type"] = str(get_mimetype(path))
        self.app.refresh_info_panels()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        option_id = event.option.id

        if option_id == "..":
            os.chdir(Path.cwd().parent)
            self.update_content()
            return

        if option_id == "error":
            return

        path = Path(option_id)

        if path.is_dir():
            try:
                os.chdir(path)
                self.update_content()
            except OSError:
                self.app.title = " Permission Denied! "
        else:
            open_file(path)
