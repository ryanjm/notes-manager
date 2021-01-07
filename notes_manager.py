import os

from os import path, listdir

def count_files(basepath):
    c = {}
    for entry in listdir(basepath):
        if entry.startswith('.'):
            continue
        entrypath = path.join(basepath, entry)
        if path.isdir(entrypath):
            for key,value in count_files(entrypath).items():
                c.setdefault(key, 0)
                c[key] += value

        elif path.isfile(entrypath):
            filename, file_extension = os.path.splitext(entrypath)
            c.setdefault(file_extension, 0)
            c[file_extension] += 1
    return c