
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
    
    import _stiz
    import _priz_bom
    import _priz_poc
    import _mater
 
    import _united_latex
    import _red_latex
    
    
#################################- перекодировка;
    def perecod(line):
        line = line.decode('cp1251').encode("utf-8")
        return line
  
#################################- стандартные изделия; Poz;Name;Kol
    _stiz.stizgen(perecod)
#################################- прочие изделия; /Poz;Name;Kol
    _priz_bom.prizgen(perecod)
    _priz_poc.prizgen(perecod)
#################################- материалы; Name;Kol;Prim
    _mater.matergen(perecod)
#################################- объединение разделов;
    _united_latex.unite()
#################################- редактирование latex;
    _red_latex.visstr()
    

if __name__ == '__main__':
    main()


