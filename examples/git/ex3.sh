#[[ Exercise 3 - Stashing ]]
#Run example1
bash ./ex1.sh
cd repo1
#Create a dev branch off of the master branch
git checkout -b dev
#Change some files in the new branch
echo "1 changed in dev!" > 1
echo "2 changed in dev!" > 2
echo "3 changed in dev!" > 3
#add changes
git add 1 2 3
#commit changes
git commit -m 'commit 3: adding "changed in dev" to files'
#check dev status
git status
#stash changes
git stash
#check dev status
git status
#checkout master
git checkout master
#cat master files - notice prior version
cat 1 2 3
#check status
git status
#check master history
git log
#checkout dev
git checkout dev
#pop stash
git stash pop
#review history of dev
git log
#checkout master
git checkout master
#merge dev into master
git merge dev
#delete dev
git branch -d dev
