
# coding: utf8

def main():
    import csv
    import sys
    import os
    import shutil 
    from shutil import copyfile
    
    dr = os.path.dirname(__file__)   
    pr = dr.rfind ('\\')
    dr = dr[0:pr]
    dr1 = dr + '\\csv\\'
    dr2 = dr + '\\template\\'  
    if not os.path.exists(os.path.join((dr1), 'detali.csv')):
        copyfile(dr2 + 'detali.csv', dr1 + 'detali.csv')
        
    if not os.path.exists(os.path.join((dr1), 'dokumenty.csv')):
        copyfile(dr2 + 'dokumenty.csv', dr1 + 'dokumenty.csv')
        
    if not os.path.exists(os.path.join((dr1), 'kompleksy.csv')):
        copyfile(dr2 + 'kompleksy.csv', dr1 + 'kompleksy.csv')
        
    if not os.path.exists(os.path.join((dr1), 'materialy.csv')):
        copyfile(dr2 + 'materialy.csv', dr1 + 'materialy.csv')
        
    if not os.path.exists(os.path.join((dr1), 'detali.csv')):
        copyfile(dr2 + 'detali.csv', dr1 + 'detali.csv')
        
    if not os.path.exists(os.path.join((dr1), 'prochie_izdelija_bom.csv')):
        copyfile(dr2 + 'prochie_izdelija_bom.csv', dr1 + 'prochie_izdelija_bom.csv')
        
    if not os.path.exists(os.path.join((dr1), 'prochie_izdelija_pokupnye.csv')):
        copyfile(dr2 + 'prochie_izdelija_pokupnye.csv', dr1 + 'prochie_izdelija_pokupnye.csv')
        
    if not os.path.exists(os.path.join((dr1), 'sborochnye_edinicy.csv')):
        copyfile(dr2 + 'sborochnye_edinicy.csv', dr1 + 'sborochnye_edinicy.csv')
        
    if not os.path.exists(os.path.join((dr1), 'standartnye_izdelija.csv')):
        copyfile(dr2 + 'standartnye_izdelija.csv', dr1 + 'standartnye_izdelija.csv')

    if not os.path.exists(os.path.join((dr1), 'standartnye_izdelija.csv')):
        copyfile(dr2 + 'standartnye_izdelija.csv', dr1 + 'standartnye_izdelija.csv')
        
    if not os.path.exists(os.path.join((dr1), 'dannye_dokumenta.csv')):
        copyfile(dr2 + 'dannye_dokumenta.csv', dr1 + 'dannye_dokumenta.csv')        
if __name__ == '__main__':
    main()


