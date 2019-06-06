# Connecting Domain with an AWS EC2

Go to Elastic IPS on the EC2 Dashboard and allocate new address.

Right click the new address and associate address to the instance.

Go to Route 53 click hosted zones.

Create hosted zone domain name is website.extension !No "www.".

Create record set, A type, name add www. Add the elastic IP to value.

Do again except this time without "www".

Go to godaddy and find the DNS ZONE FILE.

Edit the A(host) points to with elastic IP and save.

Go to CName(Alias) it's on the same page and change the www's Points to PublicDNS.

Go to NAMESERVER SETTINGS and manage and custom setup type.

Add 4 nameservers they are the NS type, save

Test website url, be patien, but it shouldn't take too long.

Remember to give correct permissions to the folders.

	chmod


