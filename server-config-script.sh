#program to set server and check connection with other server
echo "Starting server configuration..."
cd ~
mkdir Documents, Downloads
sudo dd if=/dev/zero of=swapfile bs=1024 count=1048576
ls /
sudo mkswap /swapfile
sudo chmod 600 /swapfile
sudo swapon/
sudo mkswap -f  swapfile
sudo swapon swapfile
cd Downloads
wget https://www.apachefriends.org/xampp-files/7.1.10/xampp-linux-x64-7.1.10-0-installer.run
chmod +x xampp-linux-x64-7.1.10-0-installer.run
./xampp-linux-x64-7.1.10-0-installer.run
echo "XAMPP Installed."
echo "Starting XAMPP Server..."
/opt/lampp/xampp start
/opt/lampp/xampp status
echo "XAMPP Started."

#Checking connection with Tier 2
