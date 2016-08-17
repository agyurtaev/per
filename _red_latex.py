# coding: utf8

def visstr():
    
    import csv
    import sys
    import os
    
    ofile = open('reports1.tex', 'w') 
    ifile  = open('reports.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()
    
    ofile = open('reports.tex', 'w') 
    ifile  = open('reports1.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports1.tex')
    os.remove(path)
