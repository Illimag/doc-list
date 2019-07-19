# Anaconda Jupyter Notebook

Anaconda is a development environment that installs many different things for example Jupyter Notebook.

Jupyter Notebook is a browser based Python environment, allowing for visuals and code to be seen side by side.

Very nice, there are just so much Python can do that Javascript can't and vice versa.

## To install Anaconda

We will be installing this on a WSL Ubuntu18.04 for Windows 10 machine.

Download the script to install Anaconda in the tmp folder.

	cd /tmp
	curl -O reponame

Search for the reponame, it changes.

Run the script which is a bash file.

	bash Anaconda.sh

Install is simple, even adding the path for you.

When the installation asks if you would like to initialize Anaconda3 by running conda init:

	yes

Then after go to path of conda then:

	source path/bin/activate

Then:

	conda init

This will automatically set path for you.

If somehow this needs to be done manually:

Don't forget

	source ~/.bashrc

Now verify installation.

	conda info

To update:

	conda update conda

	conda update anaconda

## Jupyter Notebook

Can install with pip.

	pip install jupyter

Anaconda has Jupyter Notebook by default.

Run notebook:

	jupyter notebook

This will launch the server

	localhost:8888

## Installing Anoconda with Arch Linux

Firstly this will require 3G disk space.

Next we need to have wget and bzip2.

	pacman -S bzip2 wget

Choose Installation path.

We'll install to:

	/usr/local/anaconda

Find the repo for the most upto date anaconda version for the correct Linux version.

Run it with wget

	wget (repo-url)

Here is where the direct repo for anaconda installer:

	https://www.anaconda.com/distribution/#linux

Directly downloaded to download folder.

The downloaded file is a shell file so:

Run as root because we will be installing it to system files:

	sudo sh anaconda.sh

Read License and say yes if you want to accept agreement.

change path to:

	/usr/local/anaconda

At end of installation, say no to auto prepend.

We will manually Prepend Path variable.

	sudo vim ~/.bashrc

Add the PATH variable:

	# added by Anaconda3 installer
	export PATH="/usr/local/anaconda/bin:$PATH"

Restart terminal and test installation:

	conda list
