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

    ifile  = open('reports_complect.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    
    #ifile  = open('reports_isp.tex', "rb")
  

    ofile.close()

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_doc.tex')
    os.remove(path)   
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_compl.tex')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_sbed.tex')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_det.tex')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_stiz.tex')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_priz_bom.tex')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_priz_poc.tex')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_mater.tex')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_complect.tex')
    os.remove(path)




