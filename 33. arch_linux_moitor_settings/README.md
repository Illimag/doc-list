# Arch Linux Monitor Settings

Use xrandr

Multimointor settings

For example find all mointor connections:

	xrandr

Now we know which mointors are which.

	xrandr --ouput (mointor) --left-of (mointor) 

Here are more example of useage

	cvt 1920 1080  ## Show the possible setting related to the resolution "1920*1080"
	sudo xrandr --newmode "1920x1080_60.00″ 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync"  ## Append the output of the last command to the option "--newmode”
	sudo xrandr --addmode VGA-1 “1920x1080_60.00″  ## Associate the resolution "1920*1080"  with "VGA-1"
	xrandr –output VGA-1 –mode 1920x1080_60.00 –rate 60  ## Switch to the new resolution

Still issues use man

	man xrandr
