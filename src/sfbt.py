#!/usr/bin/env python3
# sfbt.py -- savefile backup tool

import time
from pathlib import Path
import os
import sys
import shutil
import re

savefile_path = {
        'vintagestory': '.config/VintagestoryData/Saves/',
        'kenshi': '233860/pfx/drive_c/users/steamuser/AppData/Local/kenshi/',
        'nier': ('524220/pfx/drive_c/user/steamuser/My Documents/'
                 'My Games/NieR_Automata/'),
        'minecraft': ('.var/app/org.prismlauncher.PrismLauncher/data'
                      '/PrismLauncher/instances/1.21.4/minecraft/saves'),
        'skyrim': ('489830/pfx/drive_c/users/steamuser/Documents/My Games/'
                   'Skyrim Special Edition/Saves'),
        'dishonored2': ('403640/pfx/drive_c/users/steamuser/Saved Games/'
                        'Arkane Studios/Dishonored2/base/savegame'),
        'kingdomcome': ('379430/pfx/drive_c/users/steamuser/'
                        'Saved Games/kingdomcome/saves'),
        'crosscode': ('.config/CrossCode/Default'),
        'stardewvalley': '.config/StardewValley/Saves',
        }

# it needs to be set for games that have savefile in compatdata
steam_games = ['nier', 'kenshi', 'skyrim', 'dishonored2', 'kingdomcome']
steam_compatdata_path = Path(
        '.steam/debian-installation/steamapps/compatdata/')
home_path = Path.home()
target_path = 'backups'

if len(sys.argv) < 2:
    print('type an argument!')
    available_arguments = ', '.join(savefile_path.keys())
    print("available arguments: %s" % available_arguments)
    sys.exit()

argument = sys.argv[1]
backup_filename = argument

# sets source_dir and backup_filename if argument is in dictionary
if argument in steam_games:
    source_path = Path(home_path / steam_compatdata_path
                       / savefile_path[argument])
elif argument in savefile_path:
    source_path = Path(home_path / savefile_path[argument])
else:
    print('no argument named ' + argument + '!')
    sys.exit()

# creates backup directory if backup directory not exist
if not Path(target_path).exists():
    Path(target_path).mkdir()

# directory change
os.chdir(target_path)

# gets last backups mtime and filename
backup_regex = re.compile('%s*' % backup_filename)
backups_dict = {}
with os.scandir(os.getcwd()) as backups:
    for backup in backups:
        if backup.is_file() and backup_regex.match(backup.name) is not None:
            backup_info = os.stat(backup.name)
            backups_dict[backup_info.st_mtime] = backup.name

# keeps 3 backups and removes the oldest backup
if len(backups_dict) > 2:
    oldest_backup = min(backups_dict.keys())
    os.remove(backups_dict[oldest_backup])
    print(f"{backups_dict[oldest_backup]} backup removed!")

# checks if source direcotry exist and creates backup with current localtime
if Path(source_path).exists():
    localtime_format = time.strftime('_%d_%m_%Y_%H_%M_%S', time.localtime())
    backup_filename += localtime_format
    shutil.make_archive(backup_filename, 'zip', source_path)
    print(f"{backup_filename}.zip backup created!")
else:
    print('savefile does not exist in specified path')
