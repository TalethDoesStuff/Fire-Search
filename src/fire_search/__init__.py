from fire_search.main import Application
from pathlib import Path
import os, sys
from fire_search.constants import HELP_MESSAGE

def main() -> None:
    args = sys.argv[1:]
    
    for arg in args:
        match arg:
            case "-h" | "--help":
                print(HELP_MESSAGE)
                quit()

    app = Application()
    app.run()

if __name__ == "__main__":
    main()