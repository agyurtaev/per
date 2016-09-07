
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
    put1 = put + '/src/'
    put2 = put + '/csv/'

                         
    if os.path.exists(os.path.abspath(put2+'bom_ispolnenij.txt')) and os.path.exists(os.path.abspath(put2+'varianty_ispolnenija.txt')):
        if o=='nt':
            os.system(put1+'___start_isp.bat')
        if o=='posix':
            os.system('chmod +x '+put1+'___start_isp.sh')
            os.system('gksudo '+put1+'./___start_isp.sh')
    else:
        if o=='nt':
            os.system(put1+'___start.bat')
        if o=='posix':
            os.system('chmod +x '+put1+'___start.sh')
            os.system('gksudo '+put1+'./___start.sh')

        
if __name__ == '__main__':
    main()


