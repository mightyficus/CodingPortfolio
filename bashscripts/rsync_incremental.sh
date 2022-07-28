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
for (( log_number=$backup_backlog; log_number >= 2; log_number-- )); do
    log_date=$(ls | grep backup.*.$((${log_number}-1)) | cut -d'.' -f 2)
    # If the destination folder doesn't have the max number of backups (backup_backlog), filenaming gets weird
    # This makes sure that if any of the backup directories are missing, an empty file with the right name is added
    # New empty file keeps naming convention consistent
    if [ ! -d "backup.${log_date}.$(( ${log_number} - 1 ))" ]; then
        touch "backup.$(date --date="$(date) -${log_number} days" '+%F').$(( ${log_number} - 1 ))"
        log_date=$(ls | grep backup.*.$((${log_number}-1)) | cut -d'.' -f 2)
    fi
    mv "backup.${log_date}.$(( ${log_number} - 1 ))" "backup.${log_date}.${log_number}"
done
cp -al "backup.$(ls | grep backup.*.0 | cut -d'.' -f 2).0" "backup.$(ls | grep backup.*.0 | cut -d'.' -f 2).1"

# make new backup
rsync -a --dry-run --delete --exclude="/home/*/.cache" ${to_backup[@]} "backup.$(ls | grep backup.*.0 | cut -d'.' -f 2).0"
# Keeps naming convention consistent
mv "backup.$(ls | grep backup.*.0 | cut -d'.' -f 2).0" "backup.$(date '+%F').0/"
