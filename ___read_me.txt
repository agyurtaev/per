1. ��������� ��.
	1.1.OS WIN: 
	1.1.1. ���������� �� ��� ���������� tex ������ MikTex.
	1.2.2. ���������� ����� eskdX.
	1.2.3. ���������� Python27.
	1.1.OS LIN: 
	1.1.1. ���������� �� ��� ���������� tex ������ texlive +texmaker.
	sudo apt-get install texlive-full
	sudo apt-get install texmaker
	texmaker 
	1.2.2. ���������� ����� eskdX.
	sudo apt-get install subversion
	svn co http://svn.eskdx.org.ua/trunk eskdx
	unzip eskdx-0.98.zip
	mkdir -p ~/texmf/tex/latex
	cp -a eskdx-0.98/unpacked ~/texmf/tex/latex/eskdx
	texhash
	1.2.3. ���������� Python27.
	sudo apt-get install python2.7
	sudo apt-get install idle
2. ��������� ������ (��������� ������ cp1251).
	2.1.���������, ���� csv_doc
����������� ���� 
Form - ������ ���������
Oboz - ����������� ���������
Name - ������������ ���������
	2.2.���������, ���� csv_compl
����������� ���� 
Oboz - ����������� ���������
Name - ������������ ���������
Kol - ����������
	2.3.��������� �������, ���� csv_sbed
����������� ����
Form - ������ ���������
Poz - ������� (�� �����������)
Oboz - ����������� ���������
Name - ������������ ���������
Kol - ����������
	2.4.������, ���� csv_det
����������� ����
Form - ������ ���������
Poz - ������� (�� �����������)
Oboz - ����������� ���������
Name - ������������ ���������
Kol - ����������
	2.5.����������� �������, ���� csv_stiz
����������� ����
Poz - ������� (�� �����������)
Name - ������������ ���������
Kol - ����������
	2.6.������ �������(���), ���� csv_priz_bom
���� ������������ ������
����
RefDes;Name;PartNumber;PartNumberRU;Value;TU GOST;PartDocument;Manufacturer;
Unplaced;Case;TCx;PowerRating;Voltage;ReplacementPN;SpecSection;BomNote
	2.7.������ �������, ���� csv_priz_poc
����������� ����
Poz - ������� (�� �����������)
Name - ������������ ���������
Kol - ����������
	2.8.���������, ���� csv_mater
����������� ����
Name - ������������ ���������
Kol - ����������
Prim - ����������
	2.9.�������ns, ���� csv_complect
����������� ���� 
Oboz - ����������� ���������
Name - ������������ ���������
Kol - ����������

3. ��������� �����
	3.1. ��� ��������� pdf ��������� ___start_bat_sh.py ��� ���� ������. � ������ ������� pdf-����� ������ ���� �������.
	3.2. ��� ��������� �������� ������� � ������, ���� ���������� ������ ��������� 3, ����� ���� ����������� ��������� __reg_izm.pdf.