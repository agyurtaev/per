
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
    
    NUM = 1
    
#################################- документация;
    _doc.docgen()
#################################- комплексы;
    _compl.complgen()
#################################- сборочные единицы;
    NUM = _sbed.sbedgen(NUM)
#################################- детали;
    NUM = _det.detgen(NUM)
#################################- стандартные изделия;
    NUM = _stiz.stizgen(NUM)
#################################- прочие изделия;
    NUM = _priz_bom.prizgen(NUM)
    NUM = _priz_poc.prizgen(NUM)
#################################- материалы;
    _mater.matergen()
#################################- комплекты;
    _complect.complectgen()
#################################- данные для исполнений;
    #isp.ispgen()   
    
#################################- объединение разделов;
    _united_latex.unite()

if __name__ == '__main__':
    main()


