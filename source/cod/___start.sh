#!/bin/bash

ABSOLUTE_FILENAME=`readlink -e "$0"`
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`



cd $DIRECTORY

cp $DIRECTORY/russianb.ldf /usr/share/texlive/texmf-dist/tex/generic/babel-russian/russianb.ldf

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
python $DIRECTORY/remove_tex_trash.py
sleep 1
cd ..
cd ..
mv $DIRECTORY/_per.pdf _per.pdf
mv $DIRECTORY/__spec.pdf __spec.pdf
mv $DIRECTORY/__ved_poc.pdf __ved_poc.pdf
mv $DIRECTORY/__reg_izm.pdf __reg_izm.pdf
sleep 1
