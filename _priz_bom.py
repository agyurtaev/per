# coding: utf8

def prizgen(num):
    
    import csv
    import sys
    import os
    
    BOM_EMPTY_ITEM= " "
    
## Текст для настройки программы
    cfg_file  = open('bom2sp.cfg', 'rb')
    output_log_file =open('output.log', 'w')
    cfg_readerd = csv.DictReader(cfg_file, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in cfg_readerd:
        if row_num==0:
            cfg_headerd=row
            if not (('UnplacedStr' in cfg_headerd) and ('TestPointStr' in cfg_headerd)):
                sys.exit("[ERROR] Bad config file. No {UnplacedStr} or {TestPointStr} fields. Exit")
            else:
                dni_str = row['UnplacedStr']
                tp_str = row['TestPointStr']
                output_log_file.write("[INFO] Config file is loaded. UnplacedStr={%s}, TestPointStr={%s}\n" %(dni_str, tp_str))
    cfg_file.close()
    
## Первый проход: проверка атрибутов
    ifile  = open('csv_priz_bom.csv', 'rb')
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
            if not (('RefDes' in headerd) and ('Unplaced' in headerd)and ('Name' in headerd)):
                sys.exit("[ERROR] No {RefDes} or {Unplaced} or {Name} fields. Exit")
            else:
                output_log_file.write("[INFO] CSV file header is loaded succesfully. header={%s}\n" %(header))
        row_num+=1
    ifile.close()

## Второй проход: Работа с неустановленными
    ifile  = open('csv_priz_bom.csv', 'rb')
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
    ifile  = open('projectname_tdd_11.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports_priz_bom.tex', 'w')
    vid = ''
    vidpred = ''
    st = 0
    def per(a):
        if a == 28:
            ofile.write('&&&'+'\\'+'\\''\n')
            ofile.write('&&&'+'\\'+'\\''\n')
            a = 1
        if a == 29:
            ofile.write('&&&'+'\\'+'\\''\n')
            a = 1
        if a == 30:
            a = 1 
        return a       
    for row in readerd:
        vid = row['RefDes'][0]
        if vid != vidpred:
            st += 1
            st = per(st)
            ofile.write('&&&'+'\\'+'\\''\n')
            if vid == 'C':
                ofile.write('&\hspace{3 cm}\underline{Конденсаторы}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'R':
                ofile.write('&\hspace{3 cm}\underline{Резисторы}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'D':
                ofile.write('&\hspace{3 cm}\underline{Микросхемы}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'X':
                ofile.write('&\hspace{3 cm}\underline{Соединители}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'B':
                ofile.write('&\hspace{2 cm}\underline{Кварцевые резонаторы}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'F':
                ofile.write('&\hspace{3 cm}\underline{Предохранители}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'G':
                ofile.write('&\hspace{3 cm}\underline{Генераторы}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'H':
                ofile.write('&\hspace{3 cm}\underline{Светодиоды}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'K':
                ofile.write('&\hspace{3 cm}\underline{Реле}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'L':
                ofile.write('&\hspace{1 cm}\underline{Катушки индуктивности / Дроссели}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'S':
                ofile.write('&\hspace{1 cm}\underline{Механичесие устройства коммутации}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'T':
                ofile.write('&\hspace{3 cm}\underline{Трансформаторы}&&'+'\\'+'\\''\n')
                st += 1
            if vid == 'V':
                if row['RefDes'][1] == 'T':
                    ofile.write('&\hspace{3 cm}\underline{Транзисторы}&&'+'\\'+'\\''\n')
                    st += 1
                if row['RefDes'][1] == 'D':
                    ofile.write('&\hspace{3 cm}\underline{Диоды}&&'+'\\'+'\\''\n')
                    st += 1
            if vid == 'Z':
                ofile.write('&\hspace{3 cm}\underline{Фильтры}&&'+'\\'+'\\''\n')
                st += 1
            output_log_file.write('Add category %s \n' % vid,)
            st += 1   
            ofile.write('&&&'+'\\'+'\\''\n')
        col2 = row['Name']+' '+row['PartNumber']+' '+row['PartNumberRU']+' '+row['Value']+' '+row['TU GOST']+' '+row['PartDocument']
        col4 = ''
        p = 0
        p1 = 0      
        if row['Manufacturer'] !=' ':
            col4 = row['Manufacturer']
        else:
            if row['Case'] !=' ':
                col4 = row['Case']
                p = 1
            else:
                if row['Unplaced'] !=' ':
                    col4 = row['Unplaced']
                    p = 2
        if len(col2)<50: #Если количество символов записи меньше 50, то пишем всё в одну строку
            st += 1
            st = per(st)
            ofile.write(row['RefDes']
                        +'&'
                        +col2.decode('cp1251').encode("utf-8")
                        +'&'
                        +row['kol']
                        +'&'
                        +col4.decode('cp1251').encode("utf-8")
                        +'\\'+'\\''\n')
            p1 = 1
        else:
            st += 1
            st = per(st)
            ofile.write(row['RefDes']
                        +'&'
                        +row['Name'].decode('cp1251').encode("utf-8")+' '+row['PartNumber'].decode('cp1251').encode("utf-8")+' '+row['PartNumberRU'].decode('cp1251').encode("utf-8")
                        +'&'
                        +row['kol']
                        +'&'
                        +col4.decode('cp1251').encode("utf-8")
                        +'\\'+'\\''\n')
        col4 = ''
        if row['Case'] !=' 'and p!=1:
            col4 = row['Case']
            p = 1
        else:
            if row['Unplaced'] !=' ':
                col4 = row['Unplaced']
                p = 2       
        if ((row['Value']!=' '  or row['TU GOST']!=' ' or row['PartDocument']!=' ') and p1 ==0 ) or p == 1 or p == 2:         
            if len(col2)<50:
                st += 1
                ofile.write('&'
                            +'&'
                            +'&'
                            +col4.decode('cp1251').encode("utf-8")
                            +'\\'+'\\''\n')
            else:
                st += 1
                ofile.write('&'
                            +row['Value'].decode('cp1251').encode("utf-8")+' '+row['TU GOST'].decode('cp1251').encode("utf-8")+' '+row['PartDocument'].decode('cp1251').encode("utf-8")
                            +'&'
                            +'&'
                            +col4.decode('cp1251').encode("utf-8")
                            +'\\'+'\\''\n')
        if row['Unplaced'] !=' ' and p != 2:
            st += 1
            ofile.write('&'
                        +'&'
                        +'&'
                        +row['Unplaced'].decode('cp1251').encode("utf-8")
                        +'\\'+'\\''\n')       
        vidpred = vid
        
    output_log_file.close()
    ifile.close()
    ofile.close()
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_1.csv')
    #os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_2.csv')
    #os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_3.csv')
    #os.remove(path)
    num += 5
    return num
    


