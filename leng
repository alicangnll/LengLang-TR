# -*- coding: utf-8 -*-
# LengLang v0.1
# Yazar : Ali Can GÖNÜLLÜ
import os
import time
from sys import *
from openfile import *
from leng import *
from ayirici import ayirici

semboller = {}
def calis_shell():
try:
print("LengLang v0.1 \n")
while True:
veri = raw_input("<?>: ") + "\n<EOF>"
open(".shell_veri","w").write(veri)
tokenler = leng(veri)
ayirici(tokenler,0)
except:
print("\n")
exit()

def calis_dosya():
veri = openfile(argv[1])
tokenler = leng(veri)
ayirici(tokenler,0)

if len(argv) == 2:
calis_dosya()
elif len(argv) ==1:
calis_shell()
else:
print("ERROR : ASIRI YUKLEME")