import dotenv
import os
from dotenv import load_dotenv
load_dotenv()
URL = (os.environ.get(f'URL'))
print (URL)
BRANCH_TO_MERGE = os.getenv(f'BRANCH')
CLONE_TO_PATH = os.environ.get(f'CLONE_PATH')
print (CLONE_TO_PATH)
if(len(os.listdir(CLONE_TO_PATH))>0):
    os.system("sudo rm -rf"+" "+CLONE_TO_PATH+"/*")
    os.system("sudo rm -rf"+" "+CLONE_TO_PATH+"/.env")
    os.system("sudo rm -rf"+" "+CLONE_TO_PATH+"/.git")
    os.system("sudo git clone"+ " "+URL+ " " + CLONE_TO_PATH)
else:
    os.system("sudo git clone"+ " "+URL+ " " + CLONE_TO_PATH)


print ("Finding Local Branches ...")
os.chdir(CLONE_TO_PATH)
SHOW_BRANCH = os.system("git branch -a")

#if banch is exit
#true = clone brache
#git remote add 
#git clone
os.system("sudo mkdir"+" "+BRANCH_TO_MERGE)
try:
    os.system("sudo git checkout -b"+" "+BRANCH_TO_MERGE+" "+"origin/"+BRANCH_TO_MERGE)
except:
    os.system("sudo git clone -b" + " " + BRANCH_TO_MERGE + " " + "--single-branch" +" " +URL)

#false=noting to merge

SHOW_BRANCH
try:
     os.system("sudo git merge")
except:
        os.system("gitk --all &")
