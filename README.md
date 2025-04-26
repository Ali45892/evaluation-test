# DevOps Evaluation Exercise

This repository contains the completed tasks for the DevOps Engineer evaluation.

## Table of Contents
- [Task 1: Shell Scripting & Backup with Ansible](#task-1-shell-scripting--backup-with-ansible)
- [Task 2: Python Script for File Monitoring](#task-2-python-script-for-file-monitoring)
- [Task 3: Containerization](#task-3-containerization)
- [Task 4: CI/CD with GitHub Actions](#task-4-cicd-with-github-actions)
- [Task 5: Deployment Task](#task-5-deployment-task)
- [Task 6: Monitoring & Alerting](#task-6-monitoring--alerting)

## Task 1: Shell Scripting & Backup with Ansible

### Shell Script
Location: `task1/backup_logs.sh`

This script compresses logs from `/var/log/myapp/` and stores them with a timestamp in `/backups/`.

### Ansible Playbook
Location: `task1/playbook.yml`

This playbook:
- Installs required tools (gzip, cron)
- Copies the backup script to the target host
- Configures a cron job to run the script hourly

### How to run
```bash
# Make the script executable
chmod +x task1/backup_logs.sh

# Run the Ansible playbook
ansible-playbook -i inventory.ini task1/playbook.yml
```

## Task 2: Python Script for File Monitoring

Location: `task2/file_monitor.py`

This script monitors a given directory for file changes (creation, deletion, modification) and logs these events to `log.txt`.

### Requirements
- Python 3.6+
- Watchdog package (`pip install watchdog`)

### How to run
```bash
# Install dependencies
pip install -r task2/requirements.txt

# Run the script
python task2/file_monitor.py /path/to/directory/to/monitor
```

## Task 3: Containerization

Location: `task3/`

A simple Flask application that connects to Redis and returns a "hello world" string.

### Files
- `app.py` - Flask application
- `Dockerfile` - Container definition
- `docker-compose.yml` - Multi-container setup
- `requirements.txt` - Python dependencies

### How to run
```bash
cd task3
docker-compose up -d
```

Access the application at `http://localhost:5000`

## Task 4: CI/CD with GitHub Actions

Location: `.github/workflows/ci-cd.yml`

This workflow:
- Builds the Docker image
- Runs linting (flake8)
- Runs pytest
- Pushes the image to Docker Hub (when not a PR)

The workflow runs automatically:
- On push to main branch
- On pull requests to main branch
- Every night at midnight
- Manually via workflow dispatch

## Task 5: Deployment Task

Location: `task5/deploy_playbook.yml`

This Ansible playbook deploys the Flask application to a remote Ubuntu VM by:
- Installing Docker and Docker Compose
- Deploying the application using Docker Compose

### How to run
```bash
# Update inventory.ini with your server details
ansible-playbook -i inventory.ini task5/deploy_playbook.yml
```

## Task 6: Monitoring & Alerting

Location: `task6/`

A monitoring stack using Prometheus, Node Exporter, and Grafana.

### Files
- `docker-compose.yml` - Container setup for the monitoring stack
- `prometheus/prometheus.yml` - Prometheus configuration
- `grafana/provisioning/` - Grafana dashboards and datasources

### How to run
```bash
cd task6
docker-compose up -d
```

### Accessing the services
- Prometheus: `http://localhost:9090`
- Node Exporter: `http://localhost:9100/metrics`
- Grafana: `http://localhost:3000` (default credentials: admin/admin)

### Pre-configured dashboards
Grafana comes pre-configured with dashboards for:
- CPU usage
- Memory usage
- System metrics

## Directory Structure
```
.
├── .github
│   └── workflows
│       └── ci-cd.yml
├── task1
│   ├── backup_logs.sh
│   └── playbook.yml
├── task2
│   ├── file_monitor.py
│   └── requirements.txt
├── task3
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
├── task5
│   └── deplo.yml
        inventory.ini
├── task6
│   ├── docker-compose.yml
│   ├── prometheus
│   │   └── prometheus.yml
│   └── grafana
│       └── provisioning
│           ├── dashboards
│           │   ├── dashboard.yml
│           │   └── node-exporter-dashboard.json
│           └── datasources
│               └── datasource.yml
├── inventory.ini
└── README.md
``` 
