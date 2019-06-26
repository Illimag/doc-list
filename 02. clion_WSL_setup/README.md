# JetBrain CLion WSL Setup

Setup for Windows Subsystem for Linux C complier on the JetBrain Clion IDE.

Make sure to install CLion and Windows 10 ubuntu subsystem.

Edit clion_wsl_setup.bat file by changing the username and hostname to the computer.

Run batch file: 

	./clion_wsl_setup.bat

Open CLion and go to file then settings then build, execution, deployment then to toolchains.

Change Toolchain to WSL, change the credentials.

Add workaround for casesensitive:

Go to Help then Edit Custom properties and add:

	idea.case.sensitive.fs=true

Restart IDE using File then Invalidate Caches and Restart option.

To Run a C program in CLion:

Go to Run then Edit Configurations.

Add target and executables.

Then run. The IDE will build the everything and debug. Don't need to run complier from command line anymore.

