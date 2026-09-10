# Left 4 Dead 2 config files

My Left 4 Dead 2 config files

## Install Script (Linux Only)

**Note:** The steam config files symlinks to `$HOME/.local/share/Steam/steamapps/common/Left 4 Dead 2/left4dead2/cfg`, so Steam installed through flatpak won't work.

```sh
./install
```

This installs the Steam L4D2 config files *and* old verions of left 4 dead 2 found in a specific folder used for speedrunning the game.

## Old versions install path

It detects folders at `$HOME/l4d2` which has a format of `L4D2-v[VERSION]` like this:

```
/home/USER/l4d2
├── L4D2-v2.0.0.0
├── L4D2-v2.0.1.2
├── L4D2-v2.0.2.7
├── L4D2-v2.0.4.5
└── L4D2-v2.0.9.1
```

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
