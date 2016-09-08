#!/bin/bash

ABSOLUTE_FILENAME=`readlink -e "$0"`
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`

cd $DIRECTORY

python $DIRECTORY/check_csv.py
sleep 1
python $DIRECTORY/data_latex_gen.py
sleep 1
python $DIRECTORY/_bom2pe_sort.py
sleep 1
pdflatex $DIRECTORY/_per.tex
sleep 1
python $DIRECTORY/bom2sp.py
sleep 1
pdflatex $DIRECTORY/__spec.tex
sleep 1
python $DIRECTORY/bom2vp.py
sleep 1
pdflatex $DIRECTORY/__ved_poc.tex
sleep 1
pdflatex $DIRECTORY/__reg_izm.tex
sleep 1
python $DIRECTORY/case_sort.py
sleep 1
pdflatex $DIRECTORY/case_sort.tex
sleep 1
python $DIRECTORY/remove_tex_trash.py
sleep 1
cd ..
mv $DIRECTORY/_per.pdf ./output/_per.pdf
mv $DIRECTORY/__spec.pdf ./output/__spec.pdf
mv $DIRECTORY/__ved_poc.pdf ./output/__ved_poc.pdf
mv $DIRECTORY/__reg_izm.pdf ./output/__reg_izm.pdf
mv $DIRECTORY/case_sort.pdf ./output/case_sort.pdf
sleep 1
cd $DIRECTORY
python $DIRECTORY/rename_pdf.py
sleep 1
