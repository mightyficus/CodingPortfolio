#!/bin/bash
# Create incremental backups using rsync with hard links
# Current impementation meant for daily backups

# TODO: Implement arguments for customizability- number of backups, date interval, source and destination folders

current_date=$(date)
to_backup=("/etc" "/home" "/root" "/var" "/usr/local/bin" "/usr/local/sbin" "/srv" "/opt")
# number of backups to keep
backup_backlog=10

# Change to backup folder
cd /backup

# rotate backups
# wildcard allows for missing days due to downtime (using async scheduler)
rm -rf backup.*.${backup_backlog}
#3 condition for loop needed because of bash script limitations
for (( log_number=$backup_backlog; log_number >= 2; log_number-- )); do
    log_date=$(ls | grep "backup.*.$((${log_number}-1))" | cut -d'.' -f 2)
    mv backup.${log_date}.$(( ${log_number} - 1 )) backup.${log_date}.${log_number}
done
cp -al backup.$(ls | grep "backup.*.0" | cut -d'.' -f 2).0 backup.$(ls | grep "backup.*.1" | cut -d'.' -f 2).1

#make new backup
rsync -a --delete ${to_backup[@]} "backup.$(date '+%F').0/"
