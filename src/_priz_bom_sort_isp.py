# coding: utf8

def prizgen(num,perecod,num_sbed,num_det,num_stiz,unpl_spis):
    
    import csv
    import sys
    import os
    
    BOM_EMPTY_ITEM= " "

    output_log_file =open('output.log', 'w')   
    cfg_file  = open('bom2sp.cfg', 'rb')
    cfg_readerd = csv.DictReader(cfg_file, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in cfg_readerd:
        if row_num==0:
            cfg_headerd=row
            if not (('UnplacedStr' in cfg_headerd) and ('TestPointStr' in cfg_headerd) and ('Dop' in cfg_headerd)
                    and ('Sbed' in cfg_headerd) and ('Det' in cfg_headerd) and ('Stizd' in cfg_headerd)
                    and ('Korp' in cfg_headerd)
                    and ('Volt' in cfg_headerd) and ('Om' in cfg_headerd)
                    and ('pF' in cfg_headerd) and ('F' in cfg_headerd)
                    and ('K' in cfg_headerd) and ('M' in cfg_headerd)and ('Gn' in cfg_headerd)
                    and ('Mk' in cfg_headerd)):
                print 'FATAL ERROR!!! \n' 
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'file bom2sp ERROR!!!'+'&&&'+'\\'+'\\''\n')
                output_log_file.close()
                ofile.close()
                sys.exit("[ERROR] Bad config file. No {UnplacedStr} or {TestPointStr} fields. Exit")
            else:
                dni_str = row['UnplacedStr']
                tp_str = row['TestPointStr']
                dop = row['Dop']
                sbed = row['Sbed']
                det = row['Det']
                stizd = row['Stizd']
                korp = row['Korp']
                volt = row['Volt']
                om = row['Om']
                pf = row['pF']
                f = row['F']
                k = row['K']
                m = row['M']
                mk = row['Mk']
                gn = row['Gn']
                output_log_file.write("[INFO] Config file is loaded. UnplacedStr={%s}, TestPointStr={%s}\n" %(dni_str, tp_str))
    cfg_file.close()
     
## Одиннадцатый проход: Латех
    unpl_num = []
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    prizn = 0
    for row in readerd:
        if row['RefDes'] == ' ':
            prizn = 1
    ifile.close()
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_priz_bom.tex', 'w')
    ofile_sbed =open('reports_sbed_bom.tex', 'w')
    ofile_det =open('reports_det_bom.tex', 'w')
    ofile_stiz =open('reports_stiz_bom.tex', 'w')
    ofile_info_case =open('reports_info_case.tex', 'w')
    ofile_pn =open('partn_new.txt', 'w')
    ifile_pn  = open('partn_old.txt', "rb")
    vid = ''
    vidpred = ''
    if prizn != 1:
        ofile.write('&&&&&&'+'\\'+'\\''\n')
        doc_title = '&&&&\hspace{2 cm}\underline{Прочие изделия}&&'+'\\'+'\\''\n'
        ofile.write(doc_title)
        ofile.write('&&&&&&'+'\\'+'\\''\n')
    for row in readerd:
        vid = row['RefDes'][0]
    
        if vid != vidpred:
            ofile.write('&&&&&&'+'\\'+'\\''\n')
            if vid == 'C':
                ofile.write('&&&&\hspace{2 cm}\underline{Конденсаторы}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'R':
                ofile.write('&&&&\hspace{2 cm}\underline{Резисторы}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'D':
                ofile.write('&&&&\hspace{2 cm}\underline{Микросхемы}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'X':
                ofile.write('&&&&\hspace{2 cm}\underline{Соединители}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'B':
                ofile.write('&&&&\hspace{1 cm}\underline{Кварцевые резонаторы}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'F':
                ofile.write('&&&&\hspace{1 cm}\underline{Устройства защиты}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'G':
                ofile.write('&&&&\hspace{2 cm}\underline{Генераторы}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'H':
                ofile.write('&&&&\hspace{2 cm}\underline{Светодиоды}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'K':
                ofile.write('&&&&\hspace{2 cm}\underline{Реле}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'L':
                #ofile.write('&&&&\hspace{0,1 cm}\underline{Катушки индуктивности / Дроссели}&&'+'\\'+'\\''\n')
                ofile.write('&&&&\hspace{2 cm}\underline{Дроссели}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'S':
                ofile.write('&&&&\hspace{0,1 cm}\underline{Механичесие устройства коммутации}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'T':
                ofile.write('&&&&\hspace{2 cm}\underline{Трансформаторы}&&'+'\\'+'\\''\n')
                num += 5
            if vid == 'V':
                if row['RefDes'][1] == 'T':
                    ofile.write('&&&&\hspace{2 cm}\underline{Транзисторы}&&'+'\\'+'\\''\n')
                    num += 5
                if row['RefDes'][1] == 'D':
                    ofile.write('&&&&\hspace{2 cm}\underline{Диоды}&&'+'\\'+'\\''\n')
                    num += 5
            if vid == 'Z':
                ofile.write('&&&&\hspace{2 cm}\underline{Фильтры}&&'+'\\'+'\\''\n')
                num += 5
            output_log_file.write('Add category %s \n' % vid)
            ofile.write('&&&&&&'+'\\'+'\\''\n')
        priz_unpl = 0
        l_sp = len(unpl_spis)
        str_pn_pnr = row['PartNumber']+row['PartNumberRU']
        while l_sp > 0:
            if str_pn_pnr == unpl_spis[l_sp-1]:
                priz_unpl = 1
            l_sp -= 1 
######################################################################################################## 7-й столбец 
        man = ''
        if len(row['Manufacturer']) < 11: 
            man = row['Manufacturer']
        else: 
            if (row['Manufacturer'][9]!= 'a'
                and row['Manufacturer'][9]!= 'e'
                and row['Manufacturer'][9]!= 'i'
                and row['Manufacturer'][9]!= 'j'
                and row['Manufacturer'][9]!= 'o'
                and row['Manufacturer'][9]!= 'q'
                and row['Manufacturer'][9]!= 'u'
                and row['Manufacturer'][9]!= 'y'
                and row['Manufacturer'][9]!= ' '):
                man = row['Manufacturer'][0:10]+'.'
            else:
                if (row['Manufacturer'][8]!= 'a'
                    and row['Manufacturer'][8]!= 'e'
                    and row['Manufacturer'][8]!= 'i'
                    and row['Manufacturer'][8]!= 'j'
                    and row['Manufacturer'][8]!= 'o'
                    and row['Manufacturer'][8]!= 'q'
                    and row['Manufacturer'][8]!= 'u'
                    and row['Manufacturer'][8]!= 'y'
                    and row['Manufacturer'][8]!= ' '):
                    man = row['Manufacturer'][0:9]+'.'        
                else:
                    man = row['Manufacturer'][0:8]+'.'
        lens7 = 10
        s7 = []
        col7 = ''
        if len(row['RefDes'])<lens7:
            if row['RefDes'] != '':
                s7.append(row['RefDes'])            
        else:
            stp = row['RefDes']
            while len(stp) > lens7:                      
                st = stp
                while len(st) > lens7:
                    pr = st.rfind (',')
                    st = st[0:pr]
                col7 = st + ','
                s7.append(col7)                                             
                stp = stp [pr+1:]
            if stp != '':
                s7.append(stp)
        if man != '' and man != ' ':
            s7.append(man)
            
        if row['BomNote']!= ' ' and row['BomNote']!= '':
            if len(row['BomNote'])<lens7:
                    s7.append(row['BomNote'])            
            else:
                s = []
                sch = 0
                st = row['BomNote']
                l = len(st)
                while l > 0:
                    if st[l-1] == ' ':
                        sch += 1
                        s.append(l-1)
                    l -= 1
                s.reverse()
                if sch == 0:  
                    print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                    ofile.close()
                    ofile =open('reports.tex', 'w')
                    ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
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
                        print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                        ofile.close()
                        ofile =open('reports.tex', 'w')
                        ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
                        output_log_file.close()
                        ifile.close()
                        ofile.close()
                        sys.exit()     
                    sch -= 1
                if not len(st[nach:]) < lens7:
                        print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                        ofile.close()
                        ofile =open('reports.tex', 'w')
                        ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
                        output_log_file.close()
                        ifile.close()
                        ofile.close()
                        sys.exit()
                        
                stp = row['BomNote']
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
######################################################################################################## 5-й столбец
        tol = 0
        val = 0
        s5 = []
        col5 = ''
        col5_list = []       
        if row['Value']!=' ' or row['TCx']!=' ' or row['PowerRating']!=' ' or row['Voltage']!= ' 'or row['Case']!= ' 'or row['Tolerance']!= ' ': 
            col5_list.append(row['Name'])
            col5_list.append(' ')
            col5_list.append(row['PartNumber'])
            col5_list.append(' ')
            col5_list.append(row['PartNumberRU'])
            col5_list.append(' (')

            if row['Case'] != ' ':
                col5_list.append(korp +' '+ row['Case'])
            else:
                col5_list.append('')
                
            if row['PowerRating'] != ' ' and row['Case'] != ' ':
                col5_list.append(', ')
            else:
                col5_list.append('')
            if row['PowerRating'] != ' ':   
                col5_list.append(row['PowerRating'])
            else:
                col5_list.append('')
                
            if row['TCx'] != ' ' and (row['PowerRating'] != ' ' or row['Case'] != ' '):
                col5_list.append(', ')
            else:
                col5_list.append('')
            if row['TCx'] != ' ':
                col5_list.append(row['TCx'])
            else:
                col5_list.append('')
                
            if row['Value'] != ' ' and (row['TCx'] != ' 'or row['PowerRating'] != ' ' or row['Case'] != ' '):
                col5_list.append(', ')
            else:
                col5_list.append('')
            if row['Value'] != ' ':
                if vid == 'L':
                    col5_list.append(row['Value']+gn)
                if vid == 'C':
                    if mk in row['Value']:
                        col5_list.append(row['Value']+f)
                    else:
                        col5_list.append(row['Value']+' '+pf)
                if vid == 'R':
                    if k in row['Value'] or m in row['Value']:
                        col5_list.append(row['Value']+om)
                    else:
                        col5_list.append(row['Value']+' '+om)
                if vid == 'Z':
                    col5_list.append(row['Value']+' '+om)               
                if vid != 'C' and vid != 'R'and vid != 'L'and vid != 'Z':
                    col5_list.append(row['Value'])
            else:
                col5_list.append('')
                
            if row['Tolerance'] != ' ' and (row['Value'] != ' ' or row['TCx'] != ' 'or row['PowerRating'] != ' ' or row['Case'] != ' '):
                col5_list.append(', ')
            else:
                col5_list.append('')
            if row['Tolerance'] != ' ':
                if 'PPM' in row['Tolerance'] or 'ppm' in row['Tolerance']:
                    col5_list.append(row['Tolerance'])
                else:
                    col5_list.append('\(\pm\)'+row['Tolerance']+'\%')
                    tol = 1
            else:
                col5_list.append('')
                
            if row['Voltage'] != ' ' and (row['Tolerance'] != ' ' or row['Value'] != ' ' or row['TCx'] != ' 'or row['PowerRating'] != ' ' or row['Case'] != ' '):
                col5_list.append(', ')
            else:
                col5_list.append('')
            if row['Voltage'] != ' ':
                col5_list.append(row['Voltage']+' '+volt)
            else:
                col5_list.append('')           
            col5_list.append(') ')
            col5_list.append(row['TU GOST'])
            val = 0
            if row['Case'] == ' ':
                col5_list[5] = ' '
                col5_list[7] = ' (' 
                if row['PowerRating'] == ' ':
                    col5_list[7] = ' '
                    col5_list[9] = ' ('
                    if row['TCx'] == ' ':
                        col5_list[9] = ' '
                        col5_list[11] = ' ('
                        if row['Value'] == ' ':
                            col5_list[11] = ' '
                            col5_list[13] = ' ('                            
                            if row['Tolerance'] == ' ':
                                col5_list[13] = ' '
                                col5_list[15] = ' ('                             
            if row['Voltage'] == ' ':
                col5_list[17] = ' '
                col5_list[15] = ') '
                if row['Tolerance'] == ' ':
                    col5_list[15] = ' '
                    col5_list[13] = ') '
                    if row['Value'] == ' ':
                        col5_list[13] = ' '
                        col5_list[11] = ') '
                        if row['TCx'] == ' ':
                            col5_list[11] = ' '
                            col5_list[9] = ') '
                            if row['PowerRating'] == ' ':
                                col5_list[9] = ' '
                                col5_list[7] = ') '                                        
        else:
            col5_list.append(row['Name'])
            col5_list.append(' ')
            col5_list.append(row['PartNumber'])
            col5_list.append(' ')
            col5_list.append(row['PartNumberRU'])
            col5_list.append(' ')
            col5_list.append(row['TU GOST'])          
            val = 1  
        lens5 = 28      
################################################ 1-я строка
        count  = len(col5_list)
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1
        if len(col5)<lens5: 
            col5 = ''
            count  = len(col5_list)
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if col5 != '':
                s5.append(col5)
            count  = len(col5_list)
            while count > 0:
                count -=1                     
                col5_list.pop(count)                                                              
        else:##del TU GOST
            col5 = ''
            count  = len(col5_list) 
            count -=1              
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if len(col5)<lens5:
                if col5 != '':
                    s5.append(col5)
                count  = len(col5_list)
                count -=1 
                while count > 0:                   
                    count -=1
                    col5_list.pop(count)  
            else:##del volt/PartNum
                if val == 0:
                    col5 = ''
                    count  = len(col5_list) 
                    count -=3              
                    while count > 0:
                        col5 = col5_list[count-1] + col5
                        count -=1
                    if len(col5)<lens5:
                        if col5 != '':
                            s5.append(col5)
                        count  = len(col5_list)
                        count -=3 
                        while count > 0:
                            count -=1
                            col5_list.pop(count) 
                if val == 1:
                    col5 = ''
                    count  = len(col5_list) 
                    count -=6              
                    while count > 0:
                        col5 = col5_list[count-1] + col5
                        count -=1
                    if len(col5)<lens5:
                        if col5 != '':
                            s5.append(col5)
                        count  = len(col5_list)
                        count -=6 
                        while count > 0:                   
                            count -=1
                            col5_list.pop(count) 
                if len(col5) >= lens5:##del tol
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=5              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=5 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                if len(col5) >= lens5:##del val
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=7              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=7 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                if len(col5) >= lens5:##del tc
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=9              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=9 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                if len(col5) >= lens5:##del pow
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=11              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=11 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                if len(col5) >= lens5:##del case
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=14              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=14 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)                                
                if len(col5) >= lens5:##PartNum
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=18              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=18 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                
                if len(col5) >= lens5:
                    print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                    ofile.close()
                    ofile =open('reports.tex', 'w')
                    ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
                    output_log_file.close()
                    ifile.close()
                    ofile.close()
                    sys.exit()

################################################ 2-я строка
        lens5 = 32
        col5 = ''
        count  = len(col5_list)
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1
        if len(col5)<lens5: 
            col5 = ''
            count  = len(col5_list)
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if col5 != '':
                s5.append(col5)
            count  = len(col5_list)
            while count > 0:
                count -=1                     
                col5_list.pop(count)
        else:##del TU GOST
            col5 = ''
            count  = len(col5_list) 
            count -=1              
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if len(col5)<lens5:
                if col5 != '':
                    s5.append(col5)
                count  = len(col5_list)
                count -=1 
                while count > 0:                   
                    count -=1
                    col5_list.pop(count)
            else:##del volt
                if val == 0:
                    col5 = ''
                    count  = len(col5_list) 
                    count -=3              
                    while count > 0:
                        col5 = col5_list[count-1] + col5
                        count -=1                            
                    if len(col5)-7<lens5:
                        if col5 != '':
                            s5.append(col5)
                        count  = len(col5_list)
                        count -=3 
                        while count > 0:                   
                            count -=1
                            col5_list.pop(count) 
                if len(col5) >= lens5:##del tol
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=5              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=5 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                if len(col5) >= lens5:##del val
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=7              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=7 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                if len(col5) >= lens5:##del tc
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=9              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=9 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                if len(col5) >= lens5:##del pow
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=11              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=11 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)
                if len(col5) >= lens5:##del case
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=14              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=14 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)                                
            if len(col5) >= lens5:
                print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                ofile.close()
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit()
################################################ 3-я строка
        col5 = ''
        count  = len(col5_list)       
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1            
        if len(col5)<lens5: 
            col5 = ''
            count  = len(col5_list)
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if col5 != '':
                s5.append(col5)
            count  = len(col5_list)
            while count > 0:
                count -=1                     
                col5_list.pop(count)                                                   
        else:##del TU GOST
            if val == 0:
                col5 = ''
                count  = len(col5_list) 
                count -=1              
                while count > 0:
                    col5 = col5_list[count-1] + col5
                    count -=1
                if len(col5)<lens5:
                    if col5 != '':
                        s5.append(col5)
                    count  = len(col5_list)
                    count -=1 
                    while count > 0:                   
                        count -=1
                        col5_list.pop(count)
                else:##del volt
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=3              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=3 
                            while count > 0:                   
                                count -=1
                                col5_list.pop(count) 
                    if len(col5) >= lens5:##del tol
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=5              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=5 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)
                    if len(col5) >= lens5:##del val
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=7              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=7 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)
                    if len(col5) >= lens5:##del tc
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=9              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=9 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)
                    if len(col5) >= lens5:##del pow
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=11              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=11 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)
        if len(col5) >= lens5:
                print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                ofile.close()
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit()

################################################ 4-я строка
        col5 = ''
        count  = len(col5_list)
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1
        if len(col5)<lens5: 
            col5 = ''
            count  = len(col5_list)
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if col5 != '':
                s5.append(col5)
            count  = len(col5_list)
            while count > 0:
                count -=1                     
                col5_list.pop(count) 
        else:##del TU GOST
            if val == 0:
                col5 = ''
                count  = len(col5_list) 
                count -=1              
                while count > 0:
                    col5 = col5_list[count-1] + col5
                    count -=1
                if len(col5)<lens5:
                    if col5 != '':
                        s5.append(col5)
                    count  = len(col5_list)
                    count -=1 
                    while count > 0:                   
                        count -=1
                        col5_list.pop(count)
                else:##del volt
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=3              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=3 
                            while count > 0:                   
                                count -=1
                                col5_list.pop(count) 
                    if len(col5) >= lens5:##del tol
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=5              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=5 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)
                    if len(col5) >= lens5:##del val
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=7              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=7 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)
                    if len(col5) >= lens5:##del tc
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=9              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=9 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)                   
        if (len(col5)-6) >= lens5:
            print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
            ofile.close()
            ofile =open('reports.tex', 'w')
            ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
            output_log_file.close()
            ifile.close()
            ofile.close()
            sys.exit()
################################################ 5-я строка
        col5 = ''
        count  = len(col5_list)
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1
        if len(col5)<lens5: 
            col5 = ''
            count  = len(col5_list)
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if col5 != '':
                s5.append(col5)
            count  = len(col5_list)
            while count > 0:
                count -=1                     
                col5_list.pop(count) 
        else:##del TU GOST
            if val == 0:
                col5 = ''
                count  = len(col5_list) 
                count -=1              
                while count > 0:
                    col5 = col5_list[count-1] + col5
                    count -=1
                if len(col5)<lens5:
                    if col5 != '':
                        s5.append(col5)
                    count  = len(col5_list)
                    count -=1 
                    while count > 0:                   
                        count -=1
                        col5_list.pop(count)
                else:##del volt
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=3              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=3 
                            while count > 0:                   
                                count -=1
                                col5_list.pop(count)
                    if len(col5) >= lens5:##del tol
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=5              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=5 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)
                    if len(col5) >= lens5:##del val
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=7              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=7 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)                 
        if len(col5) >= lens5:
            print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
            ofile.close()
            ofile =open('reports.tex', 'w')
            ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
            output_log_file.close()
            ifile.close()
            ofile.close()
            sys.exit()
################################################ 6-я строка
        col5 = ''
        count  = len(col5_list)
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1
        if len(col5)<lens5: 
            col5 = ''
            count  = len(col5_list)
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if col5 != '':
                s5.append(col5)
            count  = len(col5_list)
            while count > 0:
                count -=1                     
                col5_list.pop(count) 
        else:##del TU GOST
            if val == 0:
                col5 = ''
                count  = len(col5_list) 
                count -=1              
                while count > 0:
                    col5 = col5_list[count-1] + col5
                    count -=1
                if len(col5)<lens5:
                    if col5 != '':
                        s5.append(col5)
                    count  = len(col5_list)
                    count -=1 
                    while count > 0:                   
                        count -=1
                        col5_list.pop(count)
                else:##del volt
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=3              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=3 
                            while count > 0:                   
                                count -=1
                                col5_list.pop(count)  
                    if len(col5) >= lens5:##del tol
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=5              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=5 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count)
               
        if len(col5) >= lens5:
            print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
            ofile.close()
            ofile =open('reports.tex', 'w')
            ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
            output_log_file.close()
            ifile.close()
            ofile.close()
            sys.exit()
################################################ 7-я строка
        col5 = ''
        count  = len(col5_list)
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1
        if len(col5)<lens5: 
            col5 = ''
            count  = len(col5_list)
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if col5 != '':
                s5.append(col5)
            count  = len(col5_list)
            while count > 0:
                count -=1                     
                col5_list.pop(count) 
        else:##del TU GOST
            if val == 0:
                col5 = ''
                count  = len(col5_list) 
                count -=1              
                while count > 0:
                    col5 = col5_list[count-1] + col5
                    count -=1
                if len(col5)<lens5:
                    if col5 != '':
                        s5.append(col5)
                    count  = len(col5_list)
                    count -=1 
                    while count > 0:                   
                        count -=1
                        col5_list.pop(count)
                else:##del volt
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=3              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=3 
                            while count > 0:                   
                                count -=1
                                col5_list.pop(count) 
               
        if len(col5) >= lens5:
            print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
            ofile.close()
            ofile =open('reports.tex', 'w')
            ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
            output_log_file.close()
            ifile.close()
            ofile.close()
            sys.exit()
################################################ 8-я строка
        col5 = ''
        count  = len(col5_list)
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1
        if len(col5)<lens5: 
            col5 = ''
            count  = len(col5_list)
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if col5 != '':
                s5.append(col5)
            count  = len(col5_list)
            while count > 0:
                count -=1                     
                col5_list.pop(count) 
        else:##del TU GOST
            if val == 0:
                col5 = ''
                count  = len(col5_list) 
                count -=1              
                while count > 0:
                    col5 = col5_list[count-1] + col5
                    count -=1
                if len(col5)<lens5:
                    if col5 != '':
                        s5.append(col5)
                    count  = len(col5_list)
                    count -=1 
                    while count > 0:                   
                        count -=1
                        col5_list.pop(count)           
        if len(col5) >= lens5:
            print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
            ofile.close()
            ofile =open('reports.tex', 'w')
            ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
            output_log_file.close()
            ifile.close()
            ofile.close()
            sys.exit()

################################################ 9-я строка            
        col5 = ''
        count  = len(col5_list)
        while count > 0:
            col5 = col5_list[count-1] + col5
            count -=1
        if val == 0:
            if len(col5)<lens5: 
                col5 = ''
                count  = len(col5_list)
                while count > 0:
                    col5 = col5_list[count-1] + col5
                    count -=1
                if col5 != '':
                    s5.append(col5)
                count  = len(col5_list)
                while count > 0:
                    count -=1                     
                    col5_list.pop(count)                    
            if len(col5) >= lens5:
                print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                ofile.close()
                ofile =open('reports.tex', 'w')
                ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit()
                
################################################ Допустимые замены

        col5 = ''
        if row['ReplacementPN']!=' ':
            col5 = '( ' + dop +' '+ row['ReplacementPN']+' )'
            if len(col5)<lens5:
                s5.append(col5)
            else:
                col5 = '( ' + dop
                s5.append(col5)
                col5 = row['ReplacementPN']+' )'
                if len(col5)<lens5:
                    s5.append(col5)
                else:
                    print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                    ofile.close()
                    ofile =open('reports.tex', 'w')
                    ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
                    output_log_file.close()
                    ifile.close()
                    ofile.close()
                    sys.exit()               
                
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
        count = len(s5)        
        while count > 0:
            count -=1
            strok = s5[count]
            if strok[0]== ',':
                strok = strok[1:]
            s5[count] = strok  
              
######################################################################################################## 4-й столбец
        lens4 = 28
        s4 = []
        col4 = ''
        if len(row['PartDocument'])<lens4:
            if row['PartDocument'] != ' ' and row['PartDocument'] != ' ':
                s4.append(row['PartDocument'])
        else:
            print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
            ofile.close()
            ofile =open('reports.tex', 'w')
            ofile.write('&&&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&'+'\\'+'\\''\n')                        
            output_log_file.close()
            ifile.close()
            ofile.close()
            sys.exit()
            
        count = len(s4)
        while count > 0:
            count -=1
            if s4[count]== '  ':
                s4.pop(count)
                count = len(s4)
        count = len(s4)        
        while count > 0:
            count -=1
            if s4[count]== ' ':
                s4.pop(count)
                count = len(s4)
########################################################################################################
        priz_part = 0        
        buf_num = ''
        for rowa in ifile_pn:
            if row['PartNumber'] in rowa:
                priz_part = 1
                b = rowa
                pr = b.rfind ('|')
                buf_num = b[pr+1:]
            
        ifile_pn.seek(0)

        if priz_part == 0:
            if row['SpecSection'] != sbed and row['SpecSection'] != det and row['SpecSection'] != stizd:
                num_buf = str(num)
                ofile_pn.write(row['PartNumber']+'|'+str(num)+'\n')
                num += 1
            if row['SpecSection'] == sbed:
                num_buf = str(num_sbed)
                ofile_pn.write(row['PartNumber']+'|'+str(num_sbed)+'\n')
                num_sbed += 1
            if row['SpecSection'] == det:
                num_buf = str(num_det)
                ofile_pn.write(row['PartNumber']+'|'+str(num_det)+'\n')
                num_det += 1
            if row['SpecSection'] == stizd:
                num_buf = str(num_stiz)
                ofile_pn.write(row['PartNumber']+'|'+str(num_stiz)+'\n')
                num_stiz += 1
        else:
            num_buf = buf_num
            

        count1 = len(s5)
        count2 = len(s7)
        count3 = len(s4)
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
            if number > count3 - 1:
                s4.append('')    
            if count == count_u:

                if row['SpecSection'] != sbed and row['SpecSection'] != det and row['SpecSection'] != stizd:
                    if prizn != 1:
                        ofile.write('&&'
                                    +num_buf
                                    +'&'
                                    +perecod(s4[number])
                                    +'&'
                                    +perecod(s5[number])
                                    +'&'
                                    +perecod(row['kol'])
                                    +'&'
                                    +perecod(s7[number])
                                    +'\\'+'\\''\n')
                        ofile_info_case.write(str(num)+'&'+perecod(row['Case'])+'\\'+'\\''\n')
                        if priz_unpl == 1:
                            unpl_num.append(num)
                        
                      
                if row['SpecSection'] == sbed:
                    ofile_sbed.write('&&'
                                +num_buf
                                +'&'
                                +perecod(s4[number])
                                +'&'
                                +perecod(s5[number])
                                +'&'
                                +perecod(row['kol'])
                                +'&'
                                +perecod(s7[number])
                                +'\\'+'\\''\n')
                    if priz_unpl == 1:
                        unpl_num.append(num_sbed)  
                    
                if row['SpecSection'] == det:
                    ofile_det.write('&&'
                                +num_buf
                                +'&'
                                +perecod(s4[number])
                                +'&'
                                +perecod(s5[number])
                                +'&'
                                +perecod(row['kol'])
                                +'&'
                                +perecod(s7[number])
                                +'\\'+'\\''\n')
                    if priz_unpl == 1:
                        unpl_num.append(num_det) 
                    
                if row['SpecSection'] == stizd:
                    ofile_stiz.write('&&'
                                +num_buf
                                +'&'
                                +perecod(s4[number])
                                +'&'
                                +perecod(s5[number])
                                +'&'
                                +perecod(row['kol'])
                                +'&'
                                +perecod(s7[number])
                                +'\\'+'\\''\n')
                    if priz_unpl == 1:
                        unpl_num.append(num_stiz) 
                      
            else:
                
                if row['SpecSection'] != sbed and row['SpecSection'] != det and row['SpecSection'] != stizd:
                    ofile.write('&&&&'
                                +perecod(s5[number])
                                +'&&'
                                +perecod(s7[number])
                                +'\\'+'\\''\n')                       
                if row['SpecSection'] == sbed:
                    ofile_sbed.write('&&&&'
                                +perecod(s5[number])
                                +'&&'
                                +perecod(s7[number])
                                +'\\'+'\\''\n')
                if row['SpecSection'] == det:
                    ofile_det.write('&&&&'
                                +perecod(s5[number])
                                +'&&'
                                +perecod(s7[number])
                                +'\\'+'\\''\n')
                if row['SpecSection'] == stizd:
                    ofile_stiz.write('&&&&'
                                +perecod(s5[number])
                                +'&&'
                                +perecod(s7[number])
                                +'\\'+'\\''\n') 
            number += 1
            count -= 1      
        vidpred = vid       
    ifile.close()
    ofile.close()
    ofile_sbed.close()
    ofile_det.close()
    ofile_stiz.close()
    ofile_info_case.close
    output_log_file.close()
    ofile_pn.close()
    ifile_pn.close()
    num += 5

    ofile = open('reports_sbed1.tex', 'w') 
    ifile  = open('reports_sbed.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()    
    ifile  = open('reports_sbed_bom.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()
    ofile = open('reports_sbed.tex', 'w') 
    ifile  = open('reports_sbed1.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()    


    ofile = open('reports_det1.tex', 'w') 
    ifile  = open('reports_det.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()    
    ifile  = open('reports_det_bom.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()
    ofile = open('reports_det.tex', 'w') 
    ifile  = open('reports_det1.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()

    ofile = open('reports_stiz1.tex', 'w') 
    ifile  = open('reports_stiz.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()    
    ifile  = open('reports_stiz_bom.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()
    ofile = open('reports_stiz.tex', 'w') 
    ifile  = open('reports_stiz1.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()    
    
    return num
    
