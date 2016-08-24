# coding: utf8

def detgen(num,perecod):
    
    import csv
    import sys
    import os
    
    if not os.path.exists(os.path.abspath('csv_det.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file csv det ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    ifile  = open('csv_det.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_det.tex', 'w')
    row_num = 0
    raz = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('Form' in headerd) and ('Oboz' in headerd) and ('Name' in headerd)
                     and ('Poz' in headerd) and ('Kol' in headerd)):
                print 'FATAL ERROR!!! \n'
                ofile.close()                        
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file csv det ERROR!!!'+'&&&'+'\\'+'\\''\n')
                ifile.close()
                ofile.close()
                sys.exit()
        row_num += 1
    if row_num > 0:
        header=row
        ofile.write('&&&&&&'+'\\'+'\\''\n')    
        doc_title = '&&&&\hspace{2 cm}\underline{Детали}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        raz = 1
    ifile.seek(0)
    row_num = 0
    for row in readerd:
        if row_num > 0:
            ofile.write(perecod(row['Form'])
                            +'&&'
                            +str(num)
                            #+row['Poz'].decode('cp1251').encode("utf-8")
                            +'&'
                            +perecod(row['Oboz'])
                            +'&'
                            +perecod(row['Name'])
                            +'&'
                            +perecod(row['Kol'])
                            +'&'
                            +'\\'+'\\''\n')
            num += 1
        row_num += 1
    if raz > 0:
        num += 5
    ifile.close()
    ofile.close()
    return num
    


