function check_status {
    if [ $1 -ne 0 ]; then
        echo "Error occurred during step $2. Aborting..."
        exit 1
    fi
}

# Step 1: Install Docker
echo "Installing Docker..."
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
check_status $? "1"

# Step 2: Create the docker group and add the user to it
echo "Creating docker group and adding the user to it..."
sudo groupadd docker
sudo usermod -aG docker pi
check_status $? "2"

# Step 3: Activate the docker group membership
echo "Activating docker group membership..."
newgrp docker
check_status $? "3"

# Step 4: Install required dependencies for Docker Compose
echo "Installing dependencies for Docker Compose..."
sudo apt-get update
sudo apt-get install -y libffi-dev libssl-dev
check_status $? "4"

# Step 5: Install Python 3 and pip
echo "Installing Python 3 and pip..."
sudo apt-get install -y python3 python3-pip
check_status $? "5"

# Step 6: Remove python-configparser package (if installed)
echo "Removing python-configparser..."
sudo apt-get remove python-configparser
check_status $? "6"

# Step 7: Install Docker Compose
echo "Installing Docker Compose..."
sudo apt install -y docker-compose
check_status $? "7"

# Step 8: Install paho-mqtt library
echo "Installing paho-mqtt library..."
pip3 install paho-mqtt
check_status $? "8"

# Step 9: Reboot the system
echo "Rebooting the system..."
sudo reboot
