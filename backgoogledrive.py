#!/usr/bin/python

# Realiza un backup de los archivos guardados en la carpeta especificada
# Recibe la carpeta a respaldar y el id para subir a google drive

import os
import glob
from subprocess import call
import sys

python="/usr/bin/python"
gdcp="/usr/local/driveback/gdcp"

dirbs = [
        ['dir1','id1'],
        ['dir2','id2'],
        ['dir3','id3'],
]

def backup(path, id):
        #print "Respaldando :" + path

        for infile in glob.glob( os.path.join(path, '*') ):
                print "Respaldando :" + infile
                backupstr = gdcp + "upload -p " + id + " " + infile
                print backupstr
                try:
                        retcode = call([python, gdcp, "upload", "-p" + id, infile])
                        print retcode
                except OSError, e:
                        print "Execucion fallida:", e

def main():
        global dirbs

        for dirb in dirbs:
                backup(dirb[0], dirb[1])

# Main de programa
if __name__ == '__main__':
        main()

