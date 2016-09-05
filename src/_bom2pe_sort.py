
# coding: utf8


def main():
    import csv
    import sys
    import os
    
    BOM_EMPTY_ITEM= " "

    dr = os.path.dirname(__file__)   
    pr = dr.rfind ('\\')
    dr = dr[0:pr]
    dr1 = dr + '\\csv\\'
    dr2 = dr + '\\template\\'
    
    def perecod(line):
        line = line.decode('cp1251').encode("utf-8")
        return line

## Проверка наличия файлов
    if not os.path.isfile(os.path.abspath(dr1+'prochie_izdelija_bom.csv')):
        print sys.path
        print 'FATAL ERROR!!! \n'
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'
        +'file csv priz bom ERROR!!!' 
        +'&&'
        +'\\'+'\\''\n')
        ofile.close()
        sys.exit()        
    if not os.path.exists(os.path.abspath('bom2pe.cfg')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'
        +'file bom2pe ERROR!!!' 
        +'&&'
        +'\\'+'\\''\n')
        ofile.close()
        sys.exit()
    if not os.path.exists(os.path.abspath('changeSheet.tex')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'
        +'file changeSheet ERROR!!!' 
        +'&&'
        +'\\'+'\\''\n')
        ofile.close()
        sys.exit()
    if not os.path.exists(os.path.abspath('eskdper.sty')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'
        +'file eskdper ERROR!!!' 
        +'&&'
        +'\\'+'\\''\n')
        ofile.close()
        sys.exit()
    if not os.path.exists(os.path.abspath('remove_tex_trash.py')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'
        +'file remove tex trash ERROR!!!' 
        +'&&'
        +'\\'+'\\''\n')
        ofile.close()
        sys.exit()
## Текст для настройки программы
    output_log_file =open('output.log', 'w')
    cfg_file  = open('bom2pe.cfg', 'rb')
    cfg_readerd = csv.DictReader(cfg_file, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in cfg_readerd:
        if row_num==0:
            cfg_headerd=row
            if not (('UnplacedStr' in cfg_headerd) and ('TestPointStr' in cfg_headerd)
                    and ('Dop' in cfg_headerd) and ('Korp' in cfg_headerd)
                    and ('Volt' in cfg_headerd) and ('Om' in cfg_headerd)
                    and ('pF' in cfg_headerd) and ('F' in cfg_headerd)
                    and ('K' in cfg_headerd) and ('M' in cfg_headerd)
                    and ('Mk' in cfg_headerd)):
                Dop;Korp;Volt;Om;pF;F
                print 'FATAL ERROR!!! \n' 
                ofile =open('reports.tex', 'w')
                ofile.write('&'
                +'Conf file ERROR!!!' 
                +'&&'
                +'\\'+'\\''\n')
                output_log_file.close()
                ofile.close()
                sys.exit("[ERROR] Bad config file. No {UnplacedStr} or {TestPointStr} fields. Exit")
            else:
                dni_str = row['UnplacedStr']
                tp_str = row['TestPointStr']
                dop = row['Dop']
                korp = row['Korp']
                volt = row['Volt']
                om = row['Om']
                pf = row['pF']
                f = row['F']
                k = row['K']
                m = row['M']
                mk = row['Mk']
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
                    and ('BomNote' in headerd)and ('Tolerance' in headerd)):
                print 'FATAL ERROR!!! \n' 
                ofile =open('reports.tex', 'w')
                ofile.write('&'
                +'Bom file ERROR!!!'
                +'&&'
                +'\\'+'\\''\n')
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

## Восьмой проход: Объединие строк и подсчёт количества
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
                    row1['RefDes'] = refbuf + ',' + row2['RefDes']
                    output_log_file.write('United %s and %s\n' % (row1['RefDes'],row2['RefDes']))
                else:
                    row1['RefDes'] = refbuf + '-' + row2['RefDes']
                    output_log_file.write('United %s and %s\n' % (row1['RefDes'],row2['RefDes']))
            else:
                writerd.writerow(row1)
                row1 = row
        row_num+=1
    writerd.writerow(row1)
    ifile.close()
    ofile.close()

## Девятый проход: Латех   
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('reports.tex', 'w')
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


######################################################################################################## 2-й столбец
        #om = row['Om']
        #pf = row['pF']
        #f = row['F']
        
        val = 0
        s1 = []
        col2 = ''
        col2_list = []       
        if row['Value']!=' ' or row['TCx']!=' ' or row['PowerRating']!=' ' or row['Voltage']!= ' 'or row['Case']!= ' 'or row['Tolerance']!= ' ': 
            col2_list.append(row['Name'])
            col2_list.append(' ')
            col2_list.append(row['PartNumber'])
            col2_list.append(' ')
            col2_list.append(row['PartNumberRU'])
            col2_list.append(' (')

            if row['Case'] != ' ':
                col2_list.append(korp +' '+ row['Case'])
            else:
                col2_list.append('')
                
            if row['PowerRating'] != ' ' and row['Case'] != ' ':
                col2_list.append(', ')
            else:
                col2_list.append('')
            if row['PowerRating'] != ' ':   
                col2_list.append(row['PowerRating'])
            else:
                col2_list.append('')
                
            if row['TCx'] != ' ' and (row['PowerRating'] != ' ' or row['Case'] != ' '):
                col2_list.append(', ')
            else:
                col2_list.append('')
            if row['TCx'] != ' ':
                col2_list.append(row['TCx'])
            else:
                col2_list.append('')
                
            if row['Value'] != ' ' and (row['TCx'] != ' 'or row['PowerRating'] != ' ' or row['Case'] != ' '):
                col2_list.append(', ')
            else:
                col2_list.append('')
            if row['Value'] != ' ':
                if vid == 'C':
                    if mk in row['Value']:
                        col2_list.append(row['Value']+f)
                    else:
                        col2_list.append(row['Value']+' '+pf)
                if vid == 'R':
                    if k in row['Value'] or m in row['Value']:
                        col2_list.append(row['Value']+om)
                    else:
                        col2_list.append(row['Value']+' '+om)
                if vid != 'C' and vid != 'R':
                    col2_list.append(row['Value'])
            else:
                col2_list.append('')
                
            if row['Tolerance'] != ' ' and (row['Value'] != ' ' or row['TCx'] != ' 'or row['PowerRating'] != ' ' or row['Case'] != ' '):
                col2_list.append(', ')
            else:
                col2_list.append('')
            if row['Tolerance'] != ' ':
                col2_list.append('+/-'+row['Tolerance']+'\%')
            else:
                col2_list.append('')
                
            if row['Voltage'] != ' ' and (row['Tolerance'] != ' ' or row['Value'] != ' ' or row['TCx'] != ' 'or row['PowerRating'] != ' ' or row['Case'] != ' '):
                col2_list.append(', ')
            else:
                col2_list.append('')
            if row['Voltage'] != ' ':
                col2_list.append(row['Voltage']+volt)
            else:
                col2_list.append('')           
            col2_list.append(') ')
            col2_list.append(row['TU GOST'])
            col2_list.append(' ')
            col2_list.append(row['PartDocument'])
            val = 0
        else:
            col2_list.append(row['Name'])
            col2_list.append(' ')
            col2_list.append(row['PartNumber'])
            col2_list.append(' ')
            col2_list.append(row['PartNumberRU'])
            col2_list.append(' ')
            col2_list.append(row['TU GOST'])
            col2_list.append(' ')
            col2_list.append(row['PartDocument'])            
            val = 1
        lens2 = 50
################################################ 1-я строка        
        count  = len(col2_list)
        while count > 0:
            col2 = col2_list[count-1] + col2
            count -=1
        if len(col2)<lens2: 
            col2 = ''
            count  = len(col2_list)
            while count > 0:
                col2 = col2_list[count-1] + col2
                count -=1
            if col2 != '':
                s1.append(col2)
            count  = len(col2_list)
            while count > 0:
                count -=1                     
                col2_list.pop(count)             
        else:##del PartDocument
            col2 = ''
            count  = len(col2_list)            
            count -=2              
            while count > 0:
                col2 = col2_list[count-1] + col2
                count -=1                            
            if len(col2)<lens2:
                if col2 != '':
                    s1.append(col2)
                count  = len(col2_list)
                count -=2
                while count > 0:
                    count -=1                     
                    col2_list.pop(count)                                                   
            else:##del TU GOST
                col2 = ''
                count  = len(col2_list) 
                count -=3              
                while count > 0:
                    col2 = col2_list[count-1] + col2
                    count -=1                            
                if len(col2)<lens2:
                    if col2 != '':
                        s1.append(col2)
                    count  = len(col2_list)
                    count -=3 
                    while count > 0:                   
                        count -=1
                        col2_list.pop(count) 
                else:##del Value/PartNum
                    if val == 0:
                        col2 = ''
                        count  = len(col2_list) 
                        count -=16              
                        while count > 0:
                            col2 = col2_list[count-1] + col2
                            count -=1                            
                        if len(col2)<lens2:
                            if col2 != '':
                                s1.append(col2)
                            count  = len(col2_list)
                            count -=16 
                            while count > 0:
                                count -=1
                                col2_list.pop(count) 
                    if val == 1:
                        col2 = ''
                        count  = len(col2_list) 
                        count -=8              
                        while count > 0:
                            col2 = col2_list[count-1] + col2
                            count -=1                            
                        if len(col2)<lens2:
                            if col2 != '':
                                s1.append(col2)
                            count  = len(col2_list)
                            count -=8 
                            while count > 0:                   
                                count -=1
                                col2_list.pop(count) 
                    if len(col2) >= lens2:##PartNum
                        if val == 0:
                            col2 = ''
                            count  = len(col2_list) 
                            count -=20              
                            while count > 0:
                                col2 = col2_list[count-1] + col2
                                count -=1                            
                            if len(col2)<lens2:
                                if col2 != '':
                                    s1.append(col2)
                                count  = len(col2_list)
                                count -=20 
                                while count > 0:
                                    count -=1
                                    col2_list.pop(count) 
                    if len(col2) >= lens2:
                        print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                        ofile.close()
                        ofile =open('reports.tex', 'w')
                        ofile.write('&'
                        +'LEN ERROR!!! %s' % (row['RefDes'])
                        +'&&'
                        +'\\'+'\\''\n')
                        output_log_file.close()
                        ifile.close()
                        ofile.close()
                        sys.exit()
################################################ 2-я строка
        count  = len(col2_list)
        while count > 0:
            col2 = col2_list[count-1] + col2
            count -=1
        if len(col2)<lens2: 
            col2 = ''
            count  = len(col2_list)
            while count > 0:
                col2 = col2_list[count-1] + col2
                count -=1
            if col2 != '':
                s1.append(col2)
            count  = len(col2_list)
            while count > 0:
                count -=1                     
                col2_list.pop(count) 
        else:##del PartDocument
            col2 = ''
            count  = len(col2_list)            
            count -=2              
            while count > 0:
                col2 = col2_list[count-1] + col2
                count -=1                            
            if len(col2)<lens2:
                if col2 != '':
                    s1.append(col2)
                count  = len(col2_list)
                count -=2
                while count > 0:
                    count -=1                     
                    col2_list.pop(count)                                                   
            else:##del TU GOST
                col2 = ''
                count  = len(col2_list) 
                count -=3              
                while count > 0:
                    col2 = col2_list[count-1] + col2
                    count -=1                            
                if len(col2)<lens2:
                    if col2 != '':
                        s1.append(col2)
                    count  = len(col2_list)
                    count -=3 
                    while count > 0:                   
                        count -=1
                        col2_list.pop(count) 
                else:##del Value
                    if val == 0:
                        col2 = ''
                        count  = len(col2_list) 
                        count -=16              
                        while count > 0:
                            col2 = col2_list[count-1] + col2
                            count -=1                            
                        if len(col2)<lens2:
                            if col2 != '':
                                s1.append(col2)
                            count  = len(col2_list)
                            count -=16 
                            while count > 0:
                                count -=1
                                col2_list.pop(count)  
                    if len(col2) >= lens2:
                        print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                        ofile.close()
                        ofile =open('reports.tex', 'w')
                        ofile.write('&'
                        +'LEN ERROR!!! %s' % (row['RefDes'])
                        +'&&'
                        +'\\'+'\\''\n')
                        output_log_file.close()
                        ifile.close()
                        ofile.close()
                        sys.exit()
                        
################################################ 3-я строка
        count  = len(col2_list)
        while count > 0:
            col2 = col2_list[count-1] + col2
            count -=1
        if len(col2)<lens2: 
            col2 = ''
            count  = len(col2_list)
            while count > 0:
                col2 = col2_list[count-1] + col2
                count -=1
            if col2 != '':
                s1.append(col2)
            count  = len(col2_list)
            while count > 0:
                count -=1                     
                col2_list.pop(count) 
        else:##del PartDocument
            col2 = ''
            count  = len(col2_list)            
            count -=2              
            while count > 0:
                col2 = col2_list[count-1] + col2
                count -=1                            
            if len(col2)<lens2:
                if col2 != '':
                    s1.append(col2)
                count  = len(col2_list)
                count -=2
                while count > 0:
                    count -=1                     
                    col2_list.pop(count)                                                   
            else:##del TU GOST
                if val == 0:
                    col2 = ''
                    count  = len(col2_list) 
                    count -=3              
                    while count > 0:
                        col2 = col2_list[count-1] + col2
                        count -=1                            
                    if len(col2)<lens2:
                        if col2 != '':
                            s1.append(col2)
                        count  = len(col2_list)
                        count -=3 
                        while count > 0:
                            count -=1
                            col2_list.pop(count)  
                if len(col2) >= lens2:
                    print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                    ofile.close()
                    ofile =open('reports.tex', 'w')
                    ofile.write('&'
                    +'LEN ERROR!!! %s' % (row['RefDes'])
                    +'&&'
                    +'\\'+'\\''\n')
                    output_log_file.close()
                    ifile.close()
                    ofile.close()
                    sys.exit()
                    
################################################ 4-я строка
        count  = len(col2_list)
        while count > 0:
            col2 = col2_list[count-1] + col2
            count -=1
        if len(col2)<lens2: 
            col2 = ''
            count  = len(col2_list)
            while count > 0:
                col2 = col2_list[count-1] + col2
                count -=1
            if col2 != '':
                s1.append(col2)
            count  = len(col2_list)
            while count > 0:
                count -=1                     
                col2_list.pop(count) 
        else:##del PartDocument
            if val == 0:
                col2 = ''
                count  = len(col2_list) 
                count -=2              
                while count > 0:
                    col2 = col2_list[count-1] + col2
                    count -=1                            
                if len(col2)<lens2:
                    if col2 != '':
                        s1.append(col2)
                    count  = len(col2_list)
                    count -=2 
                    while count > 0:
                        count -=1
                        col2_list.pop(count)  
            if len(col2) >= lens2:
                print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                ofile.close()
                ofile =open('reports.tex', 'w')
                ofile.write('&'
                +'LEN ERROR!!! %s' % (row['RefDes'])
                +'&&'
                +'\\'+'\\''\n')
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit()

################################################ Допустимые замены
        col2 = ''
        if row['ReplacementPN']!=' ':
            col2 = dop + ' (' + row['ReplacementPN']+')'
            if len(col2)<50:
                s1.append(col2)
            else:
                print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                ofile.close()
                ofile =open('reports.tex', 'w')
                ofile.write('&'
                +'LEN ERROR!!! %s ' % (row['RefDes'])
                +'&&'
                +'\\'+'\\''\n')
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit()                
                
        count = len(s1)
        while count > 0:
            count -=1
            if s1[count]== '  ':
                s1.pop(count)
                count = len(s1)
        count = len(s1)        
        while count > 0:
            count -=1
            if s1[count]== ' ':
                s1.pop(count)
                
######################################################################################################## 4-й столбец
        s2 = []
        col4 = ''
        col4_list = []       
        col4_list.append(row['Unplaced'])
        col4_list.append(' ')
        col4_list.append(row['Manufacturer'])
        col4_list.append(' ')
        col4_list.append(row['BomNote'])
        lens4 = 20
################################################ 1-я строка        
        count  = len(col4_list)
        while count > 0:
            col4 = col4_list[count-1] + col4
            count -=1
        if len(col4)<lens4: 
            col4 = ''
            count  = len(col4_list)
            while count > 0:
                col4 = col4_list[count-1] + col4
                count -=1
            if col4 != '':
                s2.append(col4)
            count  = len(col4_list)
            while count > 0:
                count -=1                     
                col4_list.pop(count)             
        else:##del BomNote
            col4 = ''
            count  = len(col4_list)            
            count -=2              
            while count > 0:
                col4 = col4_list[count-1] + col4
                count -=1                            
            if len(col4)<lens4:
                if col4 != '':
                    s2.append(col4)
                count  = len(col4_list)
                count -=2
                while count > 0:
                    count -=1                     
                    col4_list.pop(count)                                                   
            else:##del Manufacturer
                col4 = ''
                count  = len(col4_list)            
                count -=4              
                while count > 0:
                    col4 = col4_list[count-1] + col4
                    count -=1                            
                if len(col4)<lens4:
                    if col4 != '':
                        s2.append(col4)
                    count  = len(col4_list)
                    count -=4
                    while count > 0:
                        count -=1                     
                        col4_list.pop(count)
                else:   
                    print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                    ofile.close()
                    ofile =open('reports.tex', 'w')
                    ofile.write('&'
                    +'LEN ERROR!!! %s' % (row['RefDes'])
                    +'&&'
                    +'\\'+'\\''\n')
                    output_log_file.close()
                    ifile.close()
                    ofile.close()
                    sys.exit()
                
################################################ 2-я строка        
        count  = len(col4_list)
        while count > 0:
            col4 = col4_list[count-1] + col4
            count -=1
        if len(col4)<lens4: 
            col4 = ''
            count  = len(col4_list)
            while count > 0:
                col4 = col4_list[count-1] + col4
                count -=1
            if col4 != '':
                s2.append(col4)
            count  = len(col4_list)
            while count > 0:
                count -=1                     
                col4_list.pop(count)
        else:##del BomNote
            col4 = ''
            count  = len(col4_list)            
            count -=2              
            while count > 0:
                col4 = col4_list[count-1] + col4
                count -=1                            
            if len(col4)<lens4:
                if col4 != '':
                    s2.append(col4)
                count  = len(col4_list)
                count -=2
                while count > 0:
                    count -=1                     
                    col4_list.pop(count) 
            else:
                print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
                ofile.close()
                ofile =open('reports.tex', 'w')
                ofile.write('&'
                +'LEN ERROR!!! %s' % (row['RefDes'])
                +'&&'
                +'\\'+'\\''\n')
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit()
################################################ 3-я строка        
        count  = len(col4_list)
        while count > 0:
            col4 = col4_list[count-1] + col4
            count -=1
        if len(col4)<lens4: 
            col4 = ''
            count  = len(col4_list)
            while count > 0:
                col4 = col4_list[count-1] + col4
                count -=1
            if col4 != '':
                s2.append(col4)
            count  = len(col4_list)
            while count > 0:
                count -=1                     
                col4_list.pop(count)
        else:
            print 'FATAL ERROR!!! %s \n' % (row['RefDes'])
            ofile.close()
            ofile =open('reports.tex', 'w')
            ofile.write('&'
            +'LEN ERROR!!! %s' % (row['RefDes'])
            +'&&'
            +'\\'+'\\''\n')
            output_log_file.close()
            ifile.close()
            ofile.close()
            sys.exit()

        count = len(s2)
        while count > 0:
            count -=1
            if s2[count]== '  ':
                s2.pop(count)
        count = len(s2)        
        while count > 0:
            count -=1
            if s2[count]== ' ':
                s2.pop(count)            
            
########################################################################################################
        count1 = len(s1)
        count2 = len(s2)      
        if count1 > count2:
            count = count1
        else:
            count = count2
        count_u = count
        while count_u > 0:
            count_u -=1
            st += 1
        count_u = count
        number = 0      
        while count > 0:
            if number > count1 - 1:
                s1.append('')                                
            if number > count2 - 1:
                s2.append('')
                
            if count == count_u:                
                ofile.write(row['RefDes']
                            +'&'
                            +perecod(s1[number])
                            +'&'
                            +row['kol']
                            +'&'
                            +perecod(s2[number])
                            +'\\'+'\\''\n')
            else:
                ofile.write('&'
                            +perecod(s1[number])
                            +'&&'
                            +perecod(s2[number])
                            +'\\'+'\\''\n')
            number += 1
            count -= 1

        vidpred = vid
    output_log_file.close()
    ifile.close()
    ofile.close()

if __name__ == '__main__':
    main()


