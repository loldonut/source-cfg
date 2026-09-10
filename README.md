## Source Games Config Files

My config files for Source Games to make it work on my system and on Linux

### Installing

Folders for specific games should have an install script *when needed*

### Get game params

The game parameters used on Steam are generated through [game-params](https://github.com/loldonut/game-params)

## Format `autoexec.cfg`

To make the tab width consistent you can use the CLI tool provided in this repo:

```sh
python3 fmt_cfg.py autoexec.cfg
```

### usage

```
usage: fmt_cfg.py [-h] [-t TAB_WIDTH] file

Align CFG variables into clean columns.

positional arguments:
  file                  Path to the .cfg file

options:
  -h, --help            show this help message and exit
  -t, --tab-width TAB_WIDTH
                        Spaces after the longest variable (default: 5)
```
