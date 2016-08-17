# coding: utf8

def complectgen(perecod):
    
    import csv
    import sys
    import os
    
    ifile  = open('csv_complect.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_complect.tex', 'w')
    row_num = 0
    for row in readerd:
        row_num += 1
    if row_num > 0:
        header=row
        ofile.write('&&&&&&'+'\\'+'\\''\n')    
        doc_title = '&&&&\hspace{2 cm}\underline{Комплекты}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
    ifile.seek(0)
    row_num = 0
    for row in readerd:
        if row_num > 0:
            ofile.write('&&&'
                            +perecod(row['Oboz'])
                            +'&'
                            +perecod(row['Name'])
                            +'&'
                            +perecod(row['Kol'])
                            +'&'
                            +'\\'+'\\''\n')
        row_num+=1
    ifile.close()
    ofile.close()
    


