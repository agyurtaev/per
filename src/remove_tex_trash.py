
# coding: utf8

def main():
    import csv
    import sys
    import os
    
    if os.path.exists(os.path.abspath('__spec.aux')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.aux')
        #os.remove(path)
    if os.path.exists(os.path.abspath('__spec.dvi')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.dvi')
        #os.remove(path)
    if os.path.exists(os.path.abspath('__spec.log')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('__spec.out')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.out')
        os.remove(path)
    if os.path.exists(os.path.abspath('__spec.synctex.gz')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.synctex.gz')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_doc.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_doc.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_compl.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_compl.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_sbed.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_sbed.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_det.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_det.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_stiz.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_stiz.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_priz_bom.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_priz_bom.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_priz_poc.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_priz_poc.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_mater.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_mater.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_complect.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_complect.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('output.log')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports.tex')):        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('projectname_tdd_1.csv')):    
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_1.csv')
        os.remove(path)
    if os.path.exists(os.path.abspath('projectname_tdd_2.csv')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_2.csv')
        os.remove(path)
    if os.path.exists(os.path.abspath('projectname_tdd_3.csv')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_3.csv')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports1.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports1.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('_per.aux')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '_per.aux')
        #os.remove(path)
    if os.path.exists(os.path.abspath('_per.dvi')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '_per.dvi')
        os.remove(path)
    if os.path.exists(os.path.abspath('_per.log')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '_per.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('_per.out')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '_per.out')
        os.remove(path)
    if os.path.exists(os.path.abspath('_per.synctex.gz')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '_per.synctex.gz')
        os.remove(path)
    if os.path.exists(os.path.abspath('projectname_tdd_1.csv')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_1.csv')
        os.remove(path)
    if os.path.exists(os.path.abspath('projectname_tdd_2.csv')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'projectname_tdd_2.csv')
        os.remove(path)
    if os.path.exists(os.path.abspath('__ved_poc.aux')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.aux')
        #os.remove(path)
    if os.path.exists(os.path.abspath('__ved_poc.dvi')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.dvi')
        os.remove(path)
    if os.path.exists(os.path.abspath('__ved_poc.log')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('__ved_poc.out')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.out')
        os.remove(path)
    if os.path.exists(os.path.abspath('__ved_poc.synctex.gz')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.synctex.gz')
        os.remove(path)
    if os.path.exists(os.path.abspath('__reg_izm.log')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__reg_izm.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('__reg_izm.dvi')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__reg_izm.dvi')
        os.remove(path)
    if os.path.exists(os.path.abspath('__reg_izm.out')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__reg_izm.out')
        os.remove(path)
    if os.path.exists(os.path.abspath('__reg_izm.synctex.gz')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__reg_izm.synctex.gz')
        os.remove(path)
    if os.path.exists(os.path.abspath('__data_reg_izm.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__data_reg_izm.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('__data_pe.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__data_pe.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('__data_sp.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__data_sp.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('__data_vp.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__data_vp.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('row_num.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'row_num.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_det_bom.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_det_bom.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_det1.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_det1.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_sbed_bom.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_sbed_bom.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_sbed1.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_sbed1.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_stiz_bom.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_stiz_bom.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_stiz1.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_stiz1.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_info_case.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_info_case.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_info_case1.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_info_case1.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_info_case2.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_info_case2.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('reports_info_case3.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports_info_case3.tex')
        os.remove(path)
    if os.path.exists(os.path.abspath('case_sort.aux')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'case_sort.aux')
        #os.remove(path)
    if os.path.exists(os.path.abspath('case_sort.dvi')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'case_sort.dvi')
        #os.remove(path)
    if os.path.exists(os.path.abspath('case_sort.log')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'case_sort.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('case_sort.out')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'case_sort.out')
        os.remove(path)
    if os.path.exists(os.path.abspath('case_sort.synctex.gz')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'case_sort.synctex.gz')
        os.remove(path)
    if os.path.exists(os.path.abspath('concat.aux')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'concat.aux')
        #os.remove(path)
    if os.path.exists(os.path.abspath('concat.dvi')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'concat.dvi')
        #os.remove(path)
    if os.path.exists(os.path.abspath('concat.log')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'concat.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('concat.out')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'concat.out')
        os.remove(path)
    if os.path.exists(os.path.abspath('concat.synctex.gz')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'concat.synctex.gz')
        os.remove(path)
    if os.path.exists(os.path.abspath('row_num_con.tex')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'row_num_con.tex')
        os.remove(path)       
if __name__ == '__main__':
    main()


