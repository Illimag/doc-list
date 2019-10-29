# Git Commands

## Clone

To clone a repo.

	git clone [URL of REPO]

If it is a private repo, the command line will ask for credentials.

## Pull

To get any changes made in the repo

	git pull

This will get all the new changes made to the repo

## Add

To add changes 

	git add .

The "." is all the files but you can change this to specific file types.

## Commit

To commit to a repo

	git commit -m "this is where messages are written about the commit"

You need to have added files first to commit.

## Push

To push changes made to the repo

	git push -u origin [repo branch]

It can be the master branch for it would be

	git push -u origin master

You need to commit first before you can push.

## Merge

This is how to merge changes from a different fork into original repo

First add connection to original repo

	git remote add myfriend git://github.com/myfriend/the_repo

Check the setup

	git remote -v

Add, commit, and push

	git add

	git commit

	git push

Now on the Github platform

Go to your version of the repository on github.

Click the “Pull Request” button at the top.

Note that your friend’s repository will be on the left and your repository will be on the right.

Click the green button “Create pull request”. Give a succinct and informative title, in the comment field give a short explanation of the changes and click the green button “Create pull request” again.

## Pull from original repo from fork

This is how to pull changes made from the original repo to fork

	git remote add upstream ORIGINAL_REPOSITORY_URL

	git fetch upstream

	git merge upstream/master

	git push origin master
