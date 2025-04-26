#!/bin/bash

# Get current timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create backup directory
mkdir -p /backups/

# Compress logs with timestamp
tar -czf /backups/myapp_logs_$TIMESTAMP.tar.gz /var/log/myapp/

# Remove logs older than 7 days
find /backups/ -name "myapp_logs_*.tar.gz" -type f -mtime +7 -delete

echo "Backup completed: /backups/myapp_logs_$TIMESTAMP.tar.gz"
