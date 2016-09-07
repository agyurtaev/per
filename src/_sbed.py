# coding: utf8

def sbedgen(num,perecod):
    
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
    
    if not os.path.exists(os.path.abspath(dr1+'sborochnye_edinicy.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file sborochnye edinicy ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
    
    ifile  = open(dr1+'sborochnye_edinicy.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_sbed.tex', 'w')
    row_num = 0
    raz = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('Form' in headerd) and ('Oboz' in headerd) and ('Name' in headerd)
                    and ('Poz' in headerd) and ('Kol' in headerd) and ('Prim' in headerd)):
                print 'FATAL ERROR!!! \n'
                ofile.close()                        
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file sborochnye edinicy ERROR!!!'+'&&&'+'\\'+'\\''\n')
                ifile.close()
                ofile.close()
                sys.exit()
        row_num += 1
    if row_num > 0:
        header=row
        ofile.write('&&&&&&'+'\\'+'\\''\n')    
        doc_title = '&&&&\hspace{1,5 cm}\underline{Сборочные единицы}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        raz = 1
    ifile.seek(0)
    row_num = 0
    for row in readerd:
        if row_num > 0:
            if row['Poz'] == '0':
                ofile.write(perecod(row['Form'])
                                +'&&'
                                +'&'
                                +perecod(row['Oboz'])
                                +'&'
                                +perecod(row['Name'])
                                +'&'
                                +perecod(row['Kol'])
                                +'&'
                                +perecod(row['Prim'])
                                +'\\'+'\\''\n')

            else:
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
                                +perecod(row['Prim'])
                                +'\\'+'\\''\n')
                num += 1                
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


    num_sbed = num
    ifile =open('projectname_tdd_2.csv', 'rb')
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)    
    prib_num = 0
    for row in readerd:
        if row['SpecSection']==sbed:
            prib_num += 1
    ifile.close()
    num = num + prib_num
    if raz > 0 or prib_num != 0:
        num += 5
    return num,num_sbed
    


