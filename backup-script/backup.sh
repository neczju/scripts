#!/usr/bin/env bash

source_path=$HOME/
destination_path=/run/media/neczju/716a0a85-57c0-46ee-84ba-a7ed3a810d53/backup

if [ ! -d "$destination_path" ]; then
    mkdir -p $destination_path
fi

rsync -a -v --delete --progress --filter="merge backup_filter" $source_path $destination_path
