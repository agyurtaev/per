
# coding: utf8

def main():
    import csv
    import sys
    import os
    import shutil 
    from shutil import copyfile
    
    o = os.name
    put = os.getcwd()
    if o=='nt':
        pr = put.rfind ('\\')
    else: 
        pr = put.rfind ('/')
    put = put[0:pr]
    put1 = put + '/output/'
    put2 = put + '/template/'
    put3 = put + '/src/'
    put4 = put + '/csv/'

    nazv = ''
    cfg_file  = open('rename_pdf.cfg', 'rb')
    cfg_readerd = csv.DictReader(cfg_file, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in cfg_readerd:
        if row_num==0:
            cfg_headerd=row
            if not (('pe' in cfg_headerd) and ('vp' in cfg_headerd)
                    and ('lri' in cfg_headerd) and ('korp' in cfg_headerd)):
                print 'FATAL ERROR!!! \n' 
                sys.exit()
            else:
                pe = row['pe']
                vp = row['vp']
                lri = row['lri']
                korp = row['korp']
    cfg_file.close()

    
    ifile  = open(put4+'dannye_dokumenta.csv', 'rb')
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
        nazv = row['signature']
    ifile.close()
    if o=='nt':
        copyfile(put1 + '_per.pdf', put1 + nazv+' '+pe+'.pdf')
        copyfile(put1 + '__ved_poc.pdf', put1 + nazv+' '+vp+'.pdf')
        copyfile(put1 + '__spec.pdf', put1 + nazv+'.pdf')
        copyfile(put1 + '__reg_izm.pdf', put1 + nazv+' '+vp+' '+lri+'.pdf')
        copyfile(put1 + 'case_sort.pdf', put1 + nazv+' '+korp+'.pdf')
    else:
        copyfile(put1 + '_per.pdf', put1 + nazv.decode('cp1251').encode("utf-8")+' '+pe.decode('cp1251').encode("utf-8")+'.pdf')
        copyfile(put1 + '__ved_poc.pdf', put1 + nazv.decode('cp1251').encode("utf-8")+' '+vp.decode('cp1251').encode("utf-8")+'.pdf')
        copyfile(put1 + '__spec.pdf', put1 + nazv.decode('cp1251').encode("utf-8")+'.pdf')
        copyfile(put1 + '__reg_izm.pdf', put1 + nazv.decode('cp1251').encode("utf-8")+' '+vp.decode('cp1251').encode("utf-8")+' '+lri.decode('cp1251').encode("utf-8")+'.pdf')
        copyfile(put1 + 'case_sort.pdf', put1 + nazv.decode('cp1251').encode("utf-8")+' '+korp.decode('cp1251').encode("utf-8")+'.pdf')
        
    if os.path.exists(put1 + '_per.pdf'):
        path = put1 + '_per.pdf'
        os.remove(path)
    if os.path.exists(put1 + '__ved_poc.pdf'):
        path = put1 + '__ved_poc.pdf'
        os.remove(path)
    if os.path.exists(put1 + '__spec.pdf'):
        path = put1 + '__spec.pdf'
        os.remove(path)
    if os.path.exists(put1 + '__reg_izm.pdf'):
        path = put1 + '__reg_izm.pdf'
        os.remove(path)
    if os.path.exists(put1 + 'case_sort.pdf'):
        path = put1 + 'case_sort.pdf'
        os.remove(path)     
     
if __name__ == '__main__':
    main()


