#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ilya.dementev
#
# Created:     29.06.2016
#-------------------------------------------------------------------------------

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
            if (row1['Name']==row1['Name'] and row1['PartNumber']==row2['PartNumber'] and row1['PartNumberRU']==row2['PartNumberRU'] and row1['PartDocument']==row2['PartDocument'] and row1['Unplaced']==row2['Unplaced']):
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
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile =open('output.tex', 'w')

    for row in readerd:
        ofile.write(row['RefDes']+'&'+row['Name']+row['PartNumber']+row['PartNumberRU']+row['Value']+row['TU GOST']+row['PartDocument']+'&'+row['kol']+'&'+row['Manufacturer']+row['Case']+row['Unplaced']+'\\'+'\\''\n')

        #strbuff = row['RefDes']+'&'+row['Name']+row['PartNumber']+row['PartNumberRU']+row['Value']+row['TU GOST']+row['PartDocument']+'&'+row['kol']+'&'+row['Manufacturer']+row['Case']+row['Unplaced']+strbuf

    ifile.close()
    ofile.close()
## THE END

if __name__ == '__main__':
    main()


