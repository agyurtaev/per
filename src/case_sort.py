# coding: utf8

def main():
    import csv
    import sys
    import os
    
    BOM_EMPTY_ITEM= " "
     
    ifile  = open('reports_info_case.tex', "rb")
    ofile  = open('reports_info_case1.tex', "wb")
    row_num=0
    row1 = ''
    row2 = ''
    refbuf = ''
    pr1 = 0
    pr2 = 0
    for row in ifile:
        st1 = ''
        st2 = ''
        if row_num==0:
            row1 = row
            pr1 = row1.rfind('&')
            st1 = row1[pr1:]
            refbuf = row1[:pr1]
        else:
            row2 = row
            pr1 = row1.rfind('&')
            pr2 = row2.rfind('&')
            st1 = row1[pr1:]
            st2 = row2[pr1:]
            if st1==st2:                                  
                refbuf = refbuf + ', ' + row2[:pr2]
            else:
                ofile.write(refbuf+row1[pr1:])
                row1 = row2
                refbuf = row2[:pr2]
        row_num+=1
    ofile.write(refbuf+row2[pr2:])
    ifile.close()
    ofile.close()

    row_num_u = 0
    ifile  = open('reports_info_case1.tex', "rb")
    ifilea =open('reports_info_case2.tex', "wb")
    for row in ifile:
        ifilea.write(row)
        row_num_u+=1
    ifile.close()
    ifilea.close() 
    ifile  = open('reports_info_case1.tex', "rb")
    ifilea  = open('reports_info_case2.tex', "rb")          
    ofile  = open('reports_info_case3.tex', "wb")
    row_num=0
    row1 = ''
    row2 = ''
    refbuf = ''
    pr = 1
    st1 = ''
    st2 = ''
    priz2 = 0
    for row in ifile:
        row_num_a = 0
        if row_num==0:
            row1 = row
            pr1 = row1.rfind('&')
            st1 = row1[pr1:] 
            refbuf = row1[:pr1-1]
        else:
            for rowa in ifilea:
                if row_num_a==0:                    
                    row2 = rowa
                    pr2 = row2.rfind('&')
                    st2 = row2[pr2:]
                else:
                    row2 = rowa
                    pr2 = row2.rfind('&')
                    st2 = row2[pr2:]
                    if row_num_a+1 < row_num:
                        if st2 == st1:
                            pr = 0    
                    if row_num_a > row_num:
                        if st2 == st1:
                            refbuf = refbuf + ', ' + row2[:pr2]
                            if row_num_a == row_num_u-1:
                                priz2 = 1
                                
                row_num_a+=1
            if pr == 1:       
                ofile.write(refbuf+row1[pr1:])
            pr = 1
        row1 = row
        pr1 = row1.rfind('&')
        st1 = row1[pr1:]
        refbuf = row1[:pr1]        
        row_num+=1 
        pr = 1
        ifilea.seek(0)
    if priz2 == 0:
        ofile.write(refbuf+row1[pr1:])
    ifile.close()
    ifilea.close()
    ofile.close()
    
    ifile  = open('reports_info_case3.tex', "rb")
    ofile =open('reports_info_case.tex', "wb")  
    for row in ifile:
        ofile.write(row)
        ofile.write('\hline')
    ofile.close()        
    ifile.close()
    
    
if __name__ == '__main__':
    main()
