# FTPLIB 

This is a python dependency.

Firstly, import the dependency.

	from ftplib import FTP_TLS

There also is FTP without S.

Create variable function

	ftp =FTP_TLS()

Add debug just in case

	ftp.set_debuglevel(2)

Connect to the FTP server with host name and port

	ftp.connect('100.000.000.000', 21)

NOTE: that the host name is a string but port is int.

Also no need to strip trailing characters.

Send username to login

	ftp.sendcmd("USER username")

NOTE:that username is username of the user of the FTP server. USER is tag in front of username string. USER tag is required.

Same for password

	ftp.sendcmd("PASS password")

Now have logged into FTP server.

After task complete close the FTP connection

	ftp.close()


