# Python2 and 3 Parallel System Install

Installing Python2 and 3 next to each other is fairly simple.

For example 16.04, but make sure to update

	sudo apt update

If run:

	python -v

You will see the version number.

Try to run this command:

	py -2

	py -3

If nothing shows then you need to install python2.

Recommend installing 2.7.9 which comes with pip as default.

pip is a installer, such as npm

For 16.04, find the correct repo and add it:

	sudo add-apt-repository reponame

The reponames change too often so it's better to look it up constantly.

Then its:

	sudo apt-get update

	sudo apt-get install build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev

	sudo apt-get install python3-pip python3.7-dev

	sudo apt-get install python3.7

If there are still issues remember to add the path, it's in Advanced settings on the control panel of a windows machine.

It's important to remember that pip is installed with it's specific python installation.

So for python2.7.9, pip is installed by default.

For example:

	py -2 pip -m install 

	py -3 pip3 -m install

It should be something along those lines.

Depending on which python installation is used more often:

	python

Can be python2 or python3

Also

	python2

	python3

So:
	python pip install

	python2 pip -m install

	python3 pip3 -m install

For Ubuntu 18.04, Currently it seems 2.7.15 is installed:

	python -v

To install python3, install it similarly to 16.04 but replace the reponame.

Can install specific versions of python.

For example:

	python3 -v

Is 3.6

	python3.7 -v 

Is 3.7

## Reasons why this is important

Sometimes there's a repo that hasent been updated in a while.

It's using an outdated version, so the only way to run the program is using the versions it was built with.

This is also like Javascript and npm.

For Javascript, nvm is recommended.

## VirtualEnv

Really recommend wrapping all python projects in it's own virtualenv.

