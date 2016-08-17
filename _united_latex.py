# coding: utf8

def unite():
    
    import csv
    import sys
    import os
    
    ofile =open('reports.tex', 'w')
    
    ifile  = open('reports_doc.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    
    ifile  = open('reports_compl.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()

    ifile  = open('reports_sbed.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()   

    ifile  = open('reports_det.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()  

    ifile  = open('reports_stiz.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close() 
    
    #ifile  = open('reports_priz_bom.tex', "rb")
    
    ifile  = open('reports_priz_poc.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close() 
    
    ifile  = open('reports_mater.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()     

    ifile  = open('reports_complect.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    
    #ifile  = open('reports_isp.tex', "rb")
  

    ofile.close()
    


