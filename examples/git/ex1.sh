#[[ Exercise Part 1 ]]
#Generate a public ssh key and publish it to GitHub/Unfuddle/Interns
#Initialize a repo
#Add files to the repo
#Commit the files
#Make some changes to the files
#Diff all added files
#Diff one file
#Dry add changes - to see what will be added without actually adding
#Dry add changes all files in current and subdirectories
#Add changes
#Commit the changes
rm -rf repo1
mkdir repo1
cd repo1
git init
touch 1 2 3
git add 1 2 3
git commit -m 'commit 1: adding files 1, 2 and 3'
echo "hello class! 1" > 1
echo "hello class! 2" > 2
echo "hello class! 3" > 3
git diff
git diff 1
git add -n 1 2 3
git add -n .
git add 1 2 3
git commit -m 'commit 2: inserting "hello class" into files'
git log
