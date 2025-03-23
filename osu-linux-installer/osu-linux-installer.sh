#!/usr/bin/env bash 

# Directory where WINEPREFIX will be created
INSTALL_PATH=$HOME/Games/osu

# Creates Games directory if not exists
if [ ! -d "$HOME/Games" ]; then
    mkdir $HOME/Games
fi

# Creates WINEPREFIX and installs osu! wine dependencies
WINEPREFIX=$INSTALL_PATH wineboot
WINEPREFIX=$INSTALL_PATH winetricks -q dotnet48 corefonts vlgothic meiryo cjkfonts

cd $INSTALL_PATH

# Creates run.sh script
RUNTIME_PATH=$INSTALL_PATH/drive_c/users/$USER/AppData/Local/osu\!/osu\!.exe
echo "#!/usr/bin/env bash" > run.sh
echo "" >> run.sh
echo WINEPREFIX=$INSTALL_PATH wine $RUNTIME_PATH >> run.sh
chmod +x run.sh

# Downloads osu! from website and installs in WINEPREFIX
wget https://m1.ppy.sh/r/osu\!install.exe
WINEPREFIX=$INSTALL_PATH wine $PWD/osu\!install.exe
