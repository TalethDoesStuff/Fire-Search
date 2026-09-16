import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "Fire-Search"
copyright = "2026, TalethDoesStuff"
author = "TalethDoesStuff"
release = "0.1.0"

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_favicon = "_static/fire_search.png"
html_logo = "_static/fire_search.png"