
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
    import _priz_bom
    import _priz_poc
    import _mater
    import _complect
    #import _isp
 
    import _united_latex
    import _red_latex
    
    NUM = 1
    
#################################- перекодировка;
    def perecod(line):
        line = line.decode('cp1251').encode("utf-8")
        return line
  
#################################- документация; Form;Oboz;Name
    _doc.docgen(perecod)
#################################- комплексы; Oboz;Name;Kol
    _compl.complgen(perecod)
#################################- сборочные единицы; Form;Poz;Oboz;Name;Kol
    NUM = _sbed.sbedgen(NUM,perecod)
#################################- детали; Form;Poz;Oboz;Name;Kol
    NUM = _det.detgen(NUM,perecod)
#################################- стандартные изделия; Poz;Name;Kol
    NUM = _stiz.stizgen(NUM,perecod)
#################################- прочие изделия; /Poz;Name;Kol
    NUM = _priz_bom.prizgen(NUM,perecod)
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
    

if __name__ == '__main__':
    main()


