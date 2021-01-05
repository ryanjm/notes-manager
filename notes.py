import click
import os.path
import json
from os import path

@click.group()
@click.version_option(message='%(prog)s version %(version)s')
def cli():
    pass

def get_source_path():
    notespath = "."
    p = path.expanduser("~/.notes")
    with open(p, 'r') as f:
        notespath = json.load(f)["source"]
    return notespath

@cli.command()
@click.argument('source', 
    required=False, 
    default=os.getcwd(), 
    type=click.Path(exists=True, file_okay=False, allow_dash=False)
    )
def init(source):
    """Initializes ~/.notes with the location of your notes"""
    s = path.expanduser(source)
    p = path.expanduser("~/.notes")
    config = {"source": s}
    with open(p, 'w+') as f:
        json.dump(config, f, indent=4)
    click.echo("Initialized source of notes. Notes is now ready.")

@cli.command()
def loc():
    """Location of the notes"""
    click.echo(get_notes_path())

def count_files(basepath):
    c = 0
    for entry in os.listdir(basepath):
        if entry.startswith('.'):
            continue
        entrypath = path.join(basepath, entry)
        if path.isdir(entrypath):
            c = c + count_files(entrypath)
        elif path.isfile(entrypath):
            c = c + 1
    return c

@cli.command()
def count():
    """Count of all notes"""
    basepath = get_source_path()
    click.echo(count_files(basepath))

@cli.command()
def o():
    """open your notes in VSCode"""
    basepath = get_source_path()
    os.system(f"code {basepath}")