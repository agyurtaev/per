Set CURRENTDIR=%CD%
cd %CURRENTDIR%\src\
check_csv.py
TIMEOUT /T 1 /NOBREAK
data_latex_gen.py
TIMEOUT /T 1 /NOBREAK
bom2sp.py
TIMEOUT /T 1 /NOBREAK
pdflatex __spec.tex -output-directory=%CURRENTDIR%\output\ -aux-directory=%CURRENTDIR%\src\
TIMEOUT /T 1 /NOBREAK
_bom2pe_sort.py
TIMEOUT /T 1 /NOBREAK
pdflatex _per.tex -output-directory=%CURRENTDIR%\output\ -aux-directory=%CURRENTDIR%\src\
TIMEOUT /T 1 /NOBREAK
bom2vp.py
TIMEOUT /T 1 /NOBREAK
pdflatex __ved_poc.tex -output-directory=%CURRENTDIR%\output\ -aux-directory=%CURRENTDIR%\src\
TIMEOUT /T 1 /NOBREAK
pdflatex __reg_izm.tex -output-directory=%CURRENTDIR%\output\ -aux-directory=%CURRENTDIR%\src\
TIMEOUT /T 1 /NOBREAK
case_sort.py
TIMEOUT /T 1 /NOBREAK
pdflatex case_sort.tex -output-directory=%CURRENTDIR%\output\ -aux-directory=%CURRENTDIR%\src\
TIMEOUT /T 1 /NOBREAK
remove_tex_trash.py
TIMEOUT /T 1 /NOBREAK
rename_pdf.py
