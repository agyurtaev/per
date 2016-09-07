# coding: utf8

def stizgen(num,perecod):
    
    import csv
    import sys
    import os
    
    dr = os.path.dirname(__file__)   
    o = os.name
    if o=='nt':
        pr = dr.rfind ('\\')
    else: 
        pr = dr.rfind ('/')
    dr = dr[0:pr]
    dr1 = dr + '/csv/'
    dr2 = dr + '/template/'
    
    if not os.path.exists(os.path.abspath(dr1+'standartnye_izdelija.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file standartnye izdelija ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
    
    ifile  = open(dr1+'standartnye_izdelija.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_stiz.tex', 'w')
    row_num = 0
    raz = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('Poz' in headerd) and ('Kol' in headerd) and ('Name' in headerd)and ('Prim' in headerd)):
                print 'FATAL ERROR!!! \n'
                ofile.close()                        
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file standartnye izdelija ERROR!!!'+'&&&'+'\\'+'\\''\n')
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
                if row['Poz'] == '0':
                    ofile.write('&&'
                                    +'&&'
                                    +perecod(row['Name'])
                                    +'&'
                                    +perecod(row['Kol'])
                                    +'&'
                                    +perecod(row['Prim'])
                                    +'\\'+'\\''\n')                    
                else:
                    ofile.write('&&'
                                    +str(num)
                                    #+row['Poz'].decode('cp1251').encode("utf-8")
                                    +'&&'
                                    +perecod(row['Name'])
                                    +'&'
                                    +perecod(row['Kol'])
                                    +'&'
                                    +perecod(row['Prim'])
                                    +'\\'+'\\''\n')
                    num += 1   
            else:
                stp = row['Name']
                n = 1
                while len(stp) > 30:
                    st = stp
                    while len(st) >30: 
                        pr = st.rfind(' ')
                        st = st[0:pr]
                    if n == 1:
                        if row['Poz'] == '0':
                            ofile.write('&&'
                                            +'&&'
                                            +perecod(st)
                                            +'&'
                                            +perecod(row['Kol'])
                                            +'&'
                                            +perecod(row['Prim'])
                                            +'\\'+'\\''\n')                            
                        else:
                            ofile.write('&&'
                                            +str(num)
                                            #+row['Poz'].decode('cp1251').encode("utf-8")
                                            +'&&'
                                            +perecod(st)
                                            +'&'
                                            +perecod(row['Kol'])
                                            +'&'
                                            +perecod(row['Prim'])
                                            +'\\'+'\\''\n')
                            num += 1
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

    cfg_file  = open('bom2sp.cfg', 'rb')
    cfg_readerd = csv.DictReader(cfg_file, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in cfg_readerd:
        if row_num==0:
            cfg_headerd=row
            if not (('UnplacedStr' in cfg_headerd) and ('TestPointStr' in cfg_headerd) and ('Dop' in cfg_headerd)
                    and ('Sbed' in cfg_headerd) and ('Det' in cfg_headerd) and ('Stizd' in cfg_headerd)):
                print 'FATAL ERROR!!! \n' 
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file bom2sp ERROR!!!'+'&&&'+'\\'+'\\''\n')
                ofile.close()
                sys.exit("[ERROR] Bad config file. No {UnplacedStr} or {TestPointStr} fields. Exit")
            else:
                dni_str = row['UnplacedStr']
                tp_str = row['TestPointStr']
                dop = row['Dop']
                sbed = row['Sbed']
                det = row['Det']
                stizd = row['Stizd']                               
    cfg_file.close()


    num_stiz = num 
    ifile =open('projectname_tdd_2.csv', 'rb')
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)    
    prib_num = 0
    for row in readerd:
        if row['SpecSection']==stizd:
            prib_num += 1
    ifile.close()
    num = num + prib_num
    if raz > 0 or prib_num != 0:
        num += 5    
    return num,num_stiz
    


