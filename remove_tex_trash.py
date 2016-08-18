
# coding: utf8

def main():
    import csv
    import sys
    import os
    
    if os.path.exists(os.path.abspath('__spec.aux')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.aux')
        os.remove(path)
    if os.path.exists(os.path.abspath('__spec.log')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.log')
        os.remove(path)
    if os.path.exists(os.path.abspath('__spec.out')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.out')
        os.remove(path)
    if os.path.exists(os.path.abspath('__spec.synctex.gz')):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__spec.synctex.gz')
        os.remove(path)    
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output.log')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports.tex')
    os.remove(path)

if __name__ == '__main__':
    main()


