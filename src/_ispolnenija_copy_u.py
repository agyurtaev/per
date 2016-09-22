
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
                pr = 0
                pr_u = 0
                
                num_ch = len(nazv_isp)      
                while num_ch > 0:
                    if rowa[nazv_isp[num_ch-1]] == 'Unplaced':
                        row['Unplaced'] = '*'
                        pr_u = 1
                    num_ch -= 1
                    
                num_ch = len(nazv_isp)  
                while num_ch > 0:
                    if rowa[nazv_isp[num_ch-1]] != 'Unplaced':
                        row['Unplaced'] = ' '
                        pr = 1
                    num_ch -= 1
                    
                if row['PartNumber'] == ' ':
                    row['PartNumber'] = rowa['PartNumber']
                    
                if (pr_u == 1 and pr == 0) or (pr_u == 0 and pr == 1):
                    writerd.writerow(row)             
        ifilea.seek(0)
    ifile.close()
    ifilea.close()    
    ofile.close()

