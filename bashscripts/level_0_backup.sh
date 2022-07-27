#!/bin/bash
#Creates a Level 0 backup of an array of folders

to_backup=("/etc" "/home" "/root" "/var" "/usr/local/bin" "/usr/local/sbin" "/srv" "/opt")
date_year=${date '+%Y'}

prev_metafile_name = $( ls /backup | grep ${$((${date_year}-1))}*.sngz )

# check if an archive metadata file exists from previous year
if [ -f prev_metafile_name]; then
    level=0
    mkdir /backup/backup_tmp
    cd /backup/backup_tmp
    while [ -f "/backup/backup_${level}.tgz" ]; do
        tar --extract --listed-incremental=/dev/null --gzip --file "/backup/backup_${level}.tgz"
        level++
    done
    cd ..
    tar --create --gzip --file="/backup/backup_year_$((${date_year}-1)).tgz" /backup/backup_tmp
    rm prev_metafile_name
fi

# if folder is empty, add "empty" file so tar doesn't complain
for folder in to_backup; do
    if [ -z "$(ls -A ${folder})" ]; then
        touch "${folder}/empty"
    fi

# Do level 0 incremental backup
tar --create --listed-incremental=/backup/${date_year}_backup_meta.sngz --gzip --file=/backup/backup_0.tgz ${to_backup[@]}
