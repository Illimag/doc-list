## Bootup live installation.iso

z shell prompt.

## Test Internet

LAN network.

Test network:

	ping -c1 jaemnkm.com

See all networks:

	ip link

Name of network(ethname, link/ether , eno1 or eno0):

	ip link set (ethername) up

Manually lease:

	dhcpcd (ethername)

Re-test:

	ping -c1 jaemnkm.com

Or:

	systemctl list-units | grep dhcpcd

## Set Time

	timedatectl set-ntp true

## USB Stick

### Booting both BIOS and UEFI modes
BIOS: 512B of MBR (master boot record).

UEFI: ESP(EFI system partion)

## Current Devices 

Find current avaiable devices:

	lsblk

Insert USB Device to machine.

Find with new device added to machine.

	lsblk

Look for sd(x).

	(x) = device lower case

Example

	sda, sdb, sdc

## Wiping USB 

Get info for logical-sector-size, sectors:

	fdisk -l /dev/sd(x)

Wipe USB:

	dd if=/dev/zero of=/dev/sd(x) bs=(logical-sector-size) seek=0 count=(sectors) status=progress

Use gdisk for partition the target USB device:

	gdisk /dev/sd(x)

Wipe partitions on target:

	d

Create new partitions:

	o

	y

Make a 10MB MBR part at beginning of devise memory.

	n

	enter

	enter

	+10MB

	EF02

Create a 500MB ESP partition.

	n

	enter

	enter

	+500MB

	EF00

Alocate remaining memory to linux:

	n

	enter

	enter

	enter

	enter

Check part:

	p

Write:

	w

See the new block layout:

	lsblk /dev/sd(x)

Format the 500MB EFI System with FAT32.

	mkfs.fat -F32 /dev/sd(x)2

Then format linux part with EXT4.

	mkfs-ext4 /dev/sd(x)3

Install Base packages set:

## mount

Mount EX4 partition as root:

	mkdir -p /mnt/usb

	mount /dev/sd(x) /mnt/usb

Mount FAT32 formatted ESP partition to boot:

	mkdir mnt/usb/boot

	mount /dev/sd(x) /mnt/usb/boot

## pacstrap

	pacstrap /mnt/usb base base-devel

## fstab

	genfstab -U /mnt/usb >> .mnt/usb/etc/fstab

Get the correct bootnames:

## Booking from different devices

	vi /mnt/usb/etc/fstab

# OS install complete

## Install additional moduals

	arch-chroot /mnt/usb

### locale

Autoentries for region and city:

	ln -sf /usr/share/zoneinfo/region/city /etc/localtime

Generate /etc/adjtime:

	hwclock --systohc

	vi /etc/locale.gen

Uncomment desired language:

	en_US.UTF-8

### hostname

Create hostname:

	echo hostname > /etc/hostname

Add hostname.

	127.0.1.1 8.8.8.8.localdomain hostname

## RAM disk image

	vi /etc/mkinitcpio.conf

Check if:

	HOOKS=(base udev block filesystems keyboard fsck)

Regenerate the initial RAM disk image with the changes made:

	mkinitcpio -p linux

## Network interface name assignment auto

	ls -s -dev/null /etc/udev/rule.d/80-net-setup-link.rules

## Journal config

	vi /etc/systemd/journald.conf

Uncomment:

	Storage=volatile

	SystemMaxUse=16M

## mount options

	vi /etc/fstab

change mount option from relatime to notime.

## bootloader

To enable booting the target USB stick in both boot modes. 

	Install -S grub efibootmgr

View current devices

	lsblk

Setup GRUB for UEFI booting mode:

	grub-install --target=i386-pc --boot-directory /boot /dev/sd(x)

(x) is usually a lower case letter.

For example:

	sda

	sdb

	sbc

Setup GRUB for UEFI booting mode:

	grub-install --target=x86_64-efi --efi-directory /boot --boot-directory /boot --removable

Generate a GRUB configuration:

	grub-mkconfig -o /boot/grub/grub.cfg

## network support

Automatic IP leasing on ethernet devices

	pacman -S ifplugd

Download packages to enable wifi support.

	pacman -S iw wpa_supplicant dialog

## Video Drivers

	pacman -S xf86-video-ati xf86-video-intel xf86-video-nouveau xf86-video-vesa

## Touchpad Support

	pacman -S xf86-input-synaptics

## Battery Support

	pacman -S acpi

## Set root password

	passwd

## User accounts

Create user:

	useradd -m (name of user)

Set user password:

	passwd (name of user)

Set user with sudo

	echo 'user ALL=(ALL) ALL' > etc/sudoers.d/10-user

Unmount the computer:

	unmount /mnt/usb/boot /mnt/usb

Poweroff computer:

	poweroff

Turn back on and login to user with password.

Change BIOS boot order.

