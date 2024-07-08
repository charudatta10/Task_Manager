import os
import subprocess


list_dirs = [".archive",".github",".vscode","build","dist","doc","src"]
list_files = [".env", ".getattribute", ".gitignore", "license", "main.py","readme.md","requirement.txt"]

for x in list_dirs:
    os.mkdir(x)  

for x in list_files:
    with open(x,"w") as f:
        pass  

subprocess.run(["git", "init"])
subprocess.run(["mkdocs", "new","."]) 
subprocess.run(["dynaconf", "-f","json"])
subprocess.run(["git", "add","."])
subprocess.run(["git", "commit","-m","Initial commit"])
# git init
# mkdocs new .
# dynaconf -f json
# pyintsaller src/name.py -onefile
