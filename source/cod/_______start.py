
def main():
    import csv
    import sys
    import os 
    import subprocess
    import time

    put = os.getcwd()
    
    proc ='/_bom2pe_sort.py'
    os.system(proc)
    time.sleep(1)

    proc = 'pdflatex _per.tex -output-directory='+put+' -aux-directory='+put+'\source\cod'        
    #os.system('cd '+put+'\n'+proc)
    os.system(proc)
    time.sleep(1)    

    #proc ='\source\cod\bom2sp.py'
    #os.system(proc)
    #time.sleep(1)
    
    #proc = 'pdflatex __spec.tex -output-directory='+put+' -aux-directory='+put+'\source\cod'        
    #os.system(proc)
    #time.sleep(1)
    
    #proc ='\source\cod\bom2vp.py'
    #os.system(proc)
    #time.sleep(1)
    
    #proc = 'pdflatex __ved_poc.tex -output-directory='+put+' -aux-directory='+put+'\source\cod'        
    #os.system(proc)
    #time.sleep(1)
    
    #proc = 'pdflatex __reg_izm.tex -output-directory='+put+' -aux-directory='+put+'\source\cod'        
    #os.system(proc)
    #time.sleep(1)
    
    proc ='remove_tex_trash.py'
    os.system(proc)
    time.sleep(1)
    
if __name__ == '__main__':
    main()


