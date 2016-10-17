# coding: utf8

def presort():
    
    import csv
    import sys
    import os
    
    BOM_EMPTY_ITEM= " "
    
    dr = os.path.dirname(__file__)   
    o = os.name
    if o=='nt':
        pr = dr.rfind ('\\')
    else: 
        pr = dr.rfind ('/')
    dr = dr[0:pr]
    dr1 = dr + '/csv/'
    dr2 = dr + '/template/'
    
    if not os.path.exists(os.path.abspath(dr1+'prochie_izdelija_bom.csv')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file prochie izdelija bom ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
    if not os.path.exists(os.path.abspath('bom2sp.cfg')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file bom2sp ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()


    
## Текст для настройки программы
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
                    and ('K' in cfg_headerd) and ('M' in cfg_headerd)
                    and ('Mk' in cfg_headerd) and ('k' in cfg_headerd)
                    ):
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
                K = row['k']
                
                output_log_file.write("[INFO] Config file is loaded. UnplacedStr={%s}, TestPointStr={%s}\n" %(dni_str, tp_str))
    cfg_file.close()
    
## Первый проход: проверка атрибутов
    pr_ch = 0
    ifile  = open(dr1+'prochie_izdelija_bom.csv', 'rb')
    reader  = csv.reader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    row_num = 0
    for row in ifile:
        if row_num==0:
            header=row
        if row_num==1:
            if row[0:3] == '---':
                pr_ch = 1
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
                ofile.write('&&&'+'prochie izdelija bom ERROR!!!'+'&&&'+'\\'+'\\''\n')
                output_log_file.close()
                ifile.close()
                ofile.close()
                sys.exit("[ERROR] No {RefDes} or {Unplaced} or {Name} fields. Exit")
            else:
                output_log_file.write("[INFO] CSV file header is loaded succesfully. header={%s}\n" %(header))
        row_num+=1
    ifile.close()

    if pr_ch == 1:
        ifile  = open(dr1+'prochie_izdelija_bom.csv', "rb")
        ofile =open('projectname_tdd_1.csv', 'wb')
        row_num = 0
        for row in ifile:
            if row_num != 1:
                ofile.write(row)
            row_num+=1       
        ifile.close()
        ofile.close()
        ifile  = open('projectname_tdd_1.csv', "rb")
        ofile =open(dr1+'prochie_izdelija_bom.csv', 'wb')
        for row in ifile:
            ofile.write(row)      
        ifile.close()
        ofile.close() 

    ifile  = open(dr1+'prochie_izdelija_bom.csv', "rb")
    ofile =open('projectname_tdd_1.csv', 'wb')
    row_num = 0
    for row in ifile:
        if row_num == 0:
            ofile.write('RefDes;Name;PartNumber;PartNumberRU;Value;TU GOST;PartDocument;Manufacturer;Unplaced;Case;TCx;PowerRating;Voltage;ReplacementPN;SpecSection;BomNote;Tolerance''\n')
        else:
            ofile.write(row)
        row_num+=1       
    ifile.close()
    ofile.close()
    ifile  = open('projectname_tdd_1.csv', "rb")
    ofile =open(dr1+'prochie_izdelija_bom.csv', 'wb')
    for row in ifile:
        ofile.write(row)      
    ifile.close()
    ofile.close()
    
    ifile  = open(dr1+'prochie_izdelija_bom.csv', 'rb')
    reader = csv.reader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    row_num = 0
    for row in reader:
        if row_num==0:
            header=row       
        row_num += 1
    ifile.seek(0)
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    ofile  = open('projectname_tdd_1.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    def conv(a):
        buf = a
        if buf != '' and buf != ' ':        
            l = len(buf)
            s = buf[l-1]
            while s == ' ':
                l = len(buf)
                buf = buf[0:l-1]
                l = len(buf)
                s = buf[l-1]        
                if l==1:
                    break
        if buf == '':
           buf = ' ' 
        return buf 
    for row in readerd:
        row['RefDes'] = conv(row['RefDes'])
        row['Name'] = conv(row['Name'])
        row['PartNumber'] = conv(row['PartNumber'])
        row['PartNumberRU'] = conv(row['PartNumberRU'])
        row['Value'] = conv(row['Value'])
        row['TU GOST'] = conv(row['TU GOST'])
        row['PartDocument'] = conv(row['PartDocument'])
        row['Manufacturer'] = conv(row['Manufacturer'])
        row['Unplaced'] = conv(row['Unplaced'])
        row['Case'] = conv(row['Case'])
        row['TCx'] = conv(row['TCx'])
        row['PowerRating'] = conv(row['PowerRating'])
        row['Voltage'] = conv(row['Voltage'])
        row['ReplacementPN'] = conv(row['ReplacementPN'])
        row['SpecSection'] = conv(row['SpecSection'])
        row['BomNote'] = conv(row['BomNote'])
        row['Tolerance'] = conv(row['Tolerance'])
        l = len(row['Value'])
        if row['Value'][l-1] == K:
            buf = row['Value']
            buf = buf[0:l-1] + k
            row['Value'] = buf
        l = len(row['Tolerance'])    
        if row['Tolerance'][l-1] == '%':
            buf = row['Tolerance']
            buf = buf[0:l-1]
            row['Tolerance'] = buf
        writerd.writerow(row)
    ifile.close()
    ofile.close()

    ifile  = open('projectname_tdd_1.csv', "rb")
    ofile =open(dr1+'prochie_izdelija_bom.csv', 'wb')
    for row in ifile:
        ofile.write(row)      
    ifile.close()
    ofile.close()

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
        l = len(row_wr['PartNumber'])
        buf = row_wr['PartNumber']
        while l > 0:
            ln = len(buf)
            if buf[l-1] == '#':
                if l < ln:
                    buf = buf[0:l-1]+ '\#' +buf[l:ln]
                else:
                    buf = buf[0:l-1]+ '\#'    
            l -= 1
        row_wr['PartNumber'] = buf        
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
        if row['RefDes'] != ' ':
            row['kol'] = 1
        else:
            row['kol'] = ' '
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
    row_un = 0
    ifile  = open('projectname_tdd_1.csv', "rb")
    ifilea =open('projectname_tdd_3.csv', 'wb')
    for row in ifile:
        row_un+=1
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
    priz = 0
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
                        if (row1['Name']==row2['Name'] and row1['PartNumber']==row2['PartNumber'] and row1['PartNumberRU']==row2['PartNumberRU']
                            and row1['PartDocument']==row2['PartDocument'] and row1['Unplaced']==row2['Unplaced']):
                            pr = 0    
                    if row_num_a > row_num:
                        if (row1['Name']==row2['Name'] and row1['PartNumber']==row2['PartNumber'] and row1['PartNumberRU']==row2['PartNumberRU']
                            and row1['PartDocument']==row2['PartDocument'] and row1['Unplaced']==row2['Unplaced']):
                            row1['kol'] =int(row1['kol']) + int(row2['kol'])               
                            refbuf = row1['RefDes']
                            row1['RefDes'] = refbuf + ',' + row2['RefDes']
                            if row_num_a == row_un:
                                priz = 1
                row_num_a+=1
            if pr == 1:       
                writerd.writerow(row1)   
        row1 = row
        row_num+=1 
        pr = 1
        ifilea.seek(0)
    if priz == 0:
        writerd.writerow(row1)
    ifile.close()
    ifilea.close()
    ofile.close()
#########################################
    ifile  = open('projectname_tdd_2.csv', "rb")
    ofile =open('projectname_tdd_2_b.csv', 'wb')
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()
#########################################    
    ifile  = open('projectname_tdd_2.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ifilea  = open('projectname_tdd_2_b.csv', "rb")    
    readerda = csv.DictReader(ifilea, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    unpl_spis = []
    row_num=0
    row_num_a=0
    for row in readerd:
        row_num_a = 0
        for rowa in readerda:
            if (row['Name']==rowa['Name'] and row['PartNumber']==rowa['PartNumber'] and row['PartNumberRU']==rowa['PartNumberRU']
                    and row['PartDocument']==rowa['PartDocument']):
                if row['Unplaced'] !=rowa['Unplaced']:
                    if not row['PartNumber']+row['PartNumberRU'] in unpl_spis:
                        unpl_spis.append(row['PartNumber']+row['PartNumberRU'])
            row_num_a+=1
        row_num += 1 
        ifilea.seek(0)
    ifile.close()
    ifilea.close()
    
    #print unpl_spis
    #c = raw_input()
    
#########################################
    
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

#########################################
    
## Одиннадцатый проход: Упорядочение по PartNum
## уст    
    ifile  = open('projectname_tdd_1.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_1_b.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    ofile_u  = open('projectname_tdd_1_u.csv', "wb")
    writerdu = csv.DictWriter(ofile_u, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)  
    writerdu.writeheader()
    up_spis = []
    vid = ''
    vidpred = ''
    row_num = 0
    ln_up_sp = 0
    for row in readerd:
        vid = row['RefDes'][0]
        if vid == 'D' or vid == 'd':
            vid = row['RefDes'][0] + row['RefDes'][1]
        if vid == 'V' or vid == 'v':
            vid = row['RefDes'][0] + row['RefDes'][1]
        if row_num == 0:
            vidpred = vid
            writerd.writeheader()
            writerd.writerow(row)
        if vid != vidpred:
            ofile.close()
            ifile_b  = open('projectname_tdd_1_b.csv', "rb")
            readerda.__init__(ifile_b, delimiter=";", quoting=csv.QUOTE_NONE)
            for rowa in readerda:
                up_spis.append(rowa['PartNumber'])
            ifile_b.close()
            
            up_spis.sort()
            
            ln_up_sp = len(up_spis)
            up_sp_count = 0
            while ln_up_sp > 0:
                ifile_b  = open('projectname_tdd_1_b.csv', "rb")
                readerda.__init__(ifile_b, delimiter=";", quoting=csv.QUOTE_NONE)
                for rowa in readerda:
                    if rowa['PartNumber'] == up_spis[up_sp_count]:
                        writerdu.writerow(rowa)
                ifile_b.close()
                up_sp_count += 1
                ln_up_sp -= 1
            
            
            up_spis = []
            ofile  = open('projectname_tdd_1_b.csv', "wb")
            writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)    
            writerd.writeheader()
            writerd.writerow(row)
        else:
            if row_num != 0:
                writerd.writerow(row)
        row_num+=1
        vidpred = vid
        

    ifile.close()
    ofile.close()
    
    ifile_b  = open('projectname_tdd_1_b.csv', "rb")
    readerda.__init__(ifile_b, delimiter=";", quoting=csv.QUOTE_NONE)
    for rowa in readerda:
        up_spis.append(rowa['PartNumber'])
    ifile_b.close()
    
    up_spis.sort()
    ln_up_sp = len(up_spis)
    up_sp_count = 0
    while ln_up_sp > 0:
        ifile_b  = open('projectname_tdd_1_b.csv', "rb")
        readerda.__init__(ifile_b, delimiter=";", quoting=csv.QUOTE_NONE)
        for rowa in readerda:
            if rowa['PartNumber'] == up_spis[up_sp_count]:
                writerdu.writerow(rowa)
        ifile_b.close()
        up_sp_count += 1
        ln_up_sp -= 1

    ofile_u.close()
    #print 'ok'
    #c = raw_input()

## неуст    
    ifile  = open('projectname_tdd_3.csv', "rb")
    readerd.__init__(ifile, delimiter=";", quoting=csv.QUOTE_NONE)
    ofile  = open('projectname_tdd_3_b.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    ofile_u  = open('projectname_tdd_3_u.csv', "wb")
    writerdu = csv.DictWriter(ofile_u, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)  
    writerdu.writeheader()
    up_spis = []
    vid = ''
    vidpred = ''
    row_num = 0
    ln_up_sp = 0
    for row in readerd:
        vid = row['RefDes'][0]
        if vid == 'D' or vid == 'd':
            vid = row['RefDes'][0] + row['RefDes'][1]
        if vid == 'V' or vid == 'v':
            vid = row['RefDes'][0] + row['RefDes'][1]
        if row_num == 0:
            vidpred = vid
            writerd.writeheader()
            writerd.writerow(row)
        if vid != vidpred:
            ofile.close()
            ifile_b  = open('projectname_tdd_3_b.csv', "rb")
            readerda.__init__(ifile_b, delimiter=";", quoting=csv.QUOTE_NONE)
            for rowa in readerda:
                up_spis.append(rowa['PartNumber'])
            ifile_b.close()
            
            up_spis.sort()
            
            ln_up_sp = len(up_spis)
            up_sp_count = 0
            while ln_up_sp > 0:
                ifile_b  = open('projectname_tdd_3_b.csv', "rb")
                readerda.__init__(ifile_b, delimiter=";", quoting=csv.QUOTE_NONE)
                for rowa in readerda:
                    if rowa['PartNumber'] == up_spis[up_sp_count]:
                        writerdu.writerow(rowa)
                ifile_b.close()
                up_sp_count += 1
                ln_up_sp -= 1
            
            
            up_spis = []
            ofile  = open('projectname_tdd_3_b.csv', "wb")
            writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)    
            writerd.writeheader()
            writerd.writerow(row)
        else:
            if row_num != 0:
                writerd.writerow(row)
        row_num+=1
        vidpred = vid
        
    
    
    ifile.close()
    ofile.close()
    
    
    ifile_b  = open('projectname_tdd_3_b.csv', "rb")
    readerda.__init__(ifile_b, delimiter=";", quoting=csv.QUOTE_NONE)
    for rowa in readerda:
        up_spis.append(rowa['PartNumber'])
    ifile_b.close()
    
    up_spis.sort()
    ln_up_sp = len(up_spis)
    up_sp_count = 0
    while ln_up_sp > 0:
        ifile_b  = open('projectname_tdd_3_b.csv', "rb")
        readerda.__init__(ifile_b, delimiter=";", quoting=csv.QUOTE_NONE)
        for rowa in readerda:
            if rowa['PartNumber'] == up_spis[up_sp_count]:
                writerdu.writerow(rowa)
        ifile_b.close()
        up_sp_count += 1
        ln_up_sp -= 1

    ofile_u.close()

#########################################
    ifile  = open('projectname_tdd_1_u.csv', "rb")
    ofile =open('projectname_tdd_1.csv', 'wb')
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()
#########################################
    ifile  = open('projectname_tdd_3_u.csv', "rb")
    ofile =open('projectname_tdd_3.csv', 'wb')
    for row in ifile:
        ofile.write(row)
    ifile.close()
    ofile.close()

    if os.path.exists(os.path.abspath('projectname_tdd_3_u.csv')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_3_u.csv')
        os.remove(path)

    if os.path.exists(os.path.abspath('projectname_tdd_3_b.csv')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_3_b.csv')
        os.remove(path)

    if os.path.exists(os.path.abspath('projectname_tdd_1_u.csv')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_1_u.csv')
        os.remove(path)

    if os.path.exists(os.path.abspath('projectname_tdd_1_b.csv')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_1_b.csv')
        os.remove(path)
        
    if os.path.exists(os.path.abspath('projectname_tdd_2_b.csv')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_2_b.csv')
        os.remove(path)       

    output_log_file.close()

    return unpl_spis
