
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
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output.log')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports.tex')
    os.remove(path)

if __name__ == '__main__':
    main()


