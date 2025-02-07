# Autor:                Elia Ressl
# Place:                Homeoffice
# Date:                 08.02.2025
# Filename:             renamefile.py
# Short description:    renames a file in the same folder as renamefile.py

import os
scriptdir = os.path.dirname(__file__)   #hier musste ich den chatbot fragen wiso das es nicht funktioniert hat. anscheinend ist das working directory nicht das directory in dem das file rename.py ist.
os.chdir(scriptdir)                     #das working directory wird zum current directory geändert. chatbot hat diesen code ausgespuckt. funktioniert aber.

oldname = str("filetoberenamed.txt")
newname = str("filehasbeenrenamed.txt")

scriptdir = os.path.dirname(__file__)
os.chdir(scriptdir)

os.rename(oldname, newname)

print("FILE ",oldname,"has been renamed to ",newname)
