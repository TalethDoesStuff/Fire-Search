# === MIME types and their extensions ===

MIMETYPES = {
    # ─────────────────────────────────────────────
    # Text / Documents
    # ─────────────────────────────────────────────
    "text/plain": [
        "txt", "text", "log", "conf", "cfg", "ini", "env",
    ],
    "text/markdown": [
        "md", "markdown", "mdown", "mkdn",
    ],
    "text/html": [
        "html", "htm", "xhtml",
    ],
    "text/css": [
        "css",
    ],
    "text/javascript": [
        "js", "mjs", "cjs",
    ],
    "text/csv": [
        "csv",
    ],
    "text/tab-separated-values": [
        "tsv",
    ],
    "text/xml": [
        "xml",
    ],
    "text/x-python": [
        "py", "pyw", "pyi",
    ],
    "text/x-c": [
        "c", "h",
    ],
    "text/x-c++": [
        "cpp", "cc", "cxx", "hpp", "hh", "hxx",
    ],
    "text/x-java": [
        "java",
    ],
    "text/x-rust": [
        "rs",
    ],
    "text/x-go": [
        "go",
    ],
    "text/x-kotlin": [
        "kt", "kts",
    ],
    "text/x-swift": [
        "swift",
    ],
    "text/x-csharp": [
        "cs",
    ],
    "text/x-shellscript": [
        "sh", "bash", "zsh", "fish",
    ],
    "text/x-lua": [
        "lua",
    ],
    "text/x-ruby": [
        "rb",
    ],
    "text/x-php": [
        "php",
    ],
    "text/x-perl": [
        "pl", "pm",
    ],
    "text/x-dart": [
        "dart",
    ],
    "text/x-sql": [
        "sql",
    ],
    "text/x-makefile": [
        "mk",
    ],

    # ─────────────────────────────────────────────
    # Data / Configuration
    # ─────────────────────────────────────────────
    "application/json": [
        "json", "jsonc", "map",
    ],
    "application/ld+json": [
        "jsonld",
    ],
    "application/yaml": [
        "yaml", "yml",
    ],
    "application/toml": [
        "toml",
    ],
    "application/xml": [
        "xml", "xsl", "xslt",
    ],
    "application/sql": [
        "sql",
    ],
    "application/x-httpd-php": [
        "php",
    ],

    # ─────────────────────────────────────────────
    # PDF / Office
    # ─────────────────────────────────────────────
    "application/pdf": [
        "pdf",
    ],

    "application/msword": [
        "doc",
    ],
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [
        "docx",
    ],

    "application/vnd.ms-excel": [
        "xls",
    ],
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [
        "xlsx",
    ],

    "application/vnd.ms-powerpoint": [
        "ppt",
    ],
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": [
        "pptx",
    ],

    "application/vnd.oasis.opendocument.text": [
        "odt",
    ],
    "application/vnd.oasis.opendocument.spreadsheet": [
        "ods",
    ],
    "application/vnd.oasis.opendocument.presentation": [
        "odp",
    ],
    "application/vnd.oasis.opendocument.graphics": [
        "odg",
    ],
    "application/vnd.oasis.opendocument.formula": [
        "odf",
    ],

    "application/rtf": [
        "rtf",
    ],

    # ─────────────────────────────────────────────
    # Images
    # ─────────────────────────────────────────────
    "image/jpeg": [
        "jpg", "jpeg", "jpe",
    ],
    "image/png": [
        "png",
    ],
    "image/gif": [
        "gif",
    ],
    "image/webp": [
        "webp",
    ],
    "image/svg+xml": [
        "svg", "svgz",
    ],
    "image/bmp": [
        "bmp", "dib",
    ],
    "image/tiff": [
        "tif", "tiff",
    ],
    "image/x-icon": [
        "ico",
    ],
    "image/avif": [
        "avif",
    ],
    "image/heic": [
        "heic",
    ],
    "image/heif": [
        "heif",
    ],
    "image/jxl": [
        "jxl",
    ],
    "image/x-xcf": [
        "xcf",
    ],

    # ─────────────────────────────────────────────
    # Audio
    # ─────────────────────────────────────────────
    "audio/mpeg": [
        "mp3",
    ],
    "audio/wav": [
        "wav",
    ],
    "audio/ogg": [
        "ogg", "oga",
    ],
    "audio/flac": [
        "flac",
    ],
    "audio/mp4": [
        "m4a", "mp4a",
    ],
    "audio/aac": [
        "aac",
    ],
    "audio/webm": [
        "weba",
    ],
    "audio/x-aiff": [
        "aif", "aiff",
    ],
    "audio/x-matroska": [
        "mka",
    ],
    "audio/midi": [
        "mid", "midi",
    ],

    # ─────────────────────────────────────────────
    # Video
    # ─────────────────────────────────────────────
    "video/mp4": [
        "mp4", "m4v",
    ],
    "video/webm": [
        "webm",
    ],
    "video/x-matroska": [
        "mkv",
    ],
    "video/x-msvideo": [
        "avi",
    ],
    "video/mpeg": [
        "mpeg", "mpg", "mpe",
    ],
    "video/quicktime": [
        "mov",
    ],
    "video/x-flv": [
        "flv",
    ],
    "video/3gpp": [
        "3gp",
    ],
    "video/ogg": [
        "ogv",
    ],
    "video/mp2t": [
        "ts", "m2ts",
    ],

    # ─────────────────────────────────────────────
    # Archives / Compression
    # ─────────────────────────────────────────────
    "application/zip": [
        "zip",
    ],
    "application/gzip": [
        "gz",
    ],
    "application/x-bzip2": [
        "bz2",
    ],
    "application/x-xz": [
        "xz",
    ],
    "application/zstd": [
        "zst",
    ],
    "application/x-7z-compressed": [
        "7z",
    ],
    "application/x-rar-compressed": [
        "rar",
    ],
    "application/x-tar": [
        "tar",
    ],
    "application/x-bzip": [
        "bz",
    ],
    "application/x-lzip": [
        "lz",
    ],
    "application/x-lzma": [
        "lzma",
    ],
    "application/x-compress": [
        "Z",
    ],
    "application/x-apple-diskimage": [
        "dmg",
    ],
    "application/x-iso9660-image": [
        "iso",
    ],

    # ─────────────────────────────────────────────
    # Disk / Binary / Executables
    # ─────────────────────────────────────────────
    "application/octet-stream": [
        "bin", "dat", "raw",
    ],
    "application/x-executable": [
        "exe",
    ],
    "application/x-msdownload": [
        "dll", "exe",
    ],
    "application/x-sharedlib": [
        "so",
    ],
    "application/x-object": [
        "o", "obj",
    ],
    "application/x-static-library": [
        "a", "lib",
    ],
    "application/x-elf": [
        "elf",
    ],

    # ─────────────────────────────────────────────
    # Fonts
    # ─────────────────────────────────────────────
    "font/ttf": [
        "ttf",
    ],
    "font/otf": [
        "otf",
    ],
    "font/woff": [
        "woff",
    ],
    "font/woff2": [
        "woff2",
    ],

    # ─────────────────────────────────────────────
    # Web / Programming
    # ─────────────────────────────────────────────
    "application/wasm": [
        "wasm",
    ],
    "application/x-javascript": [
        "jsx",
    ],
    "application/typescript": [
        "ts",
    ],
    "text/tsx": [
        "tsx",
    ],
    "application/graphql": [
        "graphql", "gql",
    ],

    # ─────────────────────────────────────────────
    # Containers / Virtual Machines
    # ─────────────────────────────────────────────
    "application/x-qemu-disk": [
        "qcow", "qcow2",
    ],
    "application/x-vmdk": [
        "vmdk",
    ],
    "application/x-vdi": [
        "vdi",
    ],
    "application/x-vhd": [
        "vhd", "vhdx",
    ],

    # ─────────────────────────────────────────────
    # Git / Dev Files
    # ─────────────────────────────────────────────
    "text/x-diff": [
        "diff", "patch",
    ],
    "application/x-git": [
        "git",
    ],

    # ─────────────────────────────────────────────
    # Game Development / Godot
    # ─────────────────────────────────────────────
    "application/x-godot-project": [
        "godot",
    ],
    "application/x-godot-resource": [
        "res", "tres",
    ],
    "application/x-godot-scene": [
        "scn", "tscn", "escn",
    ],
    "application/x-godot-shader": [
        "gdshader",
    ],
    "text/x-gdscript": [
        "gd",
    ],

    # ─────────────────────────────────────────────
    # Quake / Game Mapping
    # ─────────────────────────────────────────────
    "application/x-quake-map": [
        "map",
    ],
    "application/x-quake-bsp": [
        "bsp",
    ],
    "application/x-quake-pak": [
        "pak",
    ],
}

MISSING_ICON = ""

# === Icons for MIME types ===

ICONS = {
    # Text
    "text/plain": "",
    "text/markdown": "",
    "text/html": "",
    "text/css": "",
    "text/javascript": "",
    "text/csv": "",
    "text/tab-separated-values": "",

    # Programming
    "text/x-python": "",
    "text/x-c": "",
    "text/x-c++": "",
    "text/x-java": "",
    "text/x-rust": "",
    "text/x-go": "",
    "text/x-kotlin": "",
    "text/x-swift": "",
    "text/x-csharp": "󰌛",
    "text/x-shellscript": "",
    "text/x-lua": "",
    "text/x-ruby": "",
    "text/x-php": "",
    "text/x-perl": "",
    "text/x-dart": "",
    "text/x-sql": "",
    "text/x-diff": "",
    "text/x-gdscript": "",

    # Data
    "application/json": "",
    "application/ld+json": "",
    "application/yaml": "",
    "application/toml": "",
    "application/xml": "󰗀",
    "application/sql": "",
    "application/graphql": "",

    # Documents
    "application/pdf": "󰈙",
    "application/rtf": "",

    "application/msword": "",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "󰷈",

    "application/vnd.ms-excel": "󱎏",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "󰧷",

    "application/vnd.ms-powerpoint": "󱎐",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "󰐨",

    "application/vnd.oasis.opendocument.text": "󰷈",
    "application/vnd.oasis.opendocument.spreadsheet": "󰧷",
    "application/vnd.oasis.opendocument.presentation": "󰐨",
    "application/vnd.oasis.opendocument.graphics": "󰏘",
    "application/vnd.oasis.opendocument.formula": "󰐨",

    # Images
    "image/jpeg": "",
    "image/png": "",
    "image/gif": "",
    "image/webp": "",
    "image/svg+xml": "󰜡",
    "image/bmp": "",
    "image/tiff": "",
    "image/x-icon": "",
    "image/avif": "",
    "image/heic": "",
    "image/heif": "",
    "image/jxl": "",
    "image/x-xcf": "",

    # Audio
    "audio/mpeg": "",
    "audio/wav": "󱑽",
    "audio/ogg": "",
    "audio/flac": "",
    "audio/mp4": "",
    "audio/aac": "",
    "audio/webm": "",
    "audio/x-aiff": "",
    "audio/x-matroska": "",
    "audio/midi": "󰎆",

    # Video
    "video/mp4": "",
    "video/webm": "",
    "video/x-matroska": "",
    "video/x-msvideo": "",
    "video/mpeg": "",
    "video/quicktime": "",
    "video/x-flv": "",
    "video/3gpp": "",
    "video/ogg": "",
    "video/mp2t": "",

    # Archives
    "application/zip": "",
    "application/gzip": "",
    "application/x-bzip2": "",
    "application/x-xz": "",
    "application/zstd": "",
    "application/x-7z-compressed": "",
    "application/x-rar-compressed": "",
    "application/x-tar": "",
    "application/x-bzip": "",
    "application/x-lzip": "",
    "application/x-lzma": "",
    "application/x-compress": "",

    # Disk / binaries
    "application/octet-stream": "",
    "application/x-executable": "",
    "application/x-msdownload": "",
    "application/x-sharedlib": "",
    "application/x-object": "",
    "application/x-static-library": "",
    "application/x-elf": "",
    "application/x-apple-diskimage": "󰀲",
    "application/x-iso9660-image": "󰗮",

    # Fonts
    "font/ttf": "",
    "font/otf": "",
    "font/woff": "",
    "font/woff2": "",

    # Web
    "application/wasm": "",
    "application/x-javascript": "",
    "application/typescript": "",
    "text/tsx": "",

    # VM
    "application/x-qemu-disk": "",
    "application/x-vmdk": "",
    "application/x-vdi": "",
    "application/x-vhd": "",

    # Git
    "application/x-git": "",

    # Godot
    "application/x-godot-project": "",
    "application/x-godot-resource": "",
    "application/x-godot-scene": "",
    "application/x-godot-shader": "",

    # Quake
    "application/x-quake-map": "󰈔",
    "application/x-quake-bsp": "󰗮",
    "application/x-quake-pak": "",
}

MISSING_ICON = ""

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