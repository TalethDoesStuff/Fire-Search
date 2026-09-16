# === Project Imports ===
from fire_search.constants import (
    MIMETYPES,
    MISSING_ICON,
    ICONS,
    HIDDEN_DIR,
    HIDDEN_FILE,
    FOLDER_ICON,
)

# === Other Imports ===
from pathlib import Path
import os, sys, subprocess


# Uses the operating system's tool to open a file
def open_file(path):
    if sys.platform == "win32":
        os.startfile(path)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


# Returns a char of the nerd font icon to use
def get_icon(path: Path) -> str:
    extension = path.suffix.lower().lstrip(".")
    if path.name.startswith("."):
        if path.is_dir():
            return HIDDEN_DIR
        else:
            return HIDDEN_FILE
    if path.is_dir():
        return FOLDER_ICON
    for mime_type, extensions in MIMETYPES.items():
        if extension in extensions:
            return ICONS.get(mime_type, MISSING_ICON)

    return MISSING_ICON


# Returns the mimetype (located in constants.py)
def get_mimetype(path) -> str:
    extension = path.suffix.lower().lstrip(".")

    if path.is_dir():
        return "directory"  # Meh

    for mime_type, extensions in MIMETYPES.items():
        if extension in extensions:
            return mime_type

    return "none"  # Will evalulate to MISSING_ICON in get_icon
