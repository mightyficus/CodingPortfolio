#!/bin/bash

#push warning message to server
screen -R mc_server -X stuff "say Backup starting. World no longer saving...$(printf '\r')"
screen -R mc_server -X stuff "save-off $(printf '\r')"
screen -R mc_server -X stuff "save-all $(printf '\r')"
sleep 3

#actual backup
tar -cpvzf /home/ubuntu/mc_backups/backup-$(date +%F).tar.gz /srv/TechCraft

#Tell server backup is complete
screen -R mc_server -X stuff "save-on $(printf '\r')"
screen -R mc_server -X stuff "say Backup complete. World now saving. $(printf '\r')"
