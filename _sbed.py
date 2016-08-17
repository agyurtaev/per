# coding: utf8

def sbedgen(num):
    
    import csv
    import sys
    import os
    
    ifile  = open('csv_sbed.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_sbed.tex', 'w')
    row_num = 0
    for row in readerd:
        row_num += 1
    if row_num > 0:
        header=row
        ofile.write('&&&&&&'+'\\'+'\\''\n')    
        doc_title = '&&&&\hspace{1,5 cm}\underline{Сборочные единицы}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
    ifile.seek(0)
    row_num = 0
    for row in readerd:
        if row_num > 0:
            ofile.write(row['Form'].decode('cp1251').encode("utf-8")
                            +'&&'
                            +str(num)
                            #+row['Poz'].decode('cp1251').encode("utf-8")
                            +'&'
                            +row['Oboz'].decode('cp1251').encode("utf-8")
                            +'&'
                            +row['Name'].decode('cp1251').encode("utf-8")
                            +'&'
                            +row['Kol'].decode('cp1251').encode("utf-8")
                            +'&'
                            +'\\'+'\\''\n')
            num += 1
        row_num += 1
    num += 5
    ifile.close()
    ofile.close()
    return num
    


