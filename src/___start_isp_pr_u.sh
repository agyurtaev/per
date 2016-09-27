#!/bin/bash

ABSOLUTE_FILENAME=`readlink -e "$0"`
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`

cd $DIRECTORY

python $DIRECTORY/check_csv.py
sleep 1
python $DIRECTORY/bom2sp.py
sleep 1
cp  $DIRECTORY/reports.tex  $DIRECTORY/reports_sp_ob.tex 
sleep 1
python $DIRECTORY/_bom2pe_sort.py
sleep 1
cp  $DIRECTORY/reports.tex  $DIRECTORY/reports_pe_ob.tex
sleep 1
python $DIRECTORY/data_latex_gen.py
sleep 1
