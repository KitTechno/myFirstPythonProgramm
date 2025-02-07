# Autor:                Elia Ressl
# Place:                Homeoffice
# Date:                 08.02.2025
# Filename:             renamefile.py
# Short description:    renames a file in the same folder as renamefile.py

import os

oldname = str("filetoberenamed.txt")
newname = str("filehasbeenrenamed")
newname = str(newname + ".txt")

print("current working directory: ",os.getcwd())
os.rename(oldname, newname)


print("FILE ",oldname,"has been renamed to ",newname)
