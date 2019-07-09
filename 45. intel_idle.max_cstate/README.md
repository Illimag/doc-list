# intel_idle.max_cstate

Having problems with machine freezing.

After looking it up, it maybe a problem with the intel cpu and graphics

Specifically

	Baytrail complete freeze

Which is a bug in the kernal > 3.16 on Baytrail Arch

Originally an Intel CPU bug that can be triggereed by certain c-state transitions. 

This is a work around.

	sudo vim /etc/defauly/grub

edit the 

	GRUB_CMDLINE_LINUX_DEFAULT

add

	intel_idle.max_cstate=1

For example

	GRUB_CMDLINE_LINUX_DEFAULT="quiet"

Then change it to this

	GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_idel.max_cstate=1"

Now update

	sudo update-grub
	reboot

Now there shouldn't be as many system freezes.

But there will be more power consumtion.
