# Vi Arrow Keys and Backspace

For new install using vi as default, will have different characters for different keys.

An issue that can be easily solved with the following.

	vi ~/.vimrc

This will create the vimrc file if it wasent created for you already.

Now we can add the following lines:

	set nocompatible

This will change the usage of arrow keys instead of characters.

	set backspace=indent,eol,start

This will allow the usage of the backspace to go back to the previous indentation. 
