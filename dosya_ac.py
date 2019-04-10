# -*- coding: utf-8 -*-
def dosya_ac(filename):
veri = open(filename, 'r').read()
veri += '<EOF>'
return veri