#!/bin/bash

ABSOLUTE_FILENAME=`readlink -e "$0"`
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`

cd $DIRECTORY
sleep 1
cp $DIRECTORY/reports_sp_ob.tex $DIRECTORY/reports.tex
sleep 1
pdflatex $DIRECTORY/__spec.tex
sleep 1
cp $DIRECTORY/reports_pe_ob.tex $DIRECTORY/reports.tex
sleep 1
pdflatex $DIRECTORY/_per.tex
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
mv $DIRECTORY/case_sort.pdf ./output/case_sort.pdf
sleep 1
cd $DIRECTORY
python $DIRECTORY/rename_pdf.py
sleep 1
