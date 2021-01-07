# Notes Manager

This is a personal project to manage my notes. I had intended on making this very configuarable and in time, I may do that, but for now, this is based on my current note structures. It does make any changes to your notes structure.

This uses [Click](https://click.palletsprojects.com/) to create a python-based CLI for quickly opening and creating new files. Click is an awesome library and if you are wanting to build a CLI, definetly check it out.

Right now the editor is hard coded to VSCode on my system.

## Instructions

After cloning, to set this up, you need to run the following in this directory:

```
$ pip install --editable .
```

This will install `notes` in your environment and then you can run it by just calling `notes`. See more information on this [here](https://click.palletsprojects.com/en/7.x/setuptools/).

Then you will need to initialize notes to let it know where your notes live. You can change your directory to your notes and run `notes init` or you can pass your directory path to `init`:

```
$ notes init ~/Dropbox/Notes/
```

You can then see the configuration that was created in `~/.notes`.

## Using

To open your notes in VSCode:

```
$ notes
```

You can also check all the commands via `notes --help`.

Right now the commands include:
* `count` - this shows a breakdown of all the file times you have with their count (pass `--total` to get just the total)
* `loc` - to see the location from the config
* `projects`, `areas`, `resources` - all quickly open those folders in the editor
* `journal` - creates a new journal entry (`YYYY-MM-DD.md`) in `/journal`