import click

from notes_manager import count_files
from editor_manager import open_editor
from config_manager import source_path, init_config, current_dir
from template_manager import new_journal


@click.group(invoke_without_command=True)
@click.version_option(message='%(prog)s version %(version)s')
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        open_editor(source_path())


########################################
# Initializer
########################################

@cli.command()
@click.argument('source', 
    required=False, 
    default=current_dir(), 
    type=click.Path(exists=True, file_okay=False, allow_dash=False)
    )
def init(source):
    """Initializes ~/.notes with the location of your notes"""
    init_config(source)
    click.echo("Initialized source of notes. Notes is now ready.")


########################################
# Quick folder actions
########################################

@cli.command()
def projects():
    """Opens /projects"""
    open_editor(f"{source_path()}/projects")

@cli.command()
def areas():
    """Opens /areas"""
    open_editor(f"{source_path()}/areas")

@cli.command()
def resources():
    """Opens /resources"""
    open_editor(f"{source_path()}/resources")


########################################
# Templates
########################################

@cli.command()
def journal():
    """Creates a new journal entry (`YYYY-MM-DD.md`) in `/journal`"""
    open_editor(new_journal())


########################################
# Helper commands
########################################

@cli.command()
def loc():
    """Location of the notes"""
    click.echo(source_path())

@cli.command()
@click.option('--total', default=False, is_flag=True, flag_value=True, help='Show only total count')
def count(total):
    """Count of all notes (skips dot files)"""
    counts = count_files(source_path())

    total_count = 0
    for file_type, count in counts.items():
        if total == False:
            click.echo(f"{file_type}\t\t{count}")
        total_count += count
    if total:
        click.echo(total_count)
    else:
        click.echo(f"Total:\t\t{total_count}")