# -*- coding: utf-8 -*-
def dosya_ac(dosyaac)
veri = open(dosyaac, 'r').read()
veri += '<EOF>'
return veri