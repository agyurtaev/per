# coding: utf8

def docgen(perecod):
    
    import csv
    import sys
    import os

    if not os.path.exists(os.path.abspath('csv_doc.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file csv doc ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()

    ifile  = open('csv_doc.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_doc.tex', 'w')
    row_num = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('Form' in headerd) and ('Oboz' in headerd) and ('Name' in headerd)):
                print 'FATAL ERROR!!! \n'
                ofile.close()                        
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file csv doc ERROR!!!'+'&&&'+'\\'+'\\''\n')
                ifile.close()
                ofile.close()
                sys.exit()
        row_num += 1
    if row_num > 0:   
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        doc_title = '&&&&\hspace{2 cm}\underline{Документация}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
    ifile.seek(0)
    row_num = 0
    for row in readerd:
        if row_num > 0:
            if len(row['Name']) < 30:
                ofile.write(perecod(row['Form'])
                                +'&'
                                +'&'
                                +'&'
                                +perecod(row['Oboz'])
                                +'&'
                                +perecod(row['Name'])
                                +'&'
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
                        ofile.write(perecod(row['Form'])
                                        +'&'
                                        +'&'
                                        +'&'
                                        + perecod(row['Oboz'])
                                        +'&'
                                        +perecod(st)
                                        +'&'
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
        row_num += 1
    ifile.close()
    ofile.close()
    

