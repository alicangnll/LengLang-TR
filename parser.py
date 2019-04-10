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

