bom2pe.py
TIMEOUT /T 1 /NOBREAK
pdflatex _per.tex
TIMEOUT /T 1 /NOBREAK
::__spec.pdf
::pause 
remove_tex_trash.py
::ECHO OK!
