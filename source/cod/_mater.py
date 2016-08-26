# coding: utf8

def matergen(perecod):
    
    import csv
    import sys
    import os
    
    if not os.path.exists(os.path.abspath('../csv_mater.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file csv mater ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    ifile  = open('../csv_mater.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_mater.tex', 'w')
    row_num = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('Kol' in headerd) and ('Prim' in headerd) and ('Name' in headerd)):
                print 'FATAL ERROR!!! \n'
                ofile.close()                        
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file csv mater ERROR!!!'+'&&&'+'\\'+'\\''\n')
                ifile.close()
                ofile.close()
                sys.exit()
        row_num += 1
    if row_num > 0:   
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        doc_title = '&&&&\hspace{2 cm}\underline{Материалы}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
    ifile.seek(0)
    row_num = 0
    for row in readerd:
        if row_num > 0:
            if len(row['Name']) < 30:
                ofile.write('&&&&'
                                +perecod(row['Name'])
                                +'&'
                                +perecod(row['Kol'])
                                +'&'
                                +perecod(row['Prim'])                            
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
                        ofile.write('&&&&'
                                        +perecod(st)
                                        +'&'
                                        +perecod(row['Kol'])
                                        +'&'
                                        +perecod(row['Prim'])
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

    


