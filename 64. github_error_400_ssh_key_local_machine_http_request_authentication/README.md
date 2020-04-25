# github_error_400_ssh_key_local_machine_http_request_authentication

Github now seems to require personal authentication tokens aas well as ssh and rsa keys to access public and private repositories, from local machines.

Simple fix is to add the rsa key to the ssh key configuration in the Github Dashboard.

First in the terminal:

	ssh-keygen -t rsa

When prompted

	y

Then press enter until completed.

	cat ~/.ssh/id_rsa.pub

This command will generate the ssh key.

Copy and paste this ssh into the Github dashboard in the Account Settings, ssh key.

	git remote rm origin

We now are removing the old method of pushing to github repos.

We now add the new origin with ssh url.

	git remote add origin git@github.com:jaemnkm/doc-list.git

Now we just have to push to the repo as normal

	git push origin master
