
# coding: utf8

def main():
    import csv
    import sys
    import os
    import shutil 
    from shutil import copyfile
    
    dr = os.path.dirname(__file__)
    o = os.name
    if o=='nt':
        pr = dr.rfind ('\\')
    else: 
        pr = dr.rfind ('/')    
    dr = dr[0:pr]
    dr1 = dr + '/csv/'
    dr2 = dr + '/template/'
    
    if not os.path.exists(os.path.join((dr1), 'detali.csv')):
        copyfile(dr2 + 'detali.csv', dr1 + 'detali.csv')
        
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'detali.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'detali.csv', dr1 + 'detali.csv')    
        
    if not os.path.exists(os.path.join((dr1), 'dokumenty.csv')):
        copyfile(dr2 + 'dokumenty.csv', dr1 + 'dokumenty.csv')
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'dokumenty.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'dokumenty.csv', dr1 + 'dokumenty.csv')
        
    if not os.path.exists(os.path.join((dr1), 'kompleksy.csv')):
        copyfile(dr2 + 'kompleksy.csv', dr1 + 'kompleksy.csv')
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'kompleksy.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'kompleksy.csv', dr1 + 'kompleksy.csv')
        
    if not os.path.exists(os.path.join((dr1), 'materialy.csv')):
        copyfile(dr2 + 'materialy.csv', dr1 + 'materialy.csv')
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'materialy.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'materialy.csv', dr1 + 'materialy.csv')
        
    if not os.path.exists(os.path.join((dr1), 'komplekty.csv')):
        copyfile(dr2 + 'komplekty.csv', dr1 + 'komplekty.csv')
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'komplekty.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'komplekty.csv', dr1 + 'komplekty.csv')
        
    if not os.path.exists(os.path.join((dr1), 'prochie_izdelija_bom.csv')):
        copyfile(dr2 + 'prochie_izdelija_bom.csv', dr1 + 'prochie_izdelija_bom.csv')
        
    if not os.path.exists(os.path.join((dr1), 'prochie_izdelija_pokupnye.csv')):
        copyfile(dr2 + 'prochie_izdelija_pokupnye.csv', dr1 + 'prochie_izdelija_pokupnye.csv')
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'prochie_izdelija_pokupnye.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'prochie_izdelija_pokupnye.csv', dr1 + 'prochie_izdelija_pokupnye.csv')
        
    if not os.path.exists(os.path.join((dr1), 'sborochnye_edinicy.csv')):
        copyfile(dr2 + 'sborochnye_edinicy.csv', dr1 + 'sborochnye_edinicy.csv')
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'sborochnye_edinicy.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'sborochnye_edinicy.csv', dr1 + 'sborochnye_edinicy.csv')
        
    if not os.path.exists(os.path.join((dr1), 'standartnye_izdelija.csv')):
        copyfile(dr2 + 'standartnye_izdelija.csv', dr1 + 'standartnye_izdelija.csv')
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'standartnye_izdelija.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'standartnye_izdelija.csv', dr1 + 'standartnye_izdelija.csv')
       
    if not os.path.exists(os.path.join((dr1), 'dannye_dokumenta.csv')):
        copyfile(dr2 + 'dannye_dokumenta.csv', dr1 + 'dannye_dokumenta.csv')
    row_num = 0
    kol = 0
    kol_p = 0
    pr_dif = 0
    ifile  = open(dr1 + 'dannye_dokumenta.csv', "rb")
    for row in ifile:
        if row_num == 0:
            st = row
            l = len(st)
            kol_p = 0
            while l > 0:
                if st[l-1] == ';':
                    kol += 1    
                st = st[0:l]
                l -= 1
        else:
            st = row
            l = len(st)
            while l > 0:
                if st[l-1] == ';':
                    kol_p += 1    
                st = st[0:l]
                l -= 1
            if kol_p != kol:
                pr_dif = 1
        row_num += 1
    ifile.close()
    if pr_dif == 1:
        copyfile(dr2 + 'dannye_dokumenta.csv', dr1 + 'dannye_dokumenta.csv')

if __name__ == '__main__':
    main()


