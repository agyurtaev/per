# coding: utf8

def stizgen(num,perecod):
    
    import csv
    import sys
    import os

    if not os.path.exists(os.path.abspath('csv_stiz.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file csv stiz ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
    
    ifile  = open('csv_stiz.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_stiz.tex', 'w')
    row_num = 0
    raz = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('Poz' in headerd) and ('Kol' in headerd) and ('Name' in headerd)):
                print 'FATAL ERROR!!! \n'
                ofile.close()                        
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file csv stiz ERROR!!!'+'&&&'+'\\'+'\\''\n')
                ifile.close()
                ofile.close()
                sys.exit()
        row_num += 1
    if row_num > 0:   
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        doc_title = '&&&&\hspace{1 cm}\underline{Стандартные изделия}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        raz = 1
    ifile.seek(0)
    row_num = 0
    for row in readerd:
        if row_num > 0:
            if len(row['Name']) < 30:
                ofile.write('&&'
                                +str(num)
                                #+row['Poz'].decode('cp1251').encode("utf-8")
                                +'&&'
                                +perecod(row['Name'])
                                +'&'
                                +perecod(row['Kol'])
                                +'&'
                                +'\\'+'\\''\n')
            else:
                stp = row['Name']
                n = 1
                while len(stp) > 30:
                    st = stp
                    while len(st) >30: 
                        pr = st.rfind(' ')
                        st = st[0:pr]
                    if n == 1:
                        ofile.write('&&'
                                        +str(num)
                                        #+row['Poz'].decode('cp1251').encode("utf-8")
                                        +'&&'
                                        +perecod(st)
                                        +'&'
                                        +perecod(row['Kol'])
                                        +'&'
                                        +'\\'+'\\''\n')
                    else:
                        ofile.write('&&&&'
                                        +perecod(st)
                                        +'&'
                                        +'&'
                                        +'\\'+'\\''\n')                   
                    stp = stp [pr:]
                    n += 1
                ofile.write('&&&&'
                                +perecod(stp)
                                +'&&'
                                +'\\'+'\\''\n')
            num += 1
        row_num += 1
    if raz > 0:
        num += 5
    ifile.close()
    ofile.close()
    return num
    


