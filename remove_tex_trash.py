
# coding: utf8

def main():
    import csv
    import sys
    import os
    
    if os.path.exists(os.path.abspath('__spec.aux')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.aux')
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
    if os.path.exists(os.path.abspath('__ved_poc.log')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('__ved_poc.out')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.out')
        os.remove(path)
    if os.path.exists(os.path.abspath('__ved_poc.synctex.gz')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.synctex.gz')
        os.remove(path)
if __name__ == '__main__':
    main()


