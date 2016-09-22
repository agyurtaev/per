Set CURRENTDIR=%CD%
cd ..
Set RODDIR=%CD%
cd %CURRENTDIR%
copy reports_sp.tex reports.tex
pdflatex __spec.tex -output-directory=%RODDIR%\output\ -aux-directory=%CURRENTDIR%
TIMEOUT /T 1 /NOBREAK
copy reports_pe.tex reports.tex
pdflatex _per.tex -output-directory=%RODDIR%\output\ -aux-directory=%CURRENTDIR%
TIMEOUT /T 1 /NOBREAK
case_sort.py
TIMEOUT /T 1 /NOBREAK
pdflatex case_sort.tex -output-directory=%RODDIR%\output\ -aux-directory=%CURRENTDIR%
TIMEOUT /T 1 /NOBREAK
remove_tex_trash.py
TIMEOUT /T 1 /NOBREAK
rename_pdf.py


