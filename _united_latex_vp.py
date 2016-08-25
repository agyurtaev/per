# coding: utf8

def unite():
    
    import csv
    import sys
    import os
    
    ofile =open('reports.tex', 'w')

    ifile  = open('reports_stiz.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close() 
    
    ifile  = open('reports_priz_bom.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    
    ifile  = open('reports_priz_poc.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close() 
    
    ifile  = open('reports_mater.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()      

    ofile.close()



