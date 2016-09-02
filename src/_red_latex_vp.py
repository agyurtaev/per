# coding: utf8

def visstr():
    
    import csv
    import sys
    import os

    if not os.path.exists(os.path.abspath('changeSheet.tex')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'+'file changeSheet ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    if not os.path.exists(os.path.abspath('__reg_izm.tex')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'+'file reg izm ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    ofile = open('reports1.tex', 'w') 
    ifile  = open('reports.tex', "rb")
    row_num = 0
    row_num_u = 0
    buf =''
    for row in ifile:
        if row_num == 24:
            row_num = 0
            ofile.write('\\newpage \n')
            
        row_num += 1
        row_num_u +=1
        buf =''
        a = row_num
        buf = '\\textit{'+ str(a) +'}'+ row
        ofile.write(buf)
        ofile.write('\\hline \n')

        if row_num == 22 and '&&&&&&&&&&' in row:
            row_num += 1
            a = row_num
            ofile.write('\\textit{'+str(a)+'}&&&&&&&&&&'+'\\'+'\\''\n')
            row_num_u +=1
            ofile.write('\\hline \n')
            row_num += 1
            a = row_num
            ofile.write('\\textit{'+str(a) + '}&&&&&&&&&&'+'\\'+'\\''\n')
            row_num_u +=1
            ofile.write('\\hline \n')
            
        if row_num == 23 and '&&&&&&&&&&' in row:
            #print '!!!!'
            row_num += 1
            a = row_num
            ofile.write('\\textit{'+str(a) + '}&&&&&&&&&&'+'\\'+'\\''\n')
            row_num_u +=1
            ofile.write('\\hline \n')
            
    ifile.close()
    ofile.close()
    
    ofile = open('reports.tex', 'w') 
    ifile  = open('reports1.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()

    row_num = row_num_u/24
    if row_num_u%24 != 0:
        row_num +=1       
    return row_num

