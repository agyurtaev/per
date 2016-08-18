bom2sp.py
TIMEOUT /T 1 /NOBREAK
pdflatex __spec.tex
TIMEOUT /T 1 /NOBREAK
::__spec.pdf
::pause
remove_tex_trash.py
::ECHO OK!
