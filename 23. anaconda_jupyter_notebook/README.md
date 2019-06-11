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


