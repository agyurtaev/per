Set CURRENTDIR=%CD%
cd ..
Set RODDIR=%CD%
cd %CURRENTDIR%
TIMEOUT /T 1 /NOBREAK
bom2sp_isp.py
copy reports.tex reports_sp.tex 
TIMEOUT /T 1 /NOBREAK
_bom2pe_sort.py
copy reports.tex reports_pe.tex




