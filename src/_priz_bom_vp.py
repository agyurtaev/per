# coding: utf8

def prizgen(perecod):
    
    import csv
    import sys
    import os
    
    BOM_EMPTY_ITEM= " "
    
    dr = os.path.dirname(__file__)   
    pr = dr.rfind ('\\')
    dr = dr[0:pr]
    dr1 = dr + '\\csv\\'
    dr2 = dr + '\\template\\'
    
    if not os.path.exists(os.path.abspath(dr1+'prochie_izdelija_bom.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'+'file prochie izdelija bom ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    if not os.path.exists(os.path.abspath('bom2vp.cfg')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'+'file bom2vp ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
 
## Текст для настройки программы
    output_log_file =open('output.log', 'w')
    cfg_file  = open('bom2vp.cfg', 'rb')
    cfg_readerd = csv.DictReader(cfg_file, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in cfg_readerd:
        if row_num==0:
            cfg_headerd=row
            if not (('UnplacedStr' in cfg_headerd) and ('TestPointStr' in cfg_headerd) and ('Dop' in cfg_headerd)):
                print 'FATAL ERROR!!! \n' 
                ofile =open('reports.tex', 'w')
                ofile.write('&'+'file bom2vp ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
                output_log_file.close()
                ofile.close()
                sys.exit("[ERROR] Bad config file. No {UnplacedStr} or {TestPointStr} fields. Exit")
            else:
                dni_str = row['UnplacedStr']
                tp_str = row['TestPointStr']
                dop = row['Dop']
                output_log_file.write("[INFO] Config file is loaded. UnplacedStr={%s}, TestPointStr={%s}\n" %(dni_str, tp_str))
    cfg_file.close()
    
## Первый проход: проверка атрибутов
    ifile  = open(dr1+'prochie_izdelija_bom.csv', 'rb')
    reader  = csv.reader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    row_num = 0
    for row in reader:
        if row_num==0:
            header=row
        row_num+=1
    ifile.seek(0)
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('RefDes' in headerd) and ('Unplaced' in headerd) and ('Name' in headerd)
                    and ('PartNumber' in headerd) and ('PartNumberRU' in headerd) and ('Value' in headerd) and ('TU GOST' in headerd)
                    and ('PartDocument' in headerd) and ('Manufacturer' in headerd) and ('Case' in headerd) and ('TCx' in headerd)
                    and ('PowerRating' in headerd) and ('Voltage' in headerd) and ('ReplacementPN' in headerd) and ('SpecSection' in headerd)
                    and ('BomNote' in headerd)):
                print 'FATAL ERROR!!! \n' 
                ofile =open('reports.tex', 'w')
                ofile.write('&'+'BOM file ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit("[ERROR] No {RefDes} or {Unplaced} or {Name} fields. Exit")
            else:
                output_log_file.write("[INFO] CSV file header is loaded succesfully. header={%s}\n" %(header))
        row_num+=1
    ifile.close()

## Второй проход: Работа с неустановленными
    ifile  = open(dr1+'prochie_izdelija_bom.csv', 'rb')
    readerd.__init__(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_1.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    for row in readerd:
        row_wr = row
        if row['Unplaced']!=BOM_EMPTY_ITEM:
            output_log_file.write('%s is unplaced {%s}, changing RefDes and note\n' % (row['RefDes'], row['Unplaced']))
            row_wr['Unplaced']=dni_str
            row_wr['RefDes']=row_wr['RefDes'] +'*'
        writerd.writerow(row_wr)
    ifile.close()
    ofile.close()

## Третий проход: Удаление контрольных точек
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_2.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    for row in readerd:
        row_wr = row
        if row['Name']== tp_str:
            output_log_file.write('%s is Test Point, removing item\n' % (row['RefDes']))
        else:
            writerd.writerow(row_wr)
    ifile.close()
    ofile.close()

## Четвертый проход: Работа с PartNumberRU
    ifile  = open('projectname_tdd_2.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_1.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    for row in readerd:
        row_wr = row
        if row['PartNumberRU']!=BOM_EMPTY_ITEM:
            output_log_file.write('%s has Russian Part Number = {%s}, removing common part number\n' % (row['RefDes'], row['PartNumberRU']))
            row_wr['PartNumber']=BOM_EMPTY_ITEM
        writerd.writerow(row_wr)
    ifile.close()
    ofile.close()

## Пятый проход: Работа с PartDocument
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_2.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    for row in readerd:
        row_wr = row
        if row['PartDocument']!=BOM_EMPTY_ITEM:
            output_log_file.write('%s has Part Document = {%s}, removing common part number\n' % (row['RefDes'], row['PartDocument']))
            row_wr['PartNumber']=BOM_EMPTY_ITEM
        writerd.writerow(row_wr)
    ifile.close()
    ofile.close()

## Шестой проход: Работа с допустимыми заменами 
    ifile  = open('projectname_tdd_2.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_1.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    row_num=0
    row1 = {}
    row2 = {}
    for row in readerd:
        if row_num==0:
            row1 = row
        else:
            row2 = row
            if (row1['RefDes']==row2['RefDes']): ## Если есть две строки с одним Ref Des-ом и у одной из них есть Replacement, а у другой нет
                output_log_file.write('Duplicated RefDes %s\n' % (row2['RefDes']))
                if(row1['ReplacementPN']!=BOM_EMPTY_ITEM):
                    row1=row1 # откладываем запись, на следующем цикле запишетстя row1 в независимости от наличия в row2 замены
                else:
                    row1=row2 # откладываем запись, на следующем цикле запишетстя row2 в независимости от наличия в row2 замены
            else:
                writerd.writerow(row1)
            row1=row2
        row_num+=1
    output_log_file.write('Last writeble RefDes %s\n' % (row1['RefDes']))
    writerd.writerow(row1)
    ifile.close()
    ofile.close()

## Седьмой проход: Добавление столбца количество
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_2.csv', "wb")
    header.append('kol')
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    row1 = {}  
    for row in readerd:
        row['kol'] = 1     
        writerd.writerow(row)
    output_log_file.write('Add kol. Last writeble RefDes %s\n' % (row['RefDes']))
    ifile.close()
    ofile.close()

## Восьмой проход: Объединие смежных строк и подсчёт количества
    ifile  = open('projectname_tdd_2.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_1.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    row_num=0
    row1 = {}
    row2 = {}
    refbuf = ''
    for row in readerd:
        if row_num==0:
            row1 = row
        else:
            row2 = row
            if (row1['Name']==row2['Name'] and row1['PartNumber']==row2['PartNumber'] and row1['PartNumberRU']==row2['PartNumberRU'] and row1['PartDocument']==row2['PartDocument'] and row1['Unplaced']==row2['Unplaced']):
                row1['kol'] =int(row1['kol']) + 1               
                if row1['kol'] == 2:
                    refbuf = row1['RefDes']
                    output_log_file.write('United %s and %s\n' % (row1['RefDes'],row2['RefDes']))                    
                    row1['RefDes'] = refbuf + ',' + row2['RefDes']
                else:
                    output_log_file.write('United %s and %s\n' % (row1['RefDes'],row2['RefDes']))                    
                    row1['RefDes'] = refbuf + '-' + row2['RefDes']
            else:
                writerd.writerow(row1)
                row1 = row
        row_num+=1
    writerd.writerow(row1)
    ifile.close()
    ofile.close()

## Девятый проход: Объединие строк и подсчёт количества  
    ifile  = open('projectname_tdd_1.csv', "rb")
    ifilea =open('projectname_tdd_3.csv', 'wb')
    for row in ifile:
        ifilea.write(row)
    ifile.close()
    ifilea.close()   
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ifilea  = open('projectname_tdd_3.csv', "rb")    
    readerda = csv.DictReader(ifilea, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )      
    ofile  = open('projectname_tdd_2.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    row_num=0
    row1 = {}
    row2 = {}
    refbuf = ''
    pr = 1
    for row in readerd:
        row_num_a = 0
        if row_num==0:
            row1 = row
        else:
            for rowa in readerda:
                if row_num_a==0:
                    row2 = rowa
                else:
                    row2 = rowa
                    if row_num_a < row_num:
                        if (row1['Name']==row2['Name'] and row1['PartNumber']==row2['PartNumber'] and row1['PartNumberRU']==row2['PartNumberRU'] and row1['PartDocument']==row2['PartDocument'] and row1['Unplaced']==row2['Unplaced']):
                            pr = 0    
                    if row_num_a > row_num:
                        if (row1['Name']==row2['Name'] and row1['PartNumber']==row2['PartNumber'] and row1['PartNumberRU']==row2['PartNumberRU'] and row1['PartDocument']==row2['PartDocument'] and row1['Unplaced']==row2['Unplaced']):
                            row1['kol'] =int(row1['kol']) + int(row2['kol'])               
                            refbuf = row1['RefDes']
                            row1['RefDes'] = refbuf + ',' + row2['RefDes']
                row_num_a+=1
            if pr == 1:       
                writerd.writerow(row1)   
        row1 = row
        row_num+=1 
        pr = 1
        ifilea.seek(0)
    writerd.writerow(row1)
    ifile.close()
    ifilea.close()
    ofile.close()

## Десятый проход: Неустанавлеваемые вниз
    ifile  = open('projectname_tdd_2.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_1.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)    
    ofilea  = open('projectname_tdd_3.csv', "wb")
    writerda = csv.DictWriter(ofilea, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    writerda.writeheader()
    row_num=0
    row1 = {}
    for row in readerd:
        if row_num==0:
            row1 = row
        else:            
            if row1['Unplaced'] != dni_str:
                writerd.writerow(row1)
            else:
                writerda.writerow(row1)
        row1 = row
        row_num+=1
    if row1['Unplaced'] != dni_str:
        writerd.writerow(row1)
    else:
        writerda.writerow(row1)
    ifile.close()
    ofile.close()
    ofilea.close()
    
    ifile  = open('projectname_tdd_1.csv', "rb")
    ifilea  = open('projectname_tdd_3.csv', "rb")
    ofile =open('projectname_tdd_2.csv', 'wb')
    for row in ifile:
        ofile.write(row)
    for row in ifilea:
        ofile.write(row)        
    ifile.close()
    ifilea.close()
    ofile.close() 
    
## Одиннадцатый проход: Латех   
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_priz_bom.tex', 'w')
    vid = ''
    vidpred = ''
    ofile.write('&&&&&&&&&&'+'\\'+'\\''\n')
    doc_title = '&\hspace{2 cm}\\textit{\underline{Прочие изделия}}&&&&&&&&&'+'\\'+'\\''\n'
    ofile.write(doc_title)
    ofile.write('&&&&&&&&&&'+'\\'+'\\''\n')
    for row in readerd:
        vid = row['RefDes'][0]
        if vid != vidpred:
            ofile.write('&&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'C':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Конденсаторы}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'R':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Резисторы}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'D':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Микросхемы}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'X':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Соединители}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'B':
                ofile.write('&\hspace{1 cm}\\textit{\underline{Кварцевые резонаторы}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'F':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Предохранители}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'G':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Генераторы}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'H':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Светодиоды}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'K':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Реле}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'L':
                ofile.write('&\hspace{0,5 cm}\\textit{\underline{Катушки индуктивности / Дроссели}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'S':
                ofile.write('&\hspace{0,5 cm}\\textit{\underline{Механичесие устройства коммутации}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'T':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Трансформаторы}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'V':
                if row['RefDes'][1] == 'T':
                    ofile.write('&\hspace{2 cm}\\textit{\underline{Транзисторы}}&&&&&&&&&'+'\\'+'\\''\n')
                if row['RefDes'][1] == 'D':
                    ofile.write('&\hspace{2 cm}\\textit{\underline{Диоды}}&&&&&&&&&'+'\\'+'\\''\n')
            if vid == 'Z':
                ofile.write('&\hspace{2 cm}\\textit{\underline{Фильтры}}&&&&&&&&&'+'\\'+'\\''\n')
            output_log_file.write('Add category %s \n' % vid)
            ofile.write('&&&&&&&&&&'+'\\'+'\\''\n')

            man = ''
            if len(row['Manufacturer']) < 13: 
                man = row['Manufacturer']
            else: 
                if (row['Manufacturer'][12]!= 'a'
                    or row['Manufacturer'][12]!= 'e'
                    or row['Manufacturer'][12]!= 'i'
                    or row['Manufacturer'][12]!= 'j'
                    or row['Manufacturer'][12]!= 'o'
                    or row['Manufacturer'][12]!= 'q'
                    or row['Manufacturer'][12]!= 'u'
                    or row['Manufacturer'][12]!= 'y'
                    or row['Manufacturer'][12]!= ' '):
                    man = row['Manufacturer'][0:11]+'.'
                else:
                    if (row['Manufacturer'][11]!= 'a'
                        or row['Manufacturer'][11]!= 'e'
                        or row['Manufacturer'][11]!= 'i'
                        or row['Manufacturer'][11]!= 'j'
                        or row['Manufacturer'][11]!= 'o'
                        or row['Manufacturer'][11]!= 'q'
                        or row['Manufacturer'][11]!= 'u'
                        or row['Manufacturer'][11]!= 'y'
                        or row['Manufacturer'][11]!= ' '):
                        man = row['Manufacturer'][0:10]+'.'
                    
                    else:
                        man = row['Manufacturer'][0:9]+'.'

######################################################################################################## 5-й столбец
        val = 0
        s5 = []
        col5 = ''
        col5_list = []       
        if row['Value']!=' ' or row['TCx']!=' ' or row['PowerRating']!=' ' or row['Voltage']!= ' ': 
            col5_list.append(row['Name'])
            col5_list.append(' ')
            col5_list.append(row['PartNumber'])
            col5_list.append(' ')
            col5_list.append(row['PartNumberRU'])
            col5_list.append(' (')
            col5_list.append(row['Value'])
            if row['TCx'] != ' ' and row['Value'] != ' ':
                col5_list.append('-')
            else:
                col5_list.append(' ')
            col5_list.append(row['TCx'])
            if row['PowerRating'] != ' 'and (row['TCx'] != ' ' or row['Value'] != ' '):
                col5_list.append('-')
            else:
                col5_list.append(' ')
            col5_list.append(row['PowerRating'])
            if row['Voltage'] != ' ' and (row['PowerRating'] != ' 'or row['TCx'] != ' ' or row['Value'] != ' '):
                col5_list.append('-')
            else:
                col5_list.append(' ')            
            col5_list.append(row['Voltage'])
            col5_list.append(') ')
            col5_list.append(row['TU GOST'])
            col5_list.append(' ')
            col5_list.append(row['PartDocument'])
            val = 0
        else:
            col5_list.append(row['Name'])
            col5_list.append(' ')
            col5_list.append(row['PartNumber'])
            col5_list.append(' ')
            col5_list.append(row['PartNumberRU'])
            col5_list.append(' ')
            col5_list.append(row['TU GOST'])
            col5_list.append(' ')
            col5_list.append(row['PartDocument'])            
            val = 1
            
        lens5 = 30      
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
        else:##del PartDocument
            col5 = ''
            count  = len(col5_list)            
            count -=2              
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1                            
            if len(col5)<lens5:
                if col5 != '':
                    s5.append(col5)
                count  = len(col5_list)
                count -=2
                while count > 0:
                    count -=1                     
                    col5_list.pop(count)                                                   
            else:##del TU GOST
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
                else:##del Value/PartNum
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=12              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=12 
                            while count > 0:
                                count -=1
                                col5_list.pop(count) 
                    if val == 1:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=8              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1                            
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=8 
                            while count > 0:                   
                                count -=1
                                col5_list.pop(count) 
                    if len(col5) >= lens5:##PartNum
                        if val == 0:
                            col5 = ''
                            count  = len(col5_list) 
                            count -=16              
                            while count > 0:
                                col5 = col5_list[count-1] + col5
                                count -=1                            
                            if len(col5)<lens5:
                                if col5 != '':
                                    s5.append(col5)
                                count  = len(col5_list)
                                count -=16 
                                while count > 0:
                                    count -=1
                                    col5_list.pop(count) 
                    if len(col5) >= lens5:
                        print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                        ofile.close()
                        ofile =open('reports.tex', 'w')
                        ofile.write('&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&&&&&&&'+'\\'+'\\''\n')                        
                        output_log_file.close()
                        ifile.close()
                        ofile.close()
                        sys.exit()

################################################ 2-я строка
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
        else:##del PartDocument
            col5 = ''
            count  = len(col5_list)            
            count -=2              
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1
            if len(col5)<lens5:
                if col5 != '':
                    s5.append(col5)
                count  = len(col5_list)
                count -=2
                while count > 0:
                    count -=1                     
                    col5_list.pop(count)
            else:##del TU GOST
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
                else:##del Value
                    if val == 0:
                        col5 = ''
                        count  = len(col5_list) 
                        count -=12              
                        while count > 0:
                            col5 = col5_list[count-1] + col5
                            count -=1 
                        if len(col5)<lens5:
                            if col5 != '':
                                s5.append(col5)
                            count  = len(col5_list)
                            count -=12 
                            while count > 0:
                                count -=1
                                col5_list.pop(count)  
                    if len(col5) >= lens5:
                        print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                        ofile.close()
                        ofile =open('reports.tex', 'w')
                        ofile.write('&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&&&&&&&'+'\\'+'\\''\n')                        
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
        else:##del PartDocument
            col5 = ''
            count  = len(col5_list)            
            count -=2              
            while count > 0:
                col5 = col5_list[count-1] + col5
                count -=1                            
            if len(col5)<lens5:
                if col5 != '':
                    s5.append(col5)
                count  = len(col5_list)
                count -=2
                while count > 0:
                    count -=1                     
                    col5_list.pop(count)                                                   
            else:##del TU GOST
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
                    ofile.write('&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&&&&&&&'+'\\'+'\\''\n')                        
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
        else:##del PartDocument
            if val == 0:
                col5 = ''
                count  = len(col5_list) 
                count -=2              
                while count > 0:
                    col5 = col5_list[count-1] + col5
                    count -=1                            
                if len(col5)<lens5:
                    if col5 != '':
                        s5.append(col5)
                    count  = len(col5_list)
                    count -=2 
                    while count > 0:
                        count -=1
                        col5_list.pop(count)  
            if len(col5) >= lens5:
                print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                ofile.close()
                ofile =open('reports.tex', 'w')
                ofile.write('&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&&&&&&&'+'\\'+'\\''\n')                        
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit()
                
################################################ Допустимые замены

        col5 = ''
        if row['ReplacementPN']!=' ':
            col5 = dop + ' (' + row['ReplacementPN']+')'
            if len(col5)<lens5:
                s5.append(col5)
            else:
                s5.append(dop)
                col5 = '(' + row['ReplacementPN']+')'
                if len(col5)<lens5:
                    s5.append(col5)
                else:
                    print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                    ofile.close()
                    ofile =open('reports.tex', 'w')
                    ofile.write('&'+'LEN ERROR!!! %s' % (row['RefDes'])+'&&&&&&&&&'+'\\'+'\\''\n')                        
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
########################################################################################################
        count = len(s5)    
        count_u = count
        number = 0      
        while count > 0:             
            if count == count_u:                
                ofile.write('&\\textit{'
                            +perecod(s5[number])
                            +'}&&&&&\\textit{'
                            +perecod(row['kol'])
                            +'}&&&\\textit{'
                            +perecod(row['kol'])
                            +'}&'
                            +'\\'+'\\''\n')
            else:
                ofile.write('&\\textit{'
                            +perecod(s5[number])
                            +'}&&&&&'
                            +'&&&'
                            +'&'
                            +'\\'+'\\''\n')
            number += 1
            count -= 1
        ofile.write('&&&&&&&&&&'+'\\'+'\\''\n') 
        vidpred = vid       
          
    ifile.close()
    ofile.close()
    output_log_file.close()
