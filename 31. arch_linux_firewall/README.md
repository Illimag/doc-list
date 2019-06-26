# Arch Linux Firewall

With ufw:

Install ufw:

	pacman -S ufw

Enable service:

	ufw enable

Check status:

	sudo ufw status verbos

Enable autostart:

	sudo systemctl enable ufw.service

with iptables
