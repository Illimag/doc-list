# FTP Server behind a NAT Router

For example we will be using Port: 50000-51000

The application will be filezilla.

Firstly, the client needs to open firewalls.

Open all remote ports on outbound connections.

This allows the client to send requests to the server.

Secondly, open firewalls on the server.

Allow inbound connections of those ports: 50000-51000

As well as letting application Filezilla server.

As well as allow inbound rule of port selected in general setting.

Default is 21 but should be changed for security reasons.

Setup Filezilla server by using custom port range: 50000-51000

Use retrieve external IP Address.

Also create user, and password.

Set user's dir for ftp.

Now go to router configuration.

Depending on router can find ip address.

Go to PORT FORWARDING

Add the IP ADDRESS of the server machine:

For example there are two machines:

1: client
2: server

The IP address is: 192.100.1

Then this means that the ip address of each machines are:

1: 192.100.1.101
2: 192.100.1.102

Add the custom ports: 50000-51000

For both TCP and UDP

In virtual server

Do same thing but instead of custom port put in port selected in general settings.

Default is 21.

Now to connect to the ftp server from the client.

On the client side the post is the server machine ip address

For example it is 192.100.1.102

Enter user and password

The port is the port selected in general settings.

Default is 21.

