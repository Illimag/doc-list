# Arch Linux Packages

## Grub Bootloader
UEFI Booting Mode

	pacman -S grub

## EFI Bootloader
EFI Booting Mode

	pacman -S efibootmgr

## Network Support
Automatic IP leasing on ethernet devices

	pacman -S ifplugd

## Wifi Support
Enable wifi support

	pacman -S iw wpa_supplicant dialog

## Video Drivers
These are some common video drivers

	pacman -S xf86-video-ati xf86-video-intel xf86-video-nouveau xf86-video-vesa

## Touchpad Support
Touchpad Support

	pacman -S xf86-input-synaptics

## Battery Support
Battery Support

	pacman -S acpi

## Git
Version Control System

	pacman -S git

Configuration for name and email:

	git config --global user.name "jaemnkm"

	git config --global user.email "jaemnkm@gmail.com"

## Ranger
Command Line File/Folder Explorer

	pacman -S ranger

## Tmux
Command Line Window Extender

	pacman -S tmux

## Visual Studio Code
IDE

Update pacman

	sudo pacman -Sy

Assume git is already installed.

Navigate to Downloads.

	cd ~/Downloads

Find and download the Visual Studio Code repo:

Here is one (June 16, 2019)

	git clone https://AUR.archlinux.org/visual-studio-code-bin.git

Navigate to bin

	cd visual-studio-code-bin

Make a pacman package

	makepkg -s

Install:

	sudo pacman -U visual-studio-code-bin-*.pkg.tar.xz

## Vim
Text Editor

	pacman -S vim

## xorg
Graphic Desktop Display

	pacman -S xorg xorg-server

## Install LTS kernel
Long Term Support

Check version

	uname -r

install

	sudo pacman -S linux-lts

	sudo pacman install linux-lts-headers

Select during lts during boot.

Or auto select:

## Microcode
Stability for processor

	sudo pacman -S intel-ucode

	sudo grub-mkconfig -o /boot/grub/grub.cfg

## Font, Spell checking, dictionaries, Gstreamer plugins, java, etc
Check each package before install, should be OK.

	pacman -S enchant mythes-en ttf-liberation hunspell-en_US ttf-bitstream-vera pkgstats adobe-source-sans-pro-fonts gst-plugins-good ttf-droid ttf-dejavu aspell-en icedtea-web gst-libav ttf-ubuntu-font-family ttf-anonymous-pro jre8-openjdk ttf-gentium languagetool libmythes

## Firewall
Internet Firewall

Install:

	sudo pacman -S ufw

Enable:

	sudo ufw enable

Check status:

	sudo ufw status verbos

Enable autostart firewall good idea:

	sudo systemctl enable ufw.service

## VLC Media Player
This is a nice video player. Cross platform

	sudo pacman -S vlc

## Utorrent Client
This is a client to do torrents

	sudo pacman -S qbittorrent

## Dropbox
Files transfer easy

This command doesnt work.

	sudo pacman -S dropbox

## Wine
Run Window Executables on linux

This command doesn't work

	sudo pacman -S wine


