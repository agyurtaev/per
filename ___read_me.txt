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
	2.1.Документы, файл dokumenty
заполняются поля 
Form - формат документа
Oboz - обозначение документа
Name - наименование документа
Prim - примечание
	2.2.Комплексы, файл kompleksy
заполняются поля 
Oboz - обозначение документа
Name - наименование документа
Kol - количество
Prim - примечание
	2.3.Сборочные единицы, файл sborochnye_edinicy
заполняются поля
Form - формат документа
Poz - позиция (не заполняется)
Oboz - обозначение документа
Name - наименование документа
Kol - количество
Prim - примечание
	2.4.Детали, файл detali
заполняются поля
Form - формат документа
Poz - позиция (не заполняется)
Oboz - обозначение документа
Name - наименование документа
Kol - количество
Prim - примечание
	2.5.Стандартные изделия, файл standartnye_izdelija
заполняются поля
Poz - позиция (не заполняется)
Name - наименование документа
Kol - количество
Prim - примечание
	2.6.Прочие изделия(бом), файл prochie_izdelija_bom
Файл генерируется САПРом
поля
RefDes;Name;PartNumber;PartNumberRU;Value;TU GOST;PartDocument;Manufacturer;
Unplaced;Case;TCx;PowerRating;Voltage;ReplacementPN;SpecSection;BomNote;Tolerance
	2.7.Прочие изделия, файл prochie_izdelija_pokupnye
заполняются поля
Poz - позиция (не заполняется)
Name - наименование документа
Prim - примечание
Kol - количество
	2.8.Материалы, файл materialy
заполняются поля
Name - наименование документа
Kol - количество
Prim - примечания
	2.9.Комплекы, файл komplekty
заполняются поля 
Oboz - обозначение документа
Name - наименование документа
Kol - количество
Prim - примечание
3. получение файла
	3.1. Для получения pdf запустить ___start_bat_sh.py два раза подряд. В момент запуска pdf-файлы должны быть закрыты.
	3.2. Для ведомости покупных изделий в случае, если количество листов превышает 3, взять файл регистрации изменений __reg_izm.pdf.