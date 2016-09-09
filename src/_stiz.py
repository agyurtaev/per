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
    p = 0
    pr = 0
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
        if row_num==0:
            if row['Poz'] !='' or row['Kol'] !='' or row['Name'] !='' or row['Prim'] !='':
                p = 1
        row_num += 1
    if row_num > 0 and p==1:   
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        doc_title = '&&&&\hspace{1 cm}\underline{Стандартные изделия}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        raz = 1
        pr = 1        
    ifile.seek(0)
    row_num = 0
    lens7 = 10
    lens5 = 28
    for row in readerd:
        if row_num > 0:
            s7 = []
            s5 = []
            if row['Prim']!= ' ' and row['Prim']!= '':
                if len(row['Prim'])<lens7:
                        s7.append(row['Prim'])            
                else:
                    sch = 0
                    st = row['Prim']
                    l = len(st)
                    while l > 0:
                        if st[l-1] == ' ':
                            sch += 1
                            s.append(l-1)
                        l -= 1
                    s.reverse()
                    if sch == 0:  
                        print 'FATAL ERROR!!! det \n'
                        ofile.close()
                        ofile =open('reports.tex', 'w')
                        ofile.write('&&&'+'LEN ERROR!!! doc'+'&&&'+'\\'+'\\''\n')                        
                        output_log_file.close()
                        ifile.close()
                        ofile.close()
                        sys.exit()
                    sc = 0
                    nach = 0
                    kon = s[sc]
                    while sch > 0:
                        if len(st[nach:kon]) < lens7:
                            nach = s[sc]+1
                            if len(s)> sc+1:
                                kon = s[sc+1]
                            sc += 1                           
                        else:
                            print 'FATAL ERROR!!!  det \n'
                            ifile.close() 
                            sys.exit()     
                        sch -= 1
                    if not len(st[nach:]) < lens7:
                            print 'FATAL ERROR!!! det \n'
                            ifile.close() 
                            sys.exit()
                            
                    stp = row['Prim']
                    while len(stp) > lens7:                      
                        st = stp
                        while len(st) > lens7:
                            pr = st.rfind (' ')
                            st = st[0:pr]
                        col7 = st
                        s7.append(col7)                                             
                        stp = stp [pr+1:]
                    if stp != '':
                        s7.append(stp)
                        
            if len(row['Name'])<lens5:
                        s5.append(row['Name'])
            else:
                stp = row['Name']
                while len(stp) > lens5:                      
                    st = stp
                    while len(st) > lens5:
                        pr = st.rfind (' ')
                        st = st[0:pr]
                    col5 = st
                    s5.append(col5)                                             
                    stp = stp [pr+1:]
                if stp != '':
                    s5.append(stp)

            count = len(s5)
            while count > 0:
                count -=1
                if s5[count]== '  ':
                    s5.pop(count)
                    count = len(s5)
            count = len(s5)        
            while count > 0:
                count -=1
                if s5[count]== ' ':
                    s5.pop(count)
                    count = len(s5)

            count = len(s7)
            while count > 0:
                count -=1
                if s7[count]== '  ':
                    s7.pop(count)
                    count = len(s7)
            count = len(s7)        
            while count > 0:
                count -=1
                if s7[count]== ' ':
                    s7.pop(count)
                    count = len(s7)
                    
            count1 = len(s5)
            count2 = len(s7)
            if count1 > count2:
                count = count1
            else:
                count = count2
            count_u = count
            number = 0

            while count > 0:
                if number > count1 - 1:
                    s5.append('')                                
                if number > count2 - 1:
                    s7.append('')   
                if count == count_u and (s5 != [''] or s7 != ['']):
                    if row['Poz'] == '0':
                        ofile.write('&&'
                                        +'&'
                                        +'&'
                                        +perecod(s5[number])
                                        +'&'
                                        +perecod(row['Kol'])
                                        +'&'
                                        +perecod(s7[number])
                                        +'\\'+'\\''\n')

                    else:
                        ofile.write('&&'
                                        +str(num)
                                        #+row['Poz'].decode('cp1251').encode("utf-8")
                                        +'&'
                                        +'&'
                                        +perecod(s5[number])
                                        +'&'
                                        +perecod(row['Kol'])
                                        +'&'
                                        +perecod(s7[number])
                                        +'\\'+'\\''\n')
                        num += 1                  
                else:
                    ofile.write('&&'
                                    +'&'
                                    +'&'
                                    +perecod(s5[number])
                                    +'&'
                                    +'&'
                                    +perecod(s7[number])
                                    +'\\'+'\\''\n')
                    if row['Poz'] != '0':
                        num += 1                     
                number += 1
                count -= 1
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

    if prib_num > 0 and pr == 0:
        ofile =open('reports_sbed.tex', 'w')
        ofile.write('&&&&&&'+'\\'+'\\''\n')    
        doc_title = '&&&&\hspace{1 cm}\underline{Стандартные изделия}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        ofile.close()
    ifile.close()
    num = num + prib_num
    if raz > 0 or prib_num != 0:
        num += 5    
    return num,num_stiz
    


