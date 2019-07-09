R, R Studio, Arch Linux OS

These are instruction on how to install the R programming language as well as the R Studio GUI Package onto an Arch Linux OS.

Firstly make sure to install R Programming Language before R Studio.

We will be using pacman which is the package manager for Arch Linux.

	sudo pacman -S r

After the installation is complete we can test the installation by.

	R

Note: Needs to be Caps. "r" will not work.

We can do a hello, world.

	print("hello, world")

OK, to quit the R shell.

	q()

Now we can start the installation process for R Studio which is a GUI/IDE for the R Language.

Firstly there are some dependencies required to install R Studio, R Language is one of them but also is OpenSSL.

To install OpenSSL with pacman

	sudo pacman -S openssl-1.0

Now go find the repo for rstudio.

AUR is a good place to look for it.

The weblinks change all the time so do a search.

After finding the repo download the snapshot.

Which will download the files in a compressed file.

Uncompress with gzip or tar.

	tar xvzf filename.tar

Now cd into the rstudio uncompressed dir.

And run the makepkg command

	makepkg

If there are any other dependencies it will show up in an error message.

The PKGBUILD file will do all the work and download all the nessessary files.

After everything is complete let's move the dir to the opt dir in the system.

	sudo mv path_of_dir /opt

Now we can install the package with pacman.

NOTE: The package will have this file format.

	filename.pkg.tar.xz

So to install.

	sudo pacman -U filename.pkg.tar.xz

After installation is complete let's change the theme as well.

White is actually really bad for the eyes.

Instead of pure white for example #fff or rgba(255,255,255,1) 

We should use something like #eee, but there's actually a type of CSS syntax for the R Studio GUI.

I found a nice theme on github which I have added to this repo. 

All credit goes to the author.

	janusvm

To install just open the R Studio application go to "Tools" then "Global Options" then "Appearences".

Under Editor Theme just add the .rstheme file.

Now we have a nice theme for R Studio GUI/IDE.
