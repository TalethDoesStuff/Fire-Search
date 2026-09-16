from fire_search.main import Application
from pathlib import Path


def main() -> None:
    print(Path.cwd())
    app = Application()
    app.run()
