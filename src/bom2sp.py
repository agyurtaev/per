
# coding: utf8

#- документация;
#- комплексы; #заготовка
#- сборочные единицы; 
#- детали;
#- стандартные изделия;
#- прочие изделия; - из 2-х частей: бом + покупные
#- материалы;
#- комплекты; #заготовка

######- данные для испонения
######- блоки -?

def main():
    import csv
    import sys
    import os
    
    import _doc
    import _compl
    import _sbed
    import _det
    import _stiz
    import _priz_bom_sort
    import _priz_bom_presort
    import _priz_poc
    import _mater
    import _complect
    #import _isp
 
    import _united_latex
    import _red_latex
    
    NUM = 15
    
    if os.path.exists(os.path.abspath('num.txt')):
        ifile  = open('num.txt', "rb")
        for row in ifile:
            NUM = int(row)
            NUM += 5
        ifile.close()
    else:
        NUM = 15
    
    
    NUM_sbed = 0
    NUM_det = 0
    NUM_stiz = 0
    unpl_spis = []
    if not os.path.exists(os.path.abspath('remove_tex_trash.py')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&&&'+'file remove tex trash ERROR!!!'+'&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()
        
#################################- перекодировка;
    def perecod(line):
        line = line.decode('cp1251').encode("utf-8")
        return line
  
#################################- документация; Form;Oboz;Name
    _doc.docgen(perecod)
#################################- комплексы; Oboz;Name;Kol
    _compl.complgen(perecod)
#################################
    unpl_spis=_priz_bom_presort.presort()
#################################- сборочные единицы; Form;Poz;Oboz;Name;Kol
    NUM,NUM_sbed = _sbed.sbedgen(NUM,perecod)
#################################- детали; Form;Poz;Oboz;Name;Kol
    NUM,NUM_det = _det.detgen(NUM,perecod)
#################################- стандартные изделия; Poz;Name;Kol
    NUM,NUM_stiz = _stiz.stizgen(NUM,perecod)
#################################- прочие изделия; /Poz;Name;Kol
    NUM = _priz_bom_sort.prizgen(NUM,perecod,NUM_sbed,NUM_det,NUM_stiz,unpl_spis)
    NUM = _priz_poc.prizgen(NUM,perecod)
#################################- материалы; Name;Kol;Prim
    _mater.matergen(perecod)
#################################- комплекты; Oboz;Name;Kol
    _complect.complectgen(perecod)
#################################- данные для исполнений;
    #isp.ispgen()     
#################################- объединение разделов;
    _united_latex.unite()
#################################- редактирование latex;
    _red_latex.visstr()
    
    ofile =open('num.txt', 'w')
    ofile.write(str(NUM))
    ofile.close()
    
    ofile =open('partn_old.txt', 'w')
    ofile.close()
    
    
if __name__ == '__main__':
    main()


