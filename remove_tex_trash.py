
# coding: utf8

def main():
    import csv
    import sys
    import os
    
    if os.path.exists(os.path.abspath('__ved_poc.aux')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__ved_poc.aux')
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
if __name__ == '__main__':
    main()


