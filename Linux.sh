#!/bin/bash

# Identify Linux distribution
distro_name=$(lsb_release -si)
distro_version=$(lsb_release -sr)

# Install common dependencies
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev libffi-dev

# Install Git based on distribution
if [[ $distro_name == "Ubuntu" || $distro_name == "Debian" ]]; then
  sudo apt-get install -y git
elif [[ $distro_name == "CentOS" || $distro_name == "RedHat" ]]; then
  sudo yum install -y git
else
  echo "Unsupported distribution: $distro_name"
  exit 1
fi

# Install Python based on distribution
if [[ $distro_name == "Ubuntu" || $distro_name == "Debian" ]]; then
  sudo apt-get install -y python3 python3-pip
elif [[ $distro_name == "CentOS" || $distro_name == "RedHat" ]]; then
  sudo yum install -y python3 python3-pip
else
  echo "Unsupported distribution: $distro_name"
  exit 1
fi

# Upgrade pip and install Python libraries
sudo python3 -m pip install --upgrade pip
sudo pip3 install matplotlib numpy pandas

# Verify installations
git --version
python3 --version
pip3 list | grep -E "matplotlib|numpy|pandas"

echo "Git, Python, and libraries installed successfully!"