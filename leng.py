# -*- coding: utf-8 -*-
# Leng-Lang v0.1
def leng(filecontents):
tk = ''
tokenler = []
var = ''
varbasladi = 0
bolge = False
string = ''
express = ''
isexpress = 0
n = ''
filecontents = list(filecontents)
for char in filecontents:
#print (tk)
tk += char
if tk == '':
if bolge == False:
tk = ''
# else if girisleri
elif bolge == True:
tk = ""
# if girisi
if express != '' and isexpress == 1:
tokenler.append('OPERATOR:' + express)
express = ''
tk = ''
# else if devam
elif express != '' and isexpress == 0:
tokenler.append('SAYI:' + express)
express = ''
tk = ''
elif var != '':
tokenler.append('DEGER:' + var)
var = ''
varbasladi = 0
tk = ''
# else if tokenler
elif tk == '\n' or tk == '<EOF>':
if express != '' and isexpress == 1:
tokenler.append('OPERATOR:' + express)
express = ''

elif express != '' and isexpress == 0:
tokenler.append('SAYI:' + express)
express = ''

elif var != '':
tokenler.append('DEGER:' + var)
var = ''
varbasladi = 0
tk = ''

elif tk == '=' and bolge == False:
if express != '' and isexpress == 0:
tokenler.append('SAYI:' + express)
express = ''

if var != '':
tokenler.append('DEGER:' + var)
var = ''
varbasladi = 0

if tokenler[-1] == 'ESITTIR':
tokenler[-1] = 'ESIT'
# Komut Diger Kısmı
else:
tokenler.append('ESITTIR')
tk = ''

elif tk == '&' or tk == '[value]' and bolge == False:
varbasladi = 1
var += tk
tk = ''

elif varbasladi == 1:
if tk != '+' or tk == '-' or tk == '*' or tk == '/' or tk == '%':
var += tk
tk = ''
else:
varbasladi = 0
tk = ''
# Komutlar Dizisi Baslıyor
elif tk == 'YAZ' or tk == 'yaz':
            tokenler.append('YAZ')
            tk = ''
        elif tk == 'EKLE' or tk == 'ekle':
            tokenler.append('EKLE')
            tk = ''
        elif tk == 'ÇARPMA' or tk == 'çarpma':
            tokenler.append('CARPMA')
            tk = ''
        elif tk == 'BÖLME' or tk == 'bölme':
            tokenler.append('BOLME')
            tk = ''
        elif tk == 'ÇIKARMA' or tk == 'çıkarma':
            tokenler.append('CIKARMA')
            tk = ''
        elif tk == 'BÖYLEYKEN' or tk == 'böyleyken':
            tokenler.append('BOYLEYKEN')
            tk = ''
        elif tk == 'TEKRAR' or tk == 'tekrar':
            tokenler.append('TEKRAR')
            tk = ''
        elif tk == 'ÇIKIŞ' or tk == "çıkış":
            tokenler.append("CIKIS")
            tk = ""
        elif tk == 'YAP' or tk == 'yap':
            tokenler.append('YAP')
            tk = ''
			elif tk == 'YUVARLA' or tk == 'yuvarla':
            tokenler.append('YUVARLA')
            tk = ''
        elif tk == 'EĞER' or tk == 'eğer':
            tokenler.append('EGER')
            tk = ''
        elif tk == 'İSE' or tk == 'ise':
		if express != '' and isexpress == 0:
		tokenler.append('SAYI:' + express)
		express = ''
		tokenler.append('ISE')
		tk = ''
		# Komut Düzeltmeleri Yapılıyor...
		elif tk == 'GİRİS' or tk == 'giriş' or tk == 'giris' or tk == 'gir'
		tokenler.append('GIRIS')
		tk = ''
		# Giris Komutu Düzenlendi
		 elif tk == '0' or tk == '1' or tk == '2' or tk == '3' or tk == '4' or tk == '5' or tk == '6' or tk == '7' or tk == '8' or tk == '9' or tk == '(' or tk == ')':
		express += tk
		tk = ''
		# Degerler Duzenlendi
		elif tk == '+' or tk == '-' or tk == '*' or tk == '/' or tk == '%':
		express += tk
		isexpress = 1
		tk = ''
		# Isaretler Duzenlendi
		elif tk == '"' or tk == ' "':
            if bolge == False:
                bolge = True
            elif bolge == True:
                tokens.append(string + '"')
                string = ''
                bolge = False
                tk = ''
	    # Diger Isaret Tanımları
        elif bolge == True:
            string += tk
            tk = ''
			
			return tokenler
