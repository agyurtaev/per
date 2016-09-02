# coding: utf8

def matergen(perecod):
    
    import csv
    import sys
    import os
    
    dr = os.path.dirname(__file__)   
    pr = dr.rfind ('\\')
    dr = dr[0:pr]
    dr1 = dr + '\\csv\\'
    dr2 = dr + '\\template\\'

    
    if not os.path.exists(os.path.abspath(dr1+'materialy.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'+'file materialy ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    ifile  = open(dr1+'materialy.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_mater.tex', 'w')
    row_num = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('Prim' in headerd) and ('Kol' in headerd) and ('Name' in headerd)and ('Prim' in headerd)):
                print 'FATAL ERROR!!! \n'
                ofile.close()                        
                ofile =open('reports.tex', 'w')
                ofile.write('&'+'file materialy ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
                ifile.close()
                ofile.close()
                sys.exit()
        row_num += 1
    if row_num > 0:   
        ofile.write('&&&&&&&&&&'+'\\'+'\\''\n')  
        doc_title = '&\hspace{2 cm}\\textit{\underline{Материалы}}&&&&&&&&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&&&&&'+'\\'+'\\''\n') 
    ifile.seek(0)
    row_num = 0
    lens2 = 30
    for row in readerd:
        if row_num > 0:
            if len(row['Name']) < lens2:
                ofile.write('&\textit{'
                            +perecod(row['Name'])
                            +'}&&&&&\\textit{'
                            +perecod(row['Kol'])
                            +'}&&&\\textit{'
                            +perecod(row['Kol'])
                            +'}&\\textit{'
                            +perecod(row['Prim'])                            
                            +'}\\'+'\\''\n')
            else:
                stp = row['Name']
                n = 1
                while len(stp) > lens2:
                    st = stp
                    while len(st) >30: 
                        pr = st.rfind(' ')
                        st = st[0:pr]
                    if n == 1:
                        ofile.write('&\\textit{'
                                    +perecod(st)
                                    +'}&&&&&\\textit{'
                                    +perecod(row['Kol'])
                                    +'}&&&\\textit{'
                                    +perecod(row['Kol'])
                                    +'}&\\textit{'
                                    +perecod(row['Prim']) 
                                    +'}\\'+'\\''\n')
                    else:
                        ofile.write('&\\textit{'
                                    +perecod(st)
                                    +'}&&&&&'
                                    +'&&&'
                                    +'&'
                                    +'\\'+'\\''\n')                  
                    stp = stp [pr:]
                    n += 1
                ofile.write('&\\textit{'
                            +perecod(stp)
                            +'}&&&&&'
                            +'&&&'
                            +'&'
                            +'\\'+'\\''\n')
        ofile.write('&&&&&&&&&&'+'\\'+'\\''\n') 
        row_num += 1
    ifile.close()
    ofile.close()

    


