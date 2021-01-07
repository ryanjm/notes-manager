import os

from os import path
from datetime import datetime

from config_manager import source_path

def new_journal():
    basepath = source_path()
    date_str = datetime.now().strftime("%F")
    todays_journal = path.join(basepath, 'journal', f"{date_str}.md")
    if not path.exists(todays_journal):
        with open(todays_journal, 'w') as f:
            f.write(f"# {date_str}\n\n")
    return todays_journal