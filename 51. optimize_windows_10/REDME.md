# Optimize Windows 10

These are the following instructions to optimize Windows 10.

## Remove Bloatware

There are alot of programs that Windows 10 comes with that can't be uninstalled in a normal way.

So we can manually delete them with Powershell.

Make sure to do this in admin.

Use this command:

	DISM /Online /Get-ProvisionedAppxPackages | select-string Packagename

To find all the packages in the system.

Some can most likely be deleted.

Other you can do a search if you are not sure.

Use this command to delete a package:

	DISM /Online /Remove-ProvisionedAppxPackage /PackageName:PACKAGENAME

Make sure to change the name of the package to the one you want to delete.

## Limit Startup Applications.

When the machine boots and then starts Windows there will be applications that start.

Some of these applications can take a while to load on first start so this is one of the things that can slow down your machine.

So let's go to task manager with Ctrl-Shift-Esc.

Then in the Startup tab just right click and disable the ones you dont need.

## Change Appearance in Performance Options

We can remove all the animation effects,etc that Windows 10 comes with by default to increase performance.

Just go to settings and search performance and in visual effects you can see that selecting best performance removes

,all the animations.

## Check for viruses.

## Run a cleaner such as CCleaner

## To make sure a system is fast, you have to start it out lean.
