import os
import sys
#sys is another built-in module 

saved_profiles = os.popen('netsh wlan show profiles').read()

print(saved_profiles)

avble_netwrk = os.popen('netsh wlan show networks').read()

print(avble_netwrk)

preferred_ssid = input('Enter the preferred Wifi Id for your connection : ')

response=os.popen('netsh wlan disconnect').read()

print(response)

if preferred_ssid not in saved_profiles:
	print("Profile for "+preferred_ssid+" is not saved in system.")
	print("Sorry but can't establish the connection.")
	sys.exit()

else:
	print("Profile for "+preferred_ssid+" is saved in system.")

while True:
	avail = os.popen('netsh wlan show networks').read()

	if preferred_ssid in avail:
		print('Found')
		break

print('--------Connecting--------')
resp=os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read()
print('........Connected........')
