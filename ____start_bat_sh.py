
# coding: utf8

def main():
    import csv
    import sys
    import os
    import platform
    import subprocess
    import time

    o = os.name
    put = os.getcwd()
    put1 = put + '/source/cod/'
    if o=='nt':
        #proc = '___start.bat'
        #p = subprocess.Popen(proc, shell = True)
        #p.wait() 
        os.system(put1+'___start.bat')
    if o=='posix':
        os.system('chmod +x '+put1+'___start.sh')
        os.system('gksudo '+put1+'./___start.sh')
        
if __name__ == '__main__':
    main()


