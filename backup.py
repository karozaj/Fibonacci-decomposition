import sys
from shutil import copy2

#skopiowac plik wejsciowy do folderu backup pod nowa nazwa
inp=sys.argv[1]
backupFolder=sys.argv[2]
date=sys.argv[3]
outp=inp.split("\\")
outp=outp[len(outp)-1]
outp=outp[:-4]+"_backup_"+date+".txt"
outp=backupFolder+"\\"+outp
copy2(inp,outp)
