
# coding: utf8


def isp():
    import csv
    import sys
    import os
    import shutil 
    from shutil import copyfile
    
    BOM_EMPTY_ITEM= " "
    o = os.name
    
    dr = os.path.dirname(__file__)   
    if o=='nt':
        pr = dr.rfind ('\\')
    else: 
        pr = dr.rfind ('/')
    dr = dr[0:pr]
    dr1 = dr + '/csv/'
    dr2 = dr + '/template/'
    
    def perecod(line):
        line = line.decode('cp1251').encode("utf-8")
        return line

## Проверка наличия файлов
    if not os.path.isfile(os.path.abspath(dr1+'bom_ispolnenij.txt')):
        print 'FATAL ERROR!!! \n'
        sys.exit()        
    if not os.path.exists(os.path.abspath(dr1+'varianty_ispolnenija.txt')):
        print 'FATAL ERROR!!! \n' 
        sys.exit()
    if not os.path.exists(os.path.abspath('_ispolnenija_red.cfg')):
        print 'FATAL ERROR!!! \n' 
        sys.exit()
    if not os.path.exists(os.path.join((dr1), 'dannye_dokumenta.csv')):
        copyfile(dr2 + 'dannye_dokumenta.csv', dr1 + 'dannye_dokumenta.csv') 
## CFG
    cfg_file  = open('_ispolnenija_red.cfg', 'rb')
    cfg_readerd = csv.DictReader(cfg_file, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in cfg_readerd:
        if row_num==0:
            cfg_headerd=row
            if not (('K' in cfg_headerd) and ('k' in cfg_headerd)):
                print 'FATAL ERROR!!! \n' 
                sys.exit()
            else:
                K = row['K']
                k = row['k']
    cfg_file.close()
    
## Удаление 2-й строки bom_ispolnenij
    ifile  = open(dr1+'bom_ispolnenij.txt', "rb")
    ofile =open('bom_ispolnenij_1.csv', 'wb')
    row_num = 0
    for row in ifile:
        if row_num != 1:
            if row_num == 0:
                ofile.write('RefDes;Name;PartNumber;PartNumberRU;Value;TU GOST;PartDocument;Manufacturer;Unplaced;Case;TCx;PowerRating;Voltage;ReplacementPN;SpecSection;BomNote;Tolerance''\n')
            else:
                ofile.write(row)
        row_num +=1
    ifile.close()
    ofile.close()
    
## Удаление пробелов, K и % bom_ispolnenij
    ifile  = open('bom_ispolnenij_1.csv', 'rb')
    reader = csv.reader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    row_num = 0
    for row in reader:
        if row_num==0:
            header=row       
        row_num += 1
    ifile.seek(0)
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    ofile  = open('bom_ispolnenij_2.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    def conv(a):
        buf = a
        l = len(buf)
        s = buf[l-1]
        while s == ' ':
            l = len(buf)
            buf = buf[0:l-1]
            l = len(buf)
            s = buf[l-1]        
            if l==1:
                break
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

    kol_isp = 0
    nazv_isp = []
    
## Удаление строк varianty_ispolnenija
    ifile  = open(dr1+'varianty_ispolnenija.txt', "rb")
    ofile =open('varianty_ispolnenija_1.csv', 'wb')
    row_num = 0
    for row in ifile:
        if (row_num != 0 and row_num != 1 and row_num != 2 and row_num != 3
            and row_num != 4 and row_num != 5 and row_num != 6 and row_num != 8
            and row[0]!= '+'):            
            l = len(row)
            ln = l
            while l > 0:
                if row[l-1] == '|':
                    buf = row
                    if buf[l] == ' ':
                        buf = buf[0:l-1] + ';' + buf[l+1:ln]
                    else:
                        buf = buf[0:l-1] + ';' + buf[l:ln]
                    row = buf
                l -= 1                
            if row_num == 7:
                l = len(row)
                ln = l
                while l > 0:
                    if row[l-1] == ' ':
                        buf = row
                        buf = buf[0:l-1] + buf[l:ln]
                        row = buf
                    l -= 1            
            ln = len(row)  
            if row[ln-3] == ';':
                row = row[1:ln-3]+row[ln-2:ln]
            else:
                if row[ln-2] == ';':
                    row = row[1:ln-2]+row[ln-1:ln]
                else:
                    row = row[1:ln]                    
            if row_num == 7:
                l = len(row)    
                while l > 0:
                    if row[l-1] == ';':
                        kol_isp += 1
                    l -= 1
                kol_isp -= 1                
            kol_isp_b = kol_isp    
            if row_num == 7:
                l = len(row)
                ln = l-1
                while l > 0:
                    if row[l-1] == ';' and kol_isp_b != 0:
                        nazv_isp.append(buf[l+1:ln])
                        ln -= len(buf[l:ln])
                        kol_isp_b -= 1
                    l -= 1
                nazv_isp.reverse()                
            ofile.write(row)
        row_num +=1
    ifile.close()
    ofile.close()

## Удаление пробелов varianty_ispolnenija
    ifile  = open('varianty_ispolnenija_1.csv', 'rb')
    reader = csv.reader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    row_num = 0
    for row in reader:
        if row_num==0:
            header=row       
        row_num += 1
    ifile.seek(0)
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    ofile  = open('varianty_ispolnenija_2.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    for row in readerd:
        kol_isp_b = kol_isp
        while kol_isp_b > 0:
            row[nazv_isp[kol_isp_b-1]] = conv (row[nazv_isp[kol_isp_b-1]])
            kol_isp_b -= 1
        row['RefDes']= conv (row['RefDes'])
        row['PartNumber']= conv (row['PartNumber'])
        writerd.writerow(row)
    ifile.close()
    ofile.close()

    return kol_isp, nazv_isp


