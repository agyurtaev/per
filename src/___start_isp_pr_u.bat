Set CURRENTDIR=%CD%
cd ..
Set RODDIR=%CD%
cd %CURRENTDIR%
check_csv.py
TIMEOUT /T 1 /NOBREAK
bom2sp.py
copy reports.tex reports_sp_ob.tex 
TIMEOUT /T 1 /NOBREAK
_bom2pe_sort.py
copy reports.tex reports_pe_ob.tex
TIMEOUT /T 1 /NOBREAK
data_latex_gen.py




