
# coding: utf8

def main():
    import csv
    import sys
    import os
    import shutil 
    from shutil import copyfile

    
    import _ispolnenija_red
    import _ispolnenija_copy
    import _ispolnenija_copy_u
    
    def perecod(line):
        line = line.decode('cp1251').encode("utf-8")
        return line
    
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
    num = kol_isp - 1
    _ispolnenija_copy_u.isp(num,nazv_isp)
    
    if o=='nt':
        os.system(put3+'___start_isp_pr_u.bat')
    if o=='posix':
        os.system('chmod +x '+put3+'___start_isp_pr_u.sh')
        os.system(put3+'./___start_isp_pr_u.sh')
        
    ofile =open('reports_info_case_buf.tex', 'w')
    ofile_sp =open('reports_sp_buf.tex', 'w')
    ofile_pe =open('reports_pe_buf.tex', 'w')

    
    ifile  = open('reports_info_case.tex', "rb")
    for row in ifile:
        ofile.write(row)
    ifile.close()
    
    ifile  = open('reports_sp_ob.tex', "rb")
    for row in ifile:
        ofile_sp.write(row)
    ifile.close()
    
    ifile  = open('reports_pe_ob.tex', "rb")
    for row in ifile:
        ofile_pe.write(row)
    ifile.close()

    
    
    copyfile(put4 + 'detali.csv', put4 + 'detali1.csv')
    copyfile(put4 + 'dokumenty.csv', put4 + 'dokumenty1.csv')
    copyfile(put4 + 'kompleksy.csv', put4 + 'kompleksy1.csv')
    copyfile(put4 + 'materialy.csv', put4 + 'materialy1.csv')
    copyfile(put4 + 'komplekty.csv', put4 + 'komplekty1.csv')
    copyfile(put4 + 'prochie_izdelija_pokupnye.csv', put4 + 'prochie_izdelija_pokupnye1.csv')
    copyfile(put4 + 'sborochnye_edinicy.csv', put4 + 'sborochnye_edinicy1.csv')
    copyfile(put4 + 'standartnye_izdelija.csv', put4 + 'standartnye_izdelija1.csv')
    
    ofile_sp.write('\\newpage'+'\n')
    ofile_sp.write('&&&'+'\hspace{3.6 cm}\underline{'+'Переменные данные'+'}'+'&'+'\underline{для исполнения}'+'&&'+'\\'+'\\''\n')
    ofile_pe.write('\\newpage'+'\n')
    
    #.decode('cp1251').encode("utf-8")

    ch_isp = 0
    while kol_isp > 0:
        
        num = kol_isp - 1
        
        if not os.path.exists(os.path.join((put4), 'detali_'+nazv_isp[num]+'.csv')):
            copyfile(put2 + 'detali.csv', put4 + 'detali.csv')
        else:
            copyfile(put4+'detali_'+nazv_isp[num]+'.csv', put4 + 'detali.csv')
            
        if not os.path.exists(os.path.join((put4), 'dokumenty_'+nazv_isp[num]+'.csv')):
            copyfile(put2 + 'dokumenty.csv', put4 + 'dokumenty.csv')
        else:
            copyfile(put4+'dokumenty_'+nazv_isp[num]+'.csv', put4 + 'dokumenty.csv')
            
        if not os.path.exists(os.path.join((put4), 'kompleksy_'+nazv_isp[num]+'.csv')):
            copyfile(put2 + 'kompleksy.csv', put4 + 'kompleksy.csv')
        else:
            copyfile(put4+'kompleksy_'+nazv_isp[num]+'.csv', put4 + 'kompleksy.csv')
            
        if not os.path.exists(os.path.join((put4), 'materialy_'+nazv_isp[num]+'.csv')):
            copyfile(put2 + 'materialy.csv', put4 + 'materialy.csv')
        else:
            copyfile(put4+'materialy_'+nazv_isp[num]+'.csv', put4 + 'materialy.csv')        

        if not os.path.exists(os.path.join((put4), 'komplekty_'+nazv_isp[num]+'.csv')):
            copyfile(put2 + 'komplekty.csv', put4 + 'komplekty.csv')
        else:
            copyfile(put4+'komplekty_'+nazv_isp[num]+'.csv', put4 + 'komplekty.csv')
            
        if not os.path.exists(os.path.join((put4), 'prochie_izdelija_pokupnye_'+nazv_isp[num]+'.csv')):
            copyfile(put2 + 'prochie_izdelija_pokupnye.csv', put4 + 'prochie_izdelija_pokupnye.csv')
        else:
            copyfile(put4+'prochie_izdelija_pokupnye_'+nazv_isp[num]+'.csv', put4 + 'prochie_izdelija_pokupnye.csv')
            
        if not os.path.exists(os.path.join((put4), 'sborochnye_edinicy_'+nazv_isp[num]+'.csv')):
            copyfile(put2 + 'sborochnye_edinicy.csv', put4 + 'sborochnye_edinicy.csv')
        else:
            copyfile(put4+'sborochnye_edinicy_'+nazv_isp[num]+'.csv', put4 + 'sborochnye_edinicy.csv')
            
        if not os.path.exists(os.path.join((put4), 'standartnye_izdelija_'+nazv_isp[num]+'.csv')):
            copyfile(put2 + 'standartnye_izdelija.csv', put4 + 'standartnye_izdelija.csv')
        else:
            copyfile(put4+'standartnye_izdelija_'+nazv_isp[num]+'.csv', put4 + 'standartnye_izdelija.csv')  

        _ispolnenija_copy.isp(num,nazv_isp)

        if o=='nt':
            os.system(put3+'___start_isp_pr.bat')
        if o=='posix':
            os.system('chmod +x '+put3+'___start_isp_pr.sh')
            os.system(put3+'./___start_isp_pr.sh')
        kol_isp -= 1
        
        ifile  = open('reports_info_case.tex', "rb")
        for row in ifile:
            ofile.write(row)
        ifile.close()

        ifile  = open(put4 + 'dannye_dokumenta.csv', 'rb')
        readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
        sign = ''
        for row in readerd:
            sign = row['signature']
        ifile.close()

        sign = perecod(sign)

        pr_pus = 0
        numrow = 0
        strok = '&&&&       & &\\'
        ifile  = open('reports_sp.tex', "rb")
        for row in ifile:
            if strok in row:
                pr_pus = 1
            numrow += 1
        ifile.close()
        
        if ch_isp != 0:
            ofile_sp.write('\\newpage'+'\n')
            
        ofile_sp.write('&&&&&&'+'\\'+'\\''\n')
        
        if ch_isp == 0:
            if pr_pus == 0:
                ofile_sp.write('&&&&'+sign+'&&'+'\\'+'\\''\n')
        else:
            if ch_isp < 10:
                if pr_pus == 0:
                    ofile_sp.write('&&&&'+sign+'-0'+str(ch_isp)+'&&'+'\\'+'\\''\n')
            else:
                if pr_pus == 0:
                    ofile_sp.write('&&&&'+sign+'-'+str(ch_isp)+'&&'+'\\'+'\\''\n')
        ofile_sp.write('&&&&&&'+'\\'+'\\''\n')
        
        ifile  = open('reports_sp.tex', "rb")
        for row in ifile:
            ofile_sp.write(row)
        ifile.close()
        
        pr_pus = 0
        numrow = 0
        strok = '&         & &   \\'
        ifile  = open('reports_pe.tex', "rb")
        for row in ifile:
            if numrow == 2:
                if strok in row:
                    pr_pus = 1
            numrow += 1
        ifile.close()
        
        if ch_isp != 0 and pr_pus == 0:
            ofile_pe.write('\\newpage'+'\n')        

        ofile_pe.write('&&&'+'\\'+'\\''\n')

        if ch_isp == 0:
            if pr_pus == 0:
                ofile_pe.write('&'+sign+'&&'+'\\'+'\\''\n')
        else:
            if ch_isp < 10:
                if pr_pus == 0:
                    ofile_pe.write('&'+sign+'-0'+str(ch_isp)+'&&'+'\\'+'\\''\n')
            else:
                if pr_pus == 0:
                    ofile_pe.write('&'+sign+'-'+str(ch_isp)+'&&'+'\\'+'\\''\n')
        ofile_pe.write('&&&'+'\\'+'\\''\n')

        ifile  = open('reports_pe.tex', "rb")
        for row in ifile:
            ofile_pe.write(row)
        ifile.close()
        
        ch_isp +=1
        
    copyfile(put4 + 'detali1.csv', put4 + 'detali.csv')
    os.remove(put4 + 'detali1.csv')

    copyfile(put4 + 'dokumenty1.csv', put4 + 'dokumenty.csv')
    os.remove(put4 + 'dokumenty1.csv')

    copyfile(put4 + 'kompleksy1.csv', put4 + 'kompleksy.csv')
    os.remove(put4 + 'kompleksy1.csv')

    copyfile(put4 + 'materialy1.csv', put4 + 'materialy.csv')
    os.remove(put4 + 'materialy1.csv')

    copyfile(put4 + 'komplekty1.csv', put4 + 'komplekty.csv')
    os.remove(put4 + 'komplekty1.csv')

    copyfile(put4 + 'prochie_izdelija_pokupnye1.csv', put4 + 'prochie_izdelija_pokupnye.csv')
    os.remove(put4 + 'prochie_izdelija_pokupnye1.csv')
    
    copyfile(put4 + 'sborochnye_edinicy1.csv', put4 + 'sborochnye_edinicy.csv')
    os.remove(put4 + 'sborochnye_edinicy1.csv')
    
    copyfile(put4 + 'standartnye_izdelija1.csv', put4 + 'standartnye_izdelija.csv')
    os.remove(put4 + 'standartnye_izdelija1.csv')


    ofile.close()    
    
    copyfile(put3+'reports_info_case_buf.tex', put3 + 'reports_info_case.tex')
    os.remove(put3 + 'reports_info_case_buf.tex')

    ofile_sp.close()
    
    copyfile(put3+'reports_sp_buf.tex', put3 + 'reports_sp.tex')
    os.remove(put3 + 'reports_sp_buf.tex')
    
    ofile_pe.close()
    
    copyfile(put3+'reports_pe_buf.tex', put3 + 'reports_pe.tex')
    os.remove(put3 + 'reports_pe_buf.tex')

    if o=='nt':
        os.system(put3+'___start_isp_tex.bat')
    if o=='posix':
        os.system('chmod +x '+put3+'___start_isp_tex.sh')
        os.system(put3+'./___start_isp_tex.sh')    
    
    
    if os.path.exists(os.path.abspath('num.txt')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'num.txt')
        os.remove(path)
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
    if os.path.exists(put4 + 'dannye_dokumenta_1.csv'):
        path = put4 + 'dannye_dokumenta_1.csv'
        os.remove(path) 
if __name__ == '__main__':
    main()
