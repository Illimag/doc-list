# Git Large File Storage

For files larger than 50MB, will need to use add dependency:

	lfs

To install on Ubuntu:

	sudo apt-get install git-lfs

Then setup:

	git lfs install

Run this in every repo that needs lfs.

Now select file type.

	git lfs track "*.psd"

To select all file types:

	git lfs track "*."

Then add it to the .gitattributes:

	git add .gitattributes

Done, now can push files larger than 50MB with git. 
