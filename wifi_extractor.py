import platform
import subprocess

# Define the command to get Wi-Fi information
if platform.system() == "Windows":
  command = "netsh wlan show profile"
else:
  command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -s"

# Run the command and save the output to a variable
wifi_info = subprocess.run(command, capture_output=True, text=True).stdout

# Get list of connected devices on the network
command = "arp -n | grep -v 'incomplete' | awk '{print $1}'"
device_info = subprocess.run(command, capture_output=True, text=True).stdout

# Print the wifi network info and connected devices
print("Wifi Network Info:")
print(wifi_info)
print("Connected Devices:")
print(device_info)
