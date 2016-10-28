#[[ Exercise 2 - Branching ]]
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
#review history of dev
git log
#checkout master
git checkout master
#check master history
git log
#cat master files - notice prior version
cat 1 2 3
#merge dev into master
git merge dev
#cat master files - notice current version
cat 1 2 3
#delete dev
git branch -d dev
