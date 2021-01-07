import os
import json

from os import path

def init_config(source):
    s = path.expanduser(source)
    p = path.expanduser("~/.notes")
    config = {"source": s}
    with open(p, 'w+') as f:
        json.dump(config, f, indent=4)

def source_path():
    notespath = "."
    p = path.expanduser("~/.notes")
    with open(p, 'r') as f:
        notespath = json.load(f)["source"]
    return notespath

def current_dir():
    return os.getcwd()