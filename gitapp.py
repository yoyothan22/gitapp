import os
URL = input("please input a git url")
# PATH_TO_CLONE = input("where to clone?")
if os.path.exists('/home/yonathane/project/gitapp/clone'):
    os.system("rm -r /home/yonathane/project/gitapp/clone/*")
    os.system("sudo rm -r /home/yonathane/project/gitapp/clone/.git")

CLONE = os.system("git clone"+ " "+URL+ " " + "~/project/gitapp/clone")
print ("finding local branches ...")
SHOW_BRANCH = os.system("git branch")
REPO_TO_CLONE = input("please provide the branch")
# BRANCH_TO_MERGE = input()
# git merge source-branch && git branch -d source-branch