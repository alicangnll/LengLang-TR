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
                        tokenler[i + 1] = "SAYI" + str(eval(tokenler[i + 1][5:]))
                    if tokenler[i + 3][0:4] == "OPERATION":
                        tokenler[i + 3] = "SAYI:" + str(eval(tokenler[i + 3][5:]))
					if tokenler[i + 1][0:4] == "DEGER":
                        tokenler[i + 1] = DEGISKENAL(tokenler[i + 1][4:],semboller)
					if tokenler[i + 3][0:4] == "DEGER":
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
            	    if tokenler[i - 2] == 'ESIT':
                    if tokenler[i - 1][0:4] == "OPERATION":
			tokenler[i - 1] = "SAYI:" + str(eval(tokenler[i - 1][5:]))
                    if tokenler[i - 3][0:4] == "OPERATION":
			tokenler[i - 3] = "SAYI:" + str(eval(tokenler[i - 3][5:]))
		    if tokenler[i - 1][0:4] == "DEGER:":
			pram_a_is_var = True
			pram_a_name = tokenler[i - 1][4:]
			tokenler[i - 1] = DEGISKENAL(tokenler[i - 1][4:],semboller)
		    if tokenler[i - 3][0:4] == "DEGER:":
			pram_b_is_var = True
			pram_b_name = tokenler[i - 3][4:]
			tokenler[i - 3] = DEGISKENAL(tokenler[i - 3][4:],semboller)
		    if tokenler[i - 1] == tokenler[i - 3]:
			i += 1
			a = i
                    while tokenler[a] != 'TEKRAR':
			a += 1
                    while tokenler[i] != 'TEKRAR' and i < len(tokenler) and DEGISKENAL(pram_a_name,semboller) == DEGISKENAL(pram_b_name,semboller):
                        parser(tokenler[0:a+i],i)
		    else:
                    while tokenler[i] != 'TEKRAR':
                        i += 1
						
        elif tokenler[i] == 'YAZDIR':
			veri = tokenler[i + 1]
			if veri[0] == '"':
				veri = veri.replace('"', '')
			elif veri[0:4] == 'SAYI':
				veri = veri[5:]
			elif veri[0:4] == 'OPERATION':
				veri = veri[5:]
				veri = eval(veri)
			elif veri[0:3] == 'DEGER':
				veri = DEGISKENAL(veri[4:], semboller)
			print veri
			i += 2
		elif tokenler[i][0:4] == 'DEGER:' and tokenler[i + 1] == 'ESITTIR':
			if tokenler[i + 2][0] == '"':
				veri = tokenler[i + 2].replace('"', '')
				YERLESTIR(tokenler[i], veri)
			elif tokenler[i + 2][0:4] == 'SAYI':
				veri = tokenler[i + 2][5:]
				YERLESTIR(tokenler[i], veri)
			elif tokenler[i + 2][0:4] == 'OPERATION':
				veri = tokenler[i + 2][5:]
				veri = eval(veri)
				YERLESTIR(tokenler[i], veri)
			elif tokenler[i + 2][0:4] == 'DEGER:':
				YERLESTIR(tokenler[i], DEGISKENAL(tokenler[i + 2][4:], semboller))
			elif tokenler[i + 2] == 'GIRDI':	
				veri = raw_input(tokenler[i + 3].replace('"', ''))
				YERLESTIR(tokenler[i], veri)
				i += 3
			elif tokenler[i] == "CIK":
				exit()
			elif tokenler[i] == 'EKLE':
			if tokenler[i + 2][0:4] == 'OPERATION':
				veri = eval(tokenler[i + 2][5:])
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data + veri))
				
				i += 3
			elif tokenler[i + 2][0:4] == 'SAYI':
				veri = int(tokenler[i + 2][5:])
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data + veri))
				
				i += 3
			elif  tokenler[i + 2][0:4] == 'DEGER:':
				veri =  int(DEGISKENAL(tokenler[i + 2][4:],semboller))
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data + veri))
				
				i += 3
			else:
				i += 3
			elif tokenler[i] == 'CARP':
			if tokenler[i + 2][0:4] == 'OPERATION':
				veri = eval(tokenler[i + 2][5:])
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data * veri))
				
				i += 3
			elif tokenler[i + 2][0:4] == 'SAYI':
				veri = int(tokenler[i + 2][5:])
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data * veri))
				
				i += 3
			elif tokenler[i + 2][0:4] == 'DEGER:':
				veri =  int(DEGISKENAL(tokenler[i + 2][4:],semboller))
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data * veri))
				
				i += 3
			else:
				i += 3
			elif tokenler[i] == 'BOL':
			if tokenler[i + 2][0:4] == 'OPERATION':
				veri = eval(tokenler[i + 2][5:])
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data / veri))
				
				i += 3
			elif tokenler[i + 2][0:4] == 'SAYI':
				veri = int(tokenler[i + 2][5:])
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data / veri))
				
				i += 3
			elif  tokenler[i + 2][0:4] == 'DEGER:':
				veri =  int(DEGISKENAL(tokenler[i + 2][4:],semboller))
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data / veri))
				
				i += 3
			else:
				i += 3
			elif tokenler[i] == 'EKSI':
			if tokenler[i + 2][0:4] == 'OPERATION':
				veri = eval(tokenler[i + 2][5:])
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data - veri))
				
				i += 3
			elif tokenler[i + 2][0:4] == 'SAYI':
				veri = int(tokenler[i + 2][5:])
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data - veri))
				
				i += 3
			elif  tokenler[i + 2][0:4] == 'DEGER:':
				veri =  int(DEGISKENAL(tokenler[i + 2][4:],semboller))
				var_data = int(DEGISKENAL(tokenler[i + 1][4:],semboller))
				YERLESTIR(tokenler[i + 1],str(var_data - veri))
				
				i += 3


            		else:
				i += 1
	except Exception as e:
			if str(e) == "list index out of range":
				pass
			else:
				print(e)
