Set CURRENTDIR=%CD%
cd %CURRENTDIR%\source\cod
bom2sp.py
TIMEOUT /T 1 /NOBREAK
pdflatex __spec.tex -output-directory=%CURRENTDIR% -aux-directory=%CURRENTDIR%\source\cod
TIMEOUT /T 1 /NOBREAK
_bom2pe_sort.py
TIMEOUT /T 1 /NOBREAK
pdflatex _per.tex -output-directory=%CURRENTDIR% -aux-directory=%CURRENTDIR%\source\cod
TIMEOUT /T 1 /NOBREAK
bom2vp.py
TIMEOUT /T 1 /NOBREAK
pdflatex __ved_poc.tex -output-directory=%CURRENTDIR% -aux-directory=%CURRENTDIR%\source\cod
TIMEOUT /T 1 /NOBREAK
pdflatex __reg_izm.tex -output-directory=%CURRENTDIR% -aux-directory=%CURRENTDIR%\source\cod
TIMEOUT /T 1 /NOBREAK
::__spec.pdf
::pause
remove_tex_trash.py
::ECHO OK!
