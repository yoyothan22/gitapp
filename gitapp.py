import os
URL = input("please input a git url")
PATH_TO_CLONE = input("where to clone?")
CLONE = os.system("git clone"+ " "+URL+ " " +PATH_TO_CLONE)
print ("finding local branches ...")
SHOW_BRANCH = os.system("git branch")
REPO_TO_CLONE = input("please provide the branch")
# BRANCH_TO_MERGE = input()
