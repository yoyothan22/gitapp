import os
URL = input("please input a git url : ")
# PATH_TO_CLONE = input("where to clone?")
if os.path.exists('/home/yonathane/project/gitapp/clone'):
    os.system("rm -r /home/yonathane/project/gitapp/clone/*")
    os.system("sudo rm -r /home/yonathane/project/gitapp/clone/.git")
errormsg =  "error"
CLONE = os.system("git clone"+ " "+URL+ " " + "~/project/gitapp/clone")
print ("Finding Local Branches ...")
SHOW_BRANCH = os.system("git branch")
REPO_TO_CLONE = input("please provide the Branch : ")
os.system("git merge"+" "+ REPO_TO_CLONE + "2>  ~/project/log.txt" ) 
