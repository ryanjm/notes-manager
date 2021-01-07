import os

def open_editor(filepath):
    # TODO: Look at grabbing $EDITOR instead
    # Needing full path to exe due to running in Alfred doesn't include path
    os.system(f"/usr/local/bin/code {filepath}")