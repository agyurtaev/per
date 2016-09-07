#!/bin/bash

ABSOLUTE_FILENAME=`readlink -e "$0"`
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`

cd $DIRECTORY

cp $DIRECTORY/russianb.ldf /usr/share/texlive/texmf-dist/tex/generic/babel-russian/russianb.ldf

python $DIRECTORY/_ispolnenija_start.py
sleep 1

