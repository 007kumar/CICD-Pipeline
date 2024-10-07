#!/bin/bash

# Define variables
REPO_URL="https://github.com/007kumar/CICD-Pipeline.git"
DEPLOY_DIR="/var/www/html"

# Clone or pull the latest code
if [ ! -d "$DEPLOY_DIR/.git" ]; then
    sudo git clone $REPO_URL $DEPLOY_DIR
else
    cd $DEPLOY_DIR
    sudo git pull origin main
fi

# Restart Nginx
sudo systemctl restart nginx
echo "Deployment completed!"

