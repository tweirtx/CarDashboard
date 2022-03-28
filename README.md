# CarDashboard
A project I'm making to add some gauges to my car via the OBDII port and a raspberry pi.

# Installation
The included install.sh script in the repository is designed to install everything necessary to get this project running on a fresh install of Raspberry Pi OS.
If you are not using a Debian-based OS, please install the appropriate rfcomm Bluetooth modules for a Bluetooth adapter at the OS level, as well as
the Python requirements using `sudo pip3 install -Ur requirements.txt` in the project directory. It is also encouraged to copy the startuptemplate shell script
and insert your Bluetooth OBD adapter's MAC address in the correct spot if you are using one.
