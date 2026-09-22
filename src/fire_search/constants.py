# Mimetypes and their extentions
MIMETYPES = {
    "text/plain": ["txt"],
    "text/markdown": ["md", "markdown"],
    "text/html": ["html", "htm"],
    "text/css": ["css"],
    "text/javascript": ["js"],
    "application/json": ["json"],
    "application/xml": ["xml"],
    "application/pdf": ["pdf"],
    "image/jpeg": ["jpg", "jpeg"],
    "image/png": ["png"],
    "image/gif": ["gif"],
    "image/webp": ["webp"],
    "image/svg+xml": ["svg"],
    "audio/mpeg": ["mp3"],
    "audio/wav": ["wav"],
    "video/mp4": ["mp4"],
    "video/webm": ["webm"],
    "application/zip": ["zip"],
    "application/x-tar": ["tar"],
    "application/x-rar-compressed": ["rar"],
    "application/x-7z-compressed": ["7z"],
    "application/vnd.ms-excel": ["xls", "xlsx"],
    "application/vnd.ms-powerpoint": ["ppt", "pptx"],
    "application/msword": ["doc", "docx"],
    "application/vnd.oasis.opendocument.text": ["odt"],
    "application/vnd.oasis.opendocument.spreadsheet": ["ods"],
    "application/vnd.oasis.opendocument.presentation": ["odp"],
    "application/vnd.oasis.opendocument.graphics": ["odg"],
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ["docx"],
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ["xlsx"],
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": [
        "pptx"
    ],
    "application/x-godot-project": ["godot"],
    "application/x-godot-resource": ["res", "tres"],
    "application/x-godot-scene": ["scn", "tscn", "encn"],
    "application/x-godot-shader": ["gdshader"],
}

MISSING_ICON = ""

# Icon for each mimetype
ICONS = {
    "text/plain": "",
    "text/markdown": "",
    "text/html": "",
    "text/css": "",
    "text/javascript": "",
    "application/json": "",
    "application/xml": "󰗀",
    "application/pdf": "󰈙",
    "image/jpeg": "",
    "image/png": "",
    "image/gif": "",
    "image/webp": "",
    "image/svg+xml": "",
    "audio/mpeg": "🎵",
    "audio/wav": "🎵",
    "video/mp4": "",
    "video/webm": "",
    "application/zip": "",
    "application/x-tar": "",
    "application/x-rar-compressed": "",
    "application/x-7z-compressed": "",
    "application/vnd.ms-excel": "󱎏",
    "application/vnd.ms-powerpoint": "󱎐",
    "application/msword": "",
    "application/vnd.oasis.opendocument.text": "📝",
    "application/vnd.oasis.opendocument.spreadsheet": "📊",
    "application/vnd.oasis.opendocument.presentation": "📽️",
    "application/vnd.oasis.opendocument.graphics": "🎨",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "📝",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "📊",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "📽️",
    "application/x-godot-project": "",
}

# Shown in the title
PROJECT_NAME = "Fire Search"

# Icon used for folders
FOLDER_ICON="󰉋"

# Folder and file icon for ALL hidden files and folders
HIDDEN_DIR = "󱞞"
HIDDEN_FILE = "󰘓"

HELP_MESSAGE = """Fire Search (FIre SEarch -> FISE)
fise [options] [location]

Options:
-h --help | displays this menu
-H --show-hidden | shows hidden files by default (Not implemented)

Credits:
@TalethDoesStuff
"""