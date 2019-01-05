### This is a fix for error 0x800703fa on Windows 10 build number 1803.

When running Ubuntu 18.04 subsystem on Windows 10 I would get a error message:

	Installing, this may take a few minutes...
	WslRegisterDistribution failed with error: 0x800703fa
	Error: 0x800703fa Illegal operation attempted on a registry key that has been marked for deletion.

	Press any key to continue...

There is a problem with LxssManager and restarting it from services fixes the problem:

	net stop "LxssManager" & sc start "LxssManager"

wsl_fix.bat is a script that starts on boot with admin command prompt to automatically restart LxssManager.

Put

	wsl_fix.bat

in this path:

	C:\Users\(username)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup>

Make sure to input your system's username correctly and also some of the folders maybe hidden if you don't have show hidden files selected.
