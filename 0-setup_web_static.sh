#!/usr/bin/env bash
#we intsall NGinx and set up directorios

# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create fake HTML file
echo "Hello, World!" | sudo tee /data/web_static/releases/test/index.html

# Create and update symbolic link
if [ -L "/data/web_static/current" ]; then
  rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '41i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restart Nginx
sudo service nginx restart
