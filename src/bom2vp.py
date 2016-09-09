
# coding: utf8

#- стандартные изделия;
#- прочие изделия; - из 2-х частей: бом + покупные
#- материалы;

######- данные для испонения


def main():
    import csv
    import sys
    import os
    
    import _stiz_vp
    import _priz_bom_vp
    import _priz_poc_vp
    import _mater_vp
 
    import _united_latex_vp
    import _red_latex_vp
    
    if not os.path.exists(os.path.abspath('remove_tex_trash.py')):
        print 'FATAL ERROR!!! \n' 
        ofile =open('reports.tex', 'w')
        ofile.write('&'+'file remove tex trash ERROR!!!'+'&&&&&&&&&'+'\\'+'\\''\n')
        ofile.close()
        sys.exit()    
    
#################################- перекодировка;
    def perecod(line):
        line = line.decode('cp1251').encode("utf-8")
        return line
  
#################################- стандартные изделия; Poz;Name;Kol
    _stiz_vp.stizgen(perecod)
#################################- прочие изделия; /Poz;Name;Kol
    _priz_bom_vp.prizgen(perecod)
    _priz_poc_vp.prizgen(perecod)
#################################- материалы; Name;Kol;Prim
    _mater_vp.matergen(perecod)
#################################- объединение разделов;
    _united_latex_vp.unite()
#################################- редактирование latex;
    row_num = 0
    row_num = _red_latex_vp.visstr()
    ofile =open('row_num.tex', 'w')
    if row_num > 3:
        row_num+=1
        ofile.write('\setcounter{page}{'+str(row_num)+'}')   
    else:
        ofile.write('\setcounter{page}{0}')  
    ofile.close()
    ofile =open('row_num_con.tex', 'w')
    #if row_num > 3:
        #row_num+=1
    ofile.write('\includepdf[pages={1-'+str(row_num-1)+'}]{__ved_poc}')   
    #else:
    #    ofile.write('\setcounter{page}{0}')  
    ofile.close()
if __name__ == '__main__':
    main()


