import hashlib
import csv
f= open('output.txt','w')
c = csv.reader(open("output.csv", "rb"))
print f
print c
a = c
print a
for row in c:
    print row
f.write('bla')
a = hash(f)
f.close()
print(a)
f = open('output.txt','r')
print hashlib.md5(f.read()).hexdigest()
f.close()
b = 0.099999999999 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
print(b)
d = '\a'
print(d)

#############
ee = open("PCB_Project.xls", "rb")
e = csv.reader(ee)
print(e)
for rec in e:
    print rec
#e.write('bla')
