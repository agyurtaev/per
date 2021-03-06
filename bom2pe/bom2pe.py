
# coding: utf8


def main():
    import csv
    import sys

    BOM_EMPTY_ITEM= " "
## Текст для настройки программы
    output_log_file =open('output.log', 'w')

    cfg_file  = open('bom2pe.cfg', 'rb')
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
                print "[INFO] Config file is loaded. UnplacedStr={%s}, TestPointStr={%s}" %(dni_str, tp_str)
                output_log_file.write("[INFO] Config file is loaded. UnplacedStr={%s}, TestPointStr={%s}\n" %(dni_str, tp_str))

## Первый проход: проверка атрибутов
    ifile  = open('projectname_tdd.csv', 'rb')
##    ifile  = codecs.open('projectname_tdd.csv', 'rb', 'utf-8')
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
                print "[INFO] CSV file header is loaded succesfully. header={%s}" %(header)
                output_log_file.write("[INFO] CSV file header is loaded succesfully. header={%s}\n" %(header))
        row_num+=1

    ifile.close()

## Второй проход: Работа с неустановленными

    ifile  = open('projectname_tdd.csv', 'rb')
    readerd.__init__(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)

    ofile  = open('projectname_tdd_pe3_1.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()

    for row in readerd:
        row_wr = row
        if row['Unplaced']!=BOM_EMPTY_ITEM:
            print '%s is unplaced {%s}, changing RefDes and note' % (row['RefDes'], row['Unplaced'])
            output_log_file.write('%s is unplaced {%s}, changing RefDes and note\n' % (row['RefDes'], row['Unplaced']))
##            dni_str ="*) не уст."
            row_wr['Unplaced']=dni_str
            row_wr['RefDes']=row_wr['RefDes'] +'*'
        writerd.writerow(row_wr)

    ifile.close()
    ofile.close()

## Второй проход: Удаление контрольных точек

    ifile  = open('projectname_tdd_pe3_1.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_pe3_2.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()

    for row in readerd:
        row_wr = row
        if row['Name']== tp_str:
            print '%s is Test Point, removing item' % (row['RefDes'])
            output_log_file.write('%s is Test Point, removing item\n' % (row['RefDes']))
##        if row['PartNumber']=='Testpoint_ALL_TYPES':
##            print 'Name is %s' % (row['Name'])
        else:
            writerd.writerow(row_wr)
    ifile.close()
    ofile.close()

## Третий проход: Работа с PartNumberRU и PartDocument

    ifile  = open('projectname_tdd_pe3_2.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_pe3_3.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()

    for row in readerd:
        row_wr = row
        if row['PartNumberRU']!=BOM_EMPTY_ITEM:
            print '%s has Russian Part Number = {%s}, removing common part number' % (row['RefDes'], row['PartNumberRU'])
            output_log_file.write('%s has Russian Part Number = {%s}, removing common part number\n' % (row['RefDes'], row['PartNumberRU']))
            row_wr['PartNumber']=BOM_EMPTY_ITEM
        writerd.writerow(row_wr)

    ifile.close()
    ofile.close()

## Четвёртый проход: Работа с PartDocument

    ifile  = open('projectname_tdd_pe3_3.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_pe3_4.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()

    for row in readerd:
        row_wr = row
        if row['PartDocument']!=BOM_EMPTY_ITEM:
            print '%s has Part Document = {%s}, removing common part number' % (row['RefDes'], row['PartDocument'])
            output_log_file.write('%s has Part Document = {%s}, removing common part number\n' % (row['RefDes'], row['PartDocument']))
            row_wr['PartNumber']=BOM_EMPTY_ITEM
        writerd.writerow(row_wr)

    ifile.close()
    ofile.close()

## Пятый проход: Работа с допустимыми заменами

    ifile  = open('projectname_tdd_pe3_4.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_pe3_5.csv', "wb")
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
                print 'Duplicated RefDes %s' % (row2['RefDes'])
                output_log_file.write('Duplicated RefDes %s\n' % (row2['RefDes']))
                if(row1['ReplacementPN']!=BOM_EMPTY_ITEM):
                    row1=row1 # откладываем запись, на следующем цикле запишетстя row1 в независимости от наличия в row2 замены
                else:
                    row1=row2 # откладываем запись, на следующем цикле запишетстя row2 в независимости от наличия в row2 замены
            else:
                writerd.writerow(row1)
            row1=row2
        row_num+=1
    print 'Last writeble RefDes %s' % (row1['RefDes'])
    output_log_file.write('Last writeble RefDes %s\n' % (row1['RefDes']))
    writerd.writerow(row1)

    ifile.close()
    ofile.close()



## Шестой проход: Вставляем количество

    ifile  = open('projectname_tdd_pe3_5.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_pe3_6.csv', "wb")
    header.append('kol')
    print header
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()

    row1 = {}
    
    for row in readerd:
        row['kol'] = 1     
        writerd.writerow(row)


    ifile.close()
    ofile.close()

## Седьмой проход: Объединяем + количество

    ifile  = open('projectname_tdd_pe3_6.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_pe3_7.csv', "wb")
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
                else:
                    row1['RefDes'] = refbuf + '-' + row2['RefDes']
            else:
                writerd.writerow(row1)
                row1 = row
        row_num+=1

        
    ifile.close()
    ofile.close()

## Седьмой проход: Латех
    
    ifile  = open('projectname_tdd_pe3_7.csv', "rb")
    #with open('projectname_tdd_pe3_7.csv', 'rb', encoding='utf-8') as ifile

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
            st += 1   
            ofile.write('&&&'+'\\'+'\\''\n')
            
        #l0 = len(row['RefDes'])
        #l1 = len(row['Name']+' '+row['PartNumber']+' '+row['PartNumberRU']+' '+row['Value']+' '+row['TU GOST']+' '+row['PartDocument'])
        #l2 = len(row['Manufacturer']+' '+row['Case']+' '+row['Unplaced'])

        #print l0, l1, l2

                
        #ofile.write('&&&'+'\\'+'\\''\n')

        col2 = row['Name']+' '+row['PartNumber']+' '+row['PartNumberRU']+' '+row['Value']+' '+row['TU GOST']+' '+row['PartDocument']

        #col4 = row['Manufacturer']+' '+row['Case']+' '+row['Unplaced']


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

        if len(col2)<50:
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
           
        if ((row['Value']!=' '  or row['TU GOST']!=' ' or row['PartDocument']!=' ') and p1 ==0) or p == 1 or p == 2:
            
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
        #strbuff = row['RefDes']+'&'+row['Name']+row['PartNumber']+row['PartNumberRU']+row['Value']+row['TU GOST']+row['PartDocument']+'&'+row['kol']+'&'+row['Manufacturer']+row['Case']+row['Unplaced']+strbuf
        vidpred = vid

    ifile.close()
    ofile.close()
## THE END

if __name__ == '__main__':
    main()


