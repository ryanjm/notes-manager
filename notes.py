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
    c = {}
    for entry in os.listdir(basepath):
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

@cli.command()
@click.option('--total', default=False, is_flag=True, flag_value=True, help='Show only total count')
def count(total):
    """Count of all notes (skips dot files)"""
    basepath = get_source_path()
    counts = count_files(basepath)
    total_count = 0
    for file_type, count in counts.items():
        if total == False:
            click.echo(f"{file_type}\t\t{count}")
        total_count += count
    if total:
        click.echo(total_count)
    else:
        click.echo(f"Total:\t\t{total_count}")
    

@cli.command()
def o():
    """open your notes in VSCode"""
    basepath = get_source_path()
    os.system(f"code {basepath}")