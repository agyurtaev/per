
# coding: utf8

def main():
    import csv
    import sys
    import os
    import shutil 
    from shutil import copyfile

    
    import _ispolnenija_red
    import _ispolnenija_copy
    
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
    kol_isp = 0
    nazv_isp = []
    
    kol_isp, nazv_isp = _ispolnenija_red.isp()

    while kol_isp > 0:
        num = kol_isp - 1
        _ispolnenija_copy.isp(num,nazv_isp)

        if o=='nt':
            os.system(put3+'___start_isp_pr.bat')
        if o=='posix':
            os.system('chmod +x '+put3+'___start_isp_pr.sh')
            #os.system('gksudo '+put3+'./___start_isp_pr.sh')
            os.system(put3+'./___start_isp_pr.sh')
        
        copyfile(put1 + '_per.pdf', put1 + nazv_isp[num]+'_per.pdf')
        copyfile(put1 + '__ved_poc.pdf', put1 + nazv_isp[num]+'__ved_poc.pdf')
        copyfile(put1 + '__spec.pdf', put1 + nazv_isp[num]+'__spec.pdf')
        copyfile(put1 + '__reg_izm.pdf', put1 + nazv_isp[num]+'__reg_izm.pdf')
        copyfile(put1 + 'case_sort.pdf', put1 + nazv_isp[num]+'case_sort.pdf')
        kol_isp -= 1
        
    if os.path.exists(os.path.abspath('varianty_ispolnenija_1.csv')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'varianty_ispolnenija_1.csv')
        os.remove(path)
    if os.path.exists(os.path.abspath('varianty_ispolnenija_2.csv')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'varianty_ispolnenija_2.csv')
        os.remove(path)
    if os.path.exists(os.path.abspath('bom_ispolnenij_1.csv')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'bom_ispolnenij_1.csv')
        os.remove(path)
    if os.path.exists(os.path.abspath('bom_ispolnenij_2.csv')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'bom_ispolnenij_2.csv')
        os.remove(path)
    if os.path.exists(put4+'dannye_dokumenta_1.csv'):
        path = put4+'dannye_dokumenta_1.csv'
        os.remove(path)
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
