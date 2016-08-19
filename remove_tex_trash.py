
# coding: utf8

def main():
    import csv
    import sys
    import os
    
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
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output.log')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports.tex')
    os.remove(path)

if __name__ == '__main__':
    main()


