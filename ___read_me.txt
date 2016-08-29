1. установка ПО.
	1.1.OS WIN: 
	1.1.1. Установить ПО для компиляции tex файлов MikTex.
	1.2.2. Установить пакет eskdX.
	1.2.3. Установить Python27.
	1.1.OS LIN: 
	1.1.1. Установить ПО для компиляции tex файлов texlive +texmaker.
	sudo apt-get install texlive-full
	sudo apt-get install texmaker
	texmaker 
	1.2.2. Установить пакет eskdX.
	sudo apt-get install subversion
	svn co http://svn.eskdx.org.ua/trunk eskdx
	unzip eskdx-0.98.zip
	mkdir -p ~/texmf/tex/latex
	cp -a eskdx-0.98/unpacked ~/texmf/tex/latex/eskdx
	texhash
	1.2.3. Установить Python27.
	sudo apt-get install python2.7
	sudo apt-get install idle
2. Занесение данных (кодировка файлов cp1251).
	2.1.Документы, файл csv_doc
заполняются поля 
Form - формат документа
Oboz - обозначение документа
Name - наименование документа
	2.2.Комплексы, файл csv_compl
заполняются поля 
Oboz - обозначение документа
Name - наименование документа
Kol - количество
	2.3.Сборочные единицы, файл csv_sbed
заполняются поля
Form - формат документа
Poz - позиция (не заполняется)
Oboz - обозначение документа
Name - наименование документа
Kol - количество
	2.4.Детали, файл csv_det
заполняются поля
Form - формат документа
Poz - позиция (не заполняется)
Oboz - обозначение документа
Name - наименование документа
Kol - количество
	2.5.Стандартные изделия, файл csv_stiz
заполняются поля
Poz - позиция (не заполняется)
Name - наименование документа
Kol - количество
	2.6.Прочие изделия(бом), файл csv_priz_bom
Файл генерируется САПРом
поля
RefDes;Name;PartNumber;PartNumberRU;Value;TU GOST;PartDocument;Manufacturer;
Unplaced;Case;TCx;PowerRating;Voltage;ReplacementPN;SpecSection;BomNote
	2.7.Прочие изделия, файл csv_priz_poc
заполняются поля
Poz - позиция (не заполняется)
Name - наименование документа
Kol - количество
	2.8.Материалы, файл csv_mater
заполняются поля
Name - наименование документа
Kol - количество
Prim - примечания
	2.9.Комплекns, файл csv_complect
заполняются поля 
Oboz - обозначение документа
Name - наименование документа
Kol - количество

3. получение файла
	3.1. Для получения pdf запустить ___start_bat_sh.py два раза подряд. В момент запуска pdf-файлы должны быть закрыты.
	3.2. Для ведомости покупных изделий в случае, если количество листов превышает 3, взять файл регистрации изменений __reg_izm.pdf.