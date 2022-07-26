#!/bin/bash
#Creates a Level 0 backup of an array of folders

to_backup=("/etc" "/home" "/root" "/var" "/usr/local/bin" "/usr/local/sbin" "/srv" "/opt")
date_year=${date '+%Y'}

#if folder is empty, add "empty" file so tar doesn't complain
for folder in to_backup; do
    if [ -z "$(ls -A ${folder})" ]; then
        touch "${folder}/empty"

Do level 0 incremental backup
tar --extract --listed-incremental=/backup/${date_year}_level_0.sngz --file=/backup ${to_backup[@]}
