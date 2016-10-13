# coding: utf8

def docgen(perecod):
    
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
    
    if not os.path.exists(os.path.abspath(dr1+'dokumenty.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file csv doc ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()

    ifile  = open(dr1+'dokumenty.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_doc.tex', 'w')
    row_num = 0
    p = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('Form' in headerd) and ('Oboz' in headerd) and ('Name' in headerd) and ('Prim' in headerd)):
                print 'FATAL ERROR!!! \n'
                ofile.close()                        
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file dokumenty ERROR!!!'+'&&&'+'\\'+'\\''\n')
                ifile.close()
                ofile.close()
                sys.exit()
        if row_num==0:
            if row['Form'] !='' or row['Oboz'] !='' or row['Name'] !='' or row['Prim'] !='':
                p = 1
        row_num += 1
    
    if row_num > 0 and p==1:   
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        doc_title = '&&&&\hspace{2 cm}\underline{Документация}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
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
                        print 'FATAL ERROR!!! doc \n'
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
                            print 'FATAL ERROR!!!  doc \n'
                            ifile.close() 
                            sys.exit()     
                        sch -= 1
                    if not len(st[nach:]) < lens7:
                            print 'FATAL ERROR!!! doc \n'
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

            count1 = len(s5)
            count2 = len(s7)
            if count1 > count2:
                count = count1
            else:
                count = count2
            count_u = count
            number = 0
            
            zv = row['Form']
            
            ff = zv.rfind('*')
            while ff != -1:
                zv = zv[0:ff]+'\(\\ast\)'+zv[ff+1:]
                ff = zv.rfind('*')
            row['Form'] = zv

            
            while count > 0:
                if number > count1 - 1:
                    s5.append('')                                
                if number > count2 - 1:
                    s7.append('')   
                if count == count_u:
                    if p==1:
                        ofile.write(perecod(row['Form'])
                                        +'&'
                                        +'&'
                                        +'&'
                                        +perecod(row['Oboz'])
                                        +'&'
                                        +perecod(s5[number])
                                        +'&'
                                        +'&'
                                        +perecod(s7[number])
                                        +'\\'+'\\''\n')                    
                else:
                    ofile.write('&'
                                    +'&'
                                    +'&'
                                    +'&'
                                    +perecod(s5[number])
                                    +'&'
                                    +'&'
                                    +perecod(s7[number])
                                    +'\\'+'\\''\n') 
                number += 1
                count -= 1
        row_num += 1
    ifile.close()
    ofile.close()
    


