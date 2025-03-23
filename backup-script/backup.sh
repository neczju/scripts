#!/usr/bin/env bash

source_path=$HOME/
destination_path=/media/usbstick/backup

if [ ! -d "$destination_path" ]; then
    mkdir -p $destination_path
fi

rsync -a -v --delete --progress --filter="merge backup_filter" $source_path $destination_path
