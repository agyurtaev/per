
# coding: utf8


def main():
    import csv
    import sys
    import os
    import shutil 
    from shutil import copyfile

    def perecod(line):
        line = line.decode('cp1251').encode("utf-8")
        return line
    
    dr = os.path.dirname(__file__)
    o = os.name
    if o=='nt':
        pr = dr.rfind ('\\')
    else: 
        pr = dr.rfind ('/')
    dr = dr[0:pr]
    dr1 = dr + '/csv/'    
    dr2 = dr + '/template/'    
    ifile  = open(dr1+'dannye_dokumenta.csv', 'rb')
    reader  = csv.reader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    row_num = 0
    for row in reader:
        if row_num==0:
            header=row
        row_num+=1
    ifile.seek(0)
    readerd = csv.DictReader(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE )
    row_num = 0
    for row in readerd:
        if row_num==0:
            headerd=row
            if not (('title' in headerd) and ('docName' in headerd) and ('signature' in headerd)
                    and ('mass' in headerd) and ('scale' in headerd) and ('author' in headerd) and ('checker' in headerd)
                    and ('tcontr' in headerd) and ('ncontr' in headerd) and ('approvedBy' in headerd) and ('material' in headerd)
                    and ('letter1' in headerd) and ('letter2' in headerd) and ('letter3' in headerd)):
                print 'ERROR!!! \n'
                copyfile(dr2 + 'data_latex_templ.tex', os.path.dirname(__file__) + '__data_pe.tex')
                copyfile(dr2 + 'data_latex_templ.tex', os.path.dirname(__file__) + '__data_sp.tex')
                copyfile(dr2 + 'data_latex_templ.tex', os.path.dirname(__file__) + '__data_vp.tex')
                copyfile(dr2 + 'data_latex_templ.tex', os.path.dirname(__file__) + '__data_reg_izm.tex')
                ifile.close()

        row_num+=1
    ifile.close()
    
    ifile  = open(dr1+'dannye_dokumenta.csv', 'rb')
    readerd.__init__(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    ofile =open('__data_pe.tex', 'w')
    row_num = 0
    for row in readerd:
        if row_num >= 0:
            if row['title'] != '':
                ofile.write('\ESKDtitle{'+perecod(row['title'])+'}')
            else:
                ofile.write('\ESKDtitle{}')

            ofile.write('\ESKDdocName{перечень элементов}')
                            
            if row['signature'] != '':
                ofile.write('\ESKDsignature{'+perecod(row['signature'])+' ПЭ3 }')
            else:
                ofile.write('\ESKDsignature{}')

            if (row['letter1'] != '') or (row['letter2'] != '') or (row['letter3'] != ''):
                ofile.write('\ESKDletter{'+perecod(row['letter1'])+'}{'+perecod(row['letter2'])+'}{'+perecod(row['letter3'])+'}')
            else:
                ofile.write('\ESKDletter{}{}{}')
                            
            if row['material'] != '':
                ofile.write('\ESKDmaterial{'+perecod(row['material'])+'}')
            else:
                ofile.write('\ESKDmaterial{}')

            if row['mass'] != '':
                ofile.write('\ESKDmass{'+perecod(row['mass'])+'}')
            else:
                ofile.write('\ESKDmass{}')
                            
            if row['scale'] != '':
                ofile.write('\ESKDscale{'+perecod(row['scale'])+'}')
            else:
                ofile.write('\ESKDscale{}')

            if row['author'] != '':
                ofile.write('\ESKDauthor{'+perecod(row['author'])+'}')
            else:
                ofile.write('\ESKDauthor{}')  

            if row['checker'] != '':
                ofile.write('\ESKDchecker{'+perecod(row['checker'])+'}')
            else:
                ofile.write('\ESKDchecker{}')

            if row['tcontr'] != '':
                ofile.write('\ESKDcolumnXIfIII{'+perecod(row['tcontr'])+'}')
            else:
                ofile.write('\ESKDcolumnXIfIII{}')
                            
            if row['ncontr'] != '':
                ofile.write('\ESKDcolumnXIfV{'+perecod(row['ncontr'])+'}')
            else:
                ofile.write('\ESKDcolumnXIfV{}')

            if row['approvedBy'] != '':
                ofile.write('\ESKDapprovedBy{'+perecod(row['approvedBy'])+'}')
            else:
                ofile.write('\ESKDapprovedBy{}')
                            
        row_num+=1
    ifile.close()
    ofile.close()

    ifile  = open(dr1+'dannye_dokumenta.csv', 'rb')
    readerd.__init__(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    ofile =open('__data_sp.tex', 'w')
    row_num = 0
    for row in readerd:
        if row_num >= 0:
            if row['title'] != '':
                ofile.write('\ESKDtitle{'+perecod(row['title'])+'}')
            else:
                ofile.write('\ESKDtitle{}')

            ofile.write('\ESKDdocName{}')
                            
            if row['signature'] != '':
                ofile.write('\ESKDsignature{'+perecod(row['signature'])+'}')
            else:
                ofile.write('\ESKDsignature{}')

            if (row['letter1'] != '') or (row['letter2'] != '') or (row['letter3'] != ''):
                ofile.write('\ESKDletter{'+perecod(row['letter1'])+'}{'+perecod(row['letter2'])+'}{'+perecod(row['letter3'])+'}')
            else:
                ofile.write('\ESKDletter{}{}{}')
                            
            if row['material'] != '':
                ofile.write('\ESKDmaterial{'+perecod(row['material'])+'}')
            else:
                ofile.write('\ESKDmaterial{}')

            if row['mass'] != '':
                ofile.write('\ESKDmass{'+perecod(row['mass'])+'}')
            else:
                ofile.write('\ESKDmass{}')
                            
            if row['scale'] != '':
                ofile.write('\ESKDscale{'+perecod(row['scale'])+'}')
            else:
                ofile.write('\ESKDscale{}')

            if row['author'] != '':
                ofile.write('\ESKDauthor{'+perecod(row['author'])+'}')
            else:
                ofile.write('\ESKDauthor{}')  

            if row['checker'] != '':
                ofile.write('\ESKDchecker{'+perecod(row['checker'])+'}')
            else:
                ofile.write('\ESKDchecker{}')

            if row['tcontr'] != '':
                ofile.write('\ESKDcolumnXIfIII{'+perecod(row['tcontr'])+'}')
            else:
                ofile.write('\ESKDcolumnXIfIII{}')
                            
            if row['ncontr'] != '':
                ofile.write('\ESKDcolumnXIfV{'+perecod(row['ncontr'])+'}')
            else:
                ofile.write('\ESKDcolumnXIfV{}')

            if row['approvedBy'] != '':
                ofile.write('\ESKDapprovedBy{'+perecod(row['approvedBy'])+'}')
            else:
                ofile.write('\ESKDapprovedBy{}')
                            
                            
        row_num+=1
    ifile.close()
    ofile.close()

    ifile  = open(dr1+'dannye_dokumenta.csv', 'rb')
    readerd.__init__(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    ofile =open('__data_vp.tex', 'w')
    row_num = 0
    for row in readerd:
        if row_num >= 0:
            if row['title'] != '':
                ofile.write('\ESKDtitle{'+perecod(row['title'])+'}')
            else:
                ofile.write('\ESKDtitle{}')

            ofile.write('\ESKDdocName{ведомость покупных}')
                            
            if row['signature'] != '':
                ofile.write('\ESKDsignature{'+perecod(row['signature'])+' ВП }')
            else:
                ofile.write('\ESKDsignature{}')

            if (row['letter1'] != '') or (row['letter2'] != '') or (row['letter3'] != ''):
                ofile.write('\ESKDletter{'+perecod(row['letter1'])+'}{'+perecod(row['letter2'])+'}{'+perecod(row['letter3'])+'}')
            else:
                ofile.write('\ESKDletter{}{}{}')
                            
            if row['material'] != '':
                ofile.write('\ESKDmaterial{'+perecod(row['material'])+'}')
            else:
                ofile.write('\ESKDmaterial{}')

            if row['mass'] != '':
                ofile.write('\ESKDmass{'+perecod(row['mass'])+'}')
            else:
                ofile.write('\ESKDmass{}')
                            
            if row['scale'] != '':
                ofile.write('\ESKDscale{'+perecod(row['scale'])+'}')
            else:
                ofile.write('\ESKDscale{}')

            if row['author'] != '':
                ofile.write('\ESKDauthor{'+perecod(row['author'])+'}')
            else:
                ofile.write('\ESKDauthor{}')  

            if row['checker'] != '':
                ofile.write('\ESKDchecker{'+perecod(row['checker'])+'}')
            else:
                ofile.write('\ESKDchecker{}')

            if row['tcontr'] != '':
                ofile.write('\ESKDcolumnXIfIII{'+perecod(row['tcontr'])+'}')
            else:
                ofile.write('\ESKDcolumnXIfIII{}')
                            
            if row['ncontr'] != '':
                ofile.write('\ESKDcolumnXIfV{'+perecod(row['ncontr'])+'}')
            else:
                ofile.write('\ESKDcolumnXIfV{}')

            if row['approvedBy'] != '':
                ofile.write('\ESKDapprovedBy{'+perecod(row['approvedBy'])+'}')
            else:
                ofile.write('\ESKDapprovedBy{}')
                            
                            
        row_num+=1
    ifile.close()
    ofile.close()

    ifile  = open(dr1+'dannye_dokumenta.csv', 'rb')
    readerd.__init__(ifile, delimiter=';', doublequote=False, quoting=csv.QUOTE_NONE)
    ofile =open('__data_reg_izm.tex', 'w')
    row_num = 0
    for row in readerd:
        if row_num >= 0:
            if row['title'] != '':
                ofile.write('\ESKDtitle{'+perecod(row['title'])+'}')
            else:
                ofile.write('\ESKDtitle{}')

            ofile.write('\ESKDdocName{ведомость покупных}')
                            
            if row['signature'] != '':
                ofile.write('\ESKDsignature{'+perecod(row['signature'])+' ВП }')
            else:
                ofile.write('\ESKDsignature{}')

            if (row['letter1'] != '') or (row['letter2'] != '') or (row['letter3'] != ''):
                ofile.write('\ESKDletter{'+perecod(row['letter1'])+'}{'+perecod(row['letter2'])+'}{'+perecod(row['letter3'])+'}')
            else:
                ofile.write('\ESKDletter{}{}{}')
                            
            if row['material'] != '':
                ofile.write('\ESKDmaterial{'+perecod(row['material'])+'}')
            else:
                ofile.write('\ESKDmaterial{}')

            if row['mass'] != '':
                ofile.write('\ESKDmass{'+perecod(row['mass'])+'}')
            else:
                ofile.write('\ESKDmass{}')
                            
            if row['scale'] != '':
                ofile.write('\ESKDscale{'+perecod(row['scale'])+'}')
            else:
                ofile.write('\ESKDscale{}')

            if row['author'] != '':
                ofile.write('\ESKDauthor{'+perecod(row['author'])+'}')
            else:
                ofile.write('\ESKDauthor{}')  

            if row['checker'] != '':
                ofile.write('\ESKDchecker{'+perecod(row['checker'])+'}')
            else:
                ofile.write('\ESKDchecker{}')

            if row['tcontr'] != '':
                ofile.write('\ESKDcolumnXIfIII{'+perecod(row['tcontr'])+'}')
            else:
                ofile.write('\ESKDcolumnXIfIII{}')
                            
            if row['ncontr'] != '':
                ofile.write('\ESKDcolumnXIfV{'+perecod(row['ncontr'])+'}')
            else:
                ofile.write('\ESKDcolumnXIfV{}')

            if row['approvedBy'] != '':
                ofile.write('\ESKDapprovedBy{'+perecod(row['approvedBy'])+'}')
            else:
                ofile.write('\ESKDapprovedBy{}')
        row_num+=1
    ifile.close()
    ofile.close()                            
if __name__ == '__main__':
    main()


