import dotenv
import os
from dotenv import load_dotenv
load_dotenv()
URL = (os.environ.get('URL'))
print (URL)
CLONE_TO_PATH = os.environ.get('CLONE_PATH')
print (CLONE_TO_PATH)
if os.path.exists(CLONE_TO_PATH):
    os.system("rm -r" + " "+CLONE_TO_PATH+"/*")
    os.system("rm -r" " "+CLONE_TO_PATH+"/.git")
    print('clean')
REPO_TO_CLONE = os.system("sudo git clone"+ " "+URL+ " " + CLONE_TO_PATH)
print ("Finding Local Branches ...")
SHOW_BRANCH = os.system("git branch")
BRANCH_TO_MERGE = os.getenv('BRANCH')

try:
     os.system("git merge"+" "+ BRANCH_TO_MERGE)
except:
        os.system("git diff")
