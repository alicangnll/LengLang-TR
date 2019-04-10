# -*- coding: utf-8 -*-
# LengLang - Python-based Turkish Experimental Language
semboller = {}

def DEGISKENAL(varname, semboller):
if varname in semboller:
return semboller[varname]

def YERLESTIR(varname, varvalue):
global semboller
semboller[varname[4:]] = varvalue

def parser(tokenler,i):
try:
while i < len(tokenler):
if tokenler[i] == 'EGER':
if tokenler[i + 2] == 'ESIT':
if tokenler[i + 1][0:4] == "OPERATION":
tokenler[i + 1] = "SAYI:" + str(eval(tokenler[i + 1][5:]))
if tokenler[i + 3][0:4] == "OPERATION":
tokenler[i + 3] = "SAYI:" + str(eval(tokenler[i + 3][5:]))
if tokenler[i + 1][0:4] == "DEGER:":
tokenler[i + 1] = DEGISKENAL(tokenler[i + 1][4:],semboller)
if tokenler[i + 3][0:4] == "DEGER:":
tokenler[i + 3] = DEGISKENAL(tokenler[i + 3][4:],semboller)
if tokenler[i + 1] == tokenler[i + 3]:
i += 5
a = i
while tokenler[a] != 'YAP':
a += 1
while tokenler[i] != 'YAP' and i < len(tokenler):
parser(tokenler[0:a+i],i)
i += 1
else:
while tokenler[i] != 'YAP':
i += 1

elif tokenler[i] == 'IKEN':
_i = 0
if tokenler[i - 2] == 'ESES':
if tokenler[i - 1][0:4] == "OPER":
tokenler[i - 1] = "SAYI:" + str(eval(tokenler[i - 1][5:]))
if tokenler[i - 3][0:4] == "OPER":
tokenler[i - 3] = "SAYI:" + str(eval(tokenler[i - 3][5:]))
if tokenler[i - 1][0:4] == "DEG:":
pram_a_is_var = True
pram_a_name = tokenler[i - 1][4:]
tokenler[i - 1] = DEGISKENAL(tokenler[i - 1][4:],semboller)
if tokenler[i - 3][0:4] == "DEG:":
pram_b_is_var = True
pram_b_name = tokenler[i - 3][4:]
tokenler[i - 3] = DEGISKENAL(tokenler[i - 3][4:],semboller)
if tokenler[i - 1] == tokenler[i - 3]:
i += 1
a = i
while tokenler[a] != 'TEKRARLA':
a += 1
while tokenler[i] != 'TEKRARLA' and i < len(tokenler) and DEGISKENAL(pram_a_name,semboller) == DEGISKENAL(pram_b_name,semboller):
parser(tokenler[0:a+i],i)
else:
while tokenler[i] != 'TEKRARLA':
i += 1

elif tokstoks[i] == 'YAZDIR':
veri = tokenler[i + 1]
if veri[0] == '"':
veri = veri.replace('"', '')
elif veri[0:4] == 'SAYI':
veri = veri[5:]
elif veri[0:4] == 'OPER':
veri = veri[5:]
veri = eval(veri)
elif veri[0:3] == 'DEG':
veri = DEGISKENAL(veri[4:], semboller)
print veri
i += 2

elif tokenler[i][0:4] == 'DEG:' and tokenler[i + 1] == 'ESITTIR':
if tokenler[i + 2][0] == '"':
veri = tokenler[i + 2].replace('"', '')
YERLESTIR(tokenler[i], veri)
elif tokenler[i + 2][0:4] == 'SAYI':
veri = tokenler[i + 2][5:]
YERLESTIR(tokenler[i], veri)


