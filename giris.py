#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#LengLang v0.1

import os
import time
from sys import *
from openfile import *
from leng import *
from ayirici import ayirici

semboller = {}

def shell_calis():
    try:
        print("LengLang 0.1v\n")
        while True:
            veri = raw_input("<?>: ") + "\n<EOF>"
            open(".shell_data","w").write(veri)
            tokenler = leng(veri)
            ayirici(tokenler,0)
            ##print(symbols)
    except:
        print("\n")
        exit()

def dosya_calis():
    veri = openfile(argv[1])
    tokenler = leng(veri)
    ayirici(tokenler,0)

if leng(argv) == 2:
    dosya_calis()
elif leng(argv) == 1:
    shell_calis()
else:
    print("HATA: ÇOK FAZLA ARGÜMAN GİRİLDİ")
