
# coding: utf8


def isp(num,nazv_isp):
    import csv
    import sys
    import os
    import shutil 
    from shutil import copyfile
    
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
      
########## 
    ifile  = open('bom_ispolnenij_2.csv', 'rb')
    reader = csv.reader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    row_num = 0
    for row in reader:
        if row_num==0:
            header=row       
        row_num += 1
    ifile.close()
    ifile  = open('bom_ispolnenij_2.csv', 'rb')
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    
    ifilea  = open('varianty_ispolnenija_2.csv', 'rb')
    readerda = csv.DictReader(ifilea, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    
    ofile  = open(dr1 +'prochie_izdelija_bom.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    
    for row in readerd:
        for rowa in readerda:
            if row ['RefDes'] == rowa ['RefDes']:
                if rowa[nazv_isp[num]] == 'Unplaced':
                    row['Unplaced'] = '*'
                if row['PartNumber'] == ' ':
                    row['PartNumber'] = rowa['PartNumber']
                writerd.writerow(row)
        ifilea.seek(0)
    ifile.close()
    ifilea.close()    
    ofile.close()
##########
    copyfile(dr1 + 'dannye_dokumenta.csv', dr1 + 'dannye_dokumenta_1.csv')
    
    ifile  = open(dr1 + 'dannye_dokumenta_1.csv', 'rb')
    reader = csv.reader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    row_num = 0
    for row in reader:
        if row_num==0:
            header=row       
        row_num += 1
    ifile.close()
    ifile  = open(dr1 + 'dannye_dokumenta_1.csv', 'rb')
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    
    ofile  = open(dr1 +'dannye_dokumenta.csv', "wb")
    writerd = csv.DictWriter(ofile, delimiter=';',fieldnames=header, quoting=csv.QUOTE_NONE)
    writerd.writeheader()
    
    for row in readerd:
        l = len(row['signature'])
        buf = row['signature']
        while l > 0:
            if buf[l-1] == '-':
                buf = buf[0:l-1]    
            l -= 1
        row['signature'] = buf
        if num != 0:
            if num < 10:
                row['signature'] = row['signature']+'-0'+str(num)
            else:
                row['signature'] = row['signature']+'-'+str(num)
        writerd.writerow(row)
    ifile.close()
    ifilea.close()    
    ofile.close()
