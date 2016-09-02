# coding: utf8

def visstr():
    
    import csv
    import sys
    import os

    if not os.path.exists(os.path.abspath('eskdspec.sty')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file eskdspec ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    if not os.path.exists(os.path.abspath('changeSheet.tex')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file changeSheet ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    ofile = open('reports1.tex', 'w') 
    ifile  = open('reports.tex', "rb")
    row_num = 0
    pr = 0
    strbuf = ''
    for row in ifile:
        row_num += 1        
        strbuf = row
        if '&&&&&&\\' in strbuf and (row_num == 25 or row_num == 26): 
            pr = 1
        if '&&&&&&\\' in strbuf and row_num == 28 and pr != 1:
            ofile.write('&&&&&&'+'\\'+'\\''\n')
            ofile.write('')
            row_num += 1
        if '&&&&&&\\' in strbuf and row_num == 27 and pr != 1:
            ofile.write('&&&&&&'+'\\'+'\\''\n')
            row_num += 1 
            ofile.write('&&&&&&'+'\\'+'\\''\n')
            row_num += 1
        if row_num == 29:
            row_num = 0
            pr = 0
        ofile.write(row)
    ifile.close()
    ofile.close()
    
    ofile = open('reports.tex', 'w') 
    ifile  = open('reports1.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()

