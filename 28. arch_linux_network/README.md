# Arch Linux Network

## LAN

See network connections:

	ip link

power up LAN network:

	ip link set (network) up

Manually lease:

	dhcpcd (network)

Test network:

	ping bing.com

## Wireless

Check for Network controller on machine:

	lspci -k | grep -A3 'Network controller'

Check for available wireless interfaces:

	iw dev

Set up wireless:

	ip link set (wifiname) up

Scan for details of wifi connections:

	iw dev (wifiname) scan | less

Connection with no encryption:

	iw dev (wifiname) connect (networkname)

Connection with WEP:

	iw dev (wifiname) connect '(networkname)' key 0:'(password)'

For connection with WPA/WPA2:

Firstly this command needs to be run as root.

	su

Enter root password.

Once in root:

	wpa_supplicant -i (wifiname) -c <(wpa_passphrase '(networkname)' '(password)')

Once the connection is established, fork process to background:

	[ctrl]+z

	bg

Now lease IP address:

	dhcpcd (wifiname)

Test network:

	ping google.com

Terminal can be closed.

## Set Time

Make sure to set the time after connecting to the internet.

	timedatectl set-ntp true
