# -*- coding: utf-8 -*-
semboller = {}

def DEGISKENAL(varadi, semboller):
if varadi in semboller:
return semboller[varadi]

def YERLESTIR(varadi, vardegeri):
global semboller
semboller[varadi[4:]] = vardegeri

# Asıl Kod Baslangici

def ayirici(tokenler,deger):
try:
while deger < len(tokenler):

if tokenler[deger] == 'EGER':
if tokenler[deger + 2] == 'ESIT':
if tokenler[deger + 1][0:4] == "OPERATOR":
tokenler[deger + 1] = "SAYI:" + str(eval(tokenler[deger + 1][5:]))

if tokenler[deger + 3][0:4] == "OPERATOR":
tokenler[deger + 3] = "SAYI:" + str(eval(tokenler[deger + 3][5:]))
if tokenler[deger + 1][0:4] == "DEGER:":
tokenler[deger + 1] = DEGISKENAL(tokenler[deger + 1][4:],semboller)
if tokenler[deger + 3][0:4] == "DEGER:":
tokenler[deger + 3] = DEGISKENAL(tokenler[deger + 3][4:],semboller)
if tokenler[deger + 1] == tokenler[deger + 3]:
deger += 5
a = deger
while tokenler[a] != 'YAP':
a += 1
while tokenler[tokenler] != 'YAP' and deger < len(tokenler):
parser(tokenler[0:a+deger],deger)
deger += 1
else:
while tokenler[deger] != 'YAP':
deger += 1
# EGER ve ESIT degerleri tanımlandi
elif tokenler[deger] == 'BOYLEYKEN':
_deger = 0
if tokenler[deger - 2] == 'ESIT':
if tokenler[deger - 1][0:4] == "OPERATOR":
tokenler[deger - 1] = "SAYI:" + str(eval(tokenler[deger - 1][5:]))
if tokenler[deger - 3][0:4] == "OPERATOR":
tokenler[deger - 3] = "SAYI:" + str(eval(tokenler[deger - 3][5:]))
if tokenler[deger - 1][0:4] == "DEGER:":
# Part 2
pram_a_is_var = True
pram_a_name = tokenler[deger - 1][4:]
tokenler[deger - 1] = DEGISKENAL(tokenler[deger - 1][4:],semboller)
if tokenler[deger - 3][0:4] == "DEGER:":
pram_b_is_var = True
pram_b_name = tokenler[deger - 3][4:]
tokenler[deger - 3] = DEGISKENAL(tokenler[deger - 3][4:],semboller)
if tokenler[deger - 1] == tokenler[deger - 3]:
deger += 1
a = deger
while tokenler[a] != 'TEKRAR':
a += 1
while tokenler[deger] != 'TEKRAR' and tokenler < len(tokenler) and DEGISKENAL(pram_a_name,semboller) == DEGISKENAL(pram_b_name,semboller):
parser(tokenler[0:a+deger],deger)
else:
while tokenler[deger] != 'TEKRAR':
deger += 1

#BOYLEYKEN degeri tanimlandi
elif tokenler[deger] == 'YAZ':
veri = tokenler[deger + 1]
if veri[0] == '"':
veri = veri.replace('"', '')
elif veri[0:4] == 'SAYI':
veri = veri[5:]
elif veri[0:4] == 'OPERATOR':
veri = veri[5:]
veri = eval(veri)
elif veri[0:3] == 'DEGER':
veri = DEGISKENAL(veri[4:], semboller)
print veri
deger += 2
#YAZ - Part 2 Baslangici
elif tokenler[deger][0:4] == 'DEGER:' and tokenler[deger + 1] == 'ESITTIR':
if tokenler[deger + 2][0] == '"':
veri = tokenler[deger + 2].replace('"', '')
YERLESTIR(tokenler[deger], veri)
elif tokenler[deger + 2][0:4] == 'SAYI':
veri = tokenler[deger + 2][5:]
YERLESTIR(tokenler[deger], veri)
elif tokenler[deger + 2][0:4] == 'OPERATOR':
veri = tokenler[deger + 2][5:]
veri = eval(veri)
YERLESTIR(tokenler[deger], veri)
elif tokenler[deger + 2][0:4] == 'DEGER:':
YERLESTIR(tokenler[deger], DEGISKENAL(tokenler[deger + 2][4:], semboller))
elif tokenler[deger + 2] == 'GIRDI':
veri = raw_input(tokenler[deger + 3].replace('"', ''))
YERLESTIR(tokenler[deger], veri)
deger += 3
#YAZ verisi bitisi

elif tokenler[deger] == "CIKIS":
exit()

# CIKIS girdisi tanımlandı

elif tokenler[deger] == 'YUVARLA':
if tokenler[deger + 2][0:4] == 'OPERATOR':
veri = eval(tokenler[deger + 2][5:])
YERLESTIR(tokenler[deger + 1],str(float(input(veri))))
deger += 3

#YUVARLA girdisi tanımlandı

elif tokenler[deger] == 'EKLE':
if tokenler[deger + 2][0:4] == 'OPERATOR':
veri = eval(tokenler[deger + 2][5:])
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data + veri))
deger += 3

# EKLE girdisi tanımlandı
elif tokenler[deger + 2] [0:4] == 'SAYI':
veri = int(tokenler[deger + 2][5:])
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data + veri))
deger += 3
# SAYI girdisi tanımlandı
elif  tokenler[deger + 2][0:4] == 'DEGER:':
veri =  int(DEGISKENAL(tokenler[deger + 2][4:],semboller))
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data + veri))
deger += 3
else:
deger += 3
# DEGER girdisi tanımlandı
elif tokenler[deger] == 'CARP':
if tokenler[deger + 2][0:4] == 'OPERATOR':
veri = eval(tokenler[deger + 2][5:])
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data * veri))
deger += 3
# CARP girdisi tanımlandı
elif tokenler[deger + 2][0:4] == 'SAYI':
veri = int(tokenler[deger + 2][5:])
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data * veri))
deger += 3
# SAYI 2.Tanımlama
elif tokenler[deger] == 'BOLME':
if tokenler[deger + 2][0:4] == 'OPERATOR':
veri = eval(tokenler[deger + 2][5:])
var_data = int(DEGİSKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data / dava))
deger += 3
elif tokenler[deger + 2][0:4] == 'SAYI':
veri = int(tokenler[deger + 2][5:])
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data / veri))
deger += 3
elif  tokenler[deger + 2][0:4] == 'DEGER:':
veri =  int(DEGISKENAL(tokenler[deger + 2][4:],semboller))
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data / veri))
deger += 3
else:
deger += 3
# BOLME girdisi tanımlandı
eif tokenler[deger] == 'CIKAR':
if tokenler[deger + 2][0:4] == 'OPERATOR':
veri = eval(tokenler[deger + 2][5:])
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data - veri)
deger += 3
# CIKAR girdisi tanımlandı
elif tokenler[deger + 2][0:4] == 'SAYI':
data = int(tokenler[deger + 2][5:])
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data - data))
deger += 3
# SAYI girdisi tanımlandı
elif  tokenler[deger + 2][0:4] == 'DEGER:':
data =  int(DEGISKENAL(tokenler[deger + 2][4:],semboller))
var_data = int(DEGISKENAL(tokenler[deger + 1][4:],semboller))
YERLESTIR(tokenler[deger + 1],str(var_data - data))
deger += 3
else:
deger += 1
