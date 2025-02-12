#!/usr/bin/python3
# sfbt.py -- savefile backup tool

import time
from pathlib import Path
import os
import sys
import shutil


savefile_path = {
        'vintagestory': '.config/VintagestoryData/Saves/',
        'kenshi': '233860/pfx/drive_c/users/steamuser/AppData/Local/kenshi/',
        'nier': ('524220/pfx/drive_c/user/steamuser/My Documents/'
                 'My Games/NieR_Automata/'),
        'minecraft': ('.var/app/org.prismlauncher.PrismLauncher/data'
                      '/PrismLauncher/instances/1.21.4/minecraft/saves'),
        'skyrim': ('489830/pfx/drive_c/users/steamuser/Documents/My Games/'
                   'Skyrim Special Edition/Saves'),
        }

steam_games = ['nier', 'kenshi', 'skyrim']
steam_compatdata_path = Path(
        '.steam/debian-installation/steamapps/compatdata/')
home_path = Path.home()
target_path = 'backups'

if len(sys.argv) < 2:
    print('Type an argument!')
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
    print('No argument named ' + argument + '!')
    sys.exit()

# creates backup directory if backup directory not exist
if not Path(target_path).exists():
    Path(target_path).mkdir()

# checks if source direcotry exist and creates backup with current localtime
if Path(source_path).exists():
    localtime_format = time.strftime('_%d_%m_%Y_%H_%M_%S', time.localtime())
    os.chdir(target_path)
    shutil.make_archive(backup_filename + localtime_format, 'zip', source_path)
    print(f"{argument} backup successful!")
else:
    print('Source directory does not exist :(')
