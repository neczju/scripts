source_path=$HOME/
destination_path=/run/media/neczju/259a6399-8a96-4211-b291-35b132154195/backup

if [ ! -d "$destination_path" ]; then
    mkdir -p $destination_path
fi

rsync -a -v --delete --progress --exclude-from="rsync_filter" $source_path $destination_path
