# -*- coding: utf-8 -*-
def leng2(filecontents):
	tk = ''
	tks = []
	var = ''
	var_basla = 0
	bolge = False
	string = ''
	express = ''
	isexpress = 0
	n = ''
	filecontents = list(filecontents)
	for char in filecontents:
		tk += char
		if tk == ' ':
			if bolge == False:
				tk = ''
			elif bolge == True:
				tk = " "
				if express != '' and isexpress == 1:
					tks.append('OPER:' + express)
					express = ''
					tk = ''
			elif express != '' and isexpress == 0:
					tks.append('SAYI:' + express)
					express = ''
					tk = ''
			elif var != '':
					tks.append('DEG:' + var)
					var = ''
					var_basla = 0
					tk = ''
		elif tk == '\n' or tk == '<EOF>':
			if express != '' and isexpress == 1:
						tks.append('OPER:' + express)
						express = ''
			elif express != '' and isexpress == 0:
						tks.append('SAYI:' + express)
						express = ''
			elif var != '':
						tks.append('DEG:' + var)
						var = ''
						var_basla = 0
						tk = ''
			elif tk == '\t':
						tk = ''
			elif tk == '=' and bolge == False:
				if express != '' and isexpress == 0:
					tks.append('SAYI:' + express)
					express = ''
				if var != '':
					tks.append('DEG:' + var)
					var = ''
					var_basla = 0
				if tks[-1] == 'ESITTIR':
					tks[-1] = 'ESIT'
				else:
					tks.append('ESITTIR')
				tk = ''
			elif tk == '&' and bolge == False:
				var_basla = 1
				var += tk
				tk = ''
			elif var_basla == 1:
				if tk != '+' or tk == '-' or tk == '*' or tk == '/' or tk == '%':
					var += tk
					tk = ''
				else:
					var_basla = 0
					tk = ''
			elif tk == 'YAZ' or tk == 'yaz':
				tks.append('YAZ')
				tk = ''
			elif tk == 'EKLE' or tk == 'ekle':
				tks.append('EKLE')
				tk = ''
			elif tk == 'CARP' or tk == 'çarp':
				tks.append('CARP')
				tk = ''
			elif tk == 'BOL' or tk == 'böl':
				tks.append('BOL')
				tk = ''
			elif tk == 'EKSI' or tk == 'eksi':
				tks.append('EKSI')
				tk = ''
			elif tk == 'BOYLEYKEN' or tk == 'böyleyken':
				tks.append('BOYLEYKEN')
				tk = ''
			elif tk == 'TEKRAR' or tk == 'tekrar':
				tks.append('TEKRAR')
				tk = ''
			elif tk == 'ÇIK' or tk == "çık":
				tks.append("CIK")
				tk = ""
			elif tk == 'YAP' or tk == 'yap':
				tks.append('YAP')
				tk = ''
			elif tk == 'EĞER' or tk == 'eğer':
				tks.append('EGER')
				tk = ''
			elif tk == 'İSE' or tk == 'ise':
				if express != '' and isexpress == 0:
					tks.append('SAYI:' + express)
					express = ''
				tks.append('ISE')
				tk = ''
			elif tk == 'GİRDİ' or tk == 'girdi' or tk == 'GİRİŞ' or tk == 'giriş':
				tks.append('GIRDI')
				tk = ''
			elif tk == '0' or tk == '1' or tk == '2' or tk == '3' or tk == '4' or tk == '5' or tk == '6' or tk == '7' or tk == '8' or tk == '9' or tk == '(' or tk == ')':
				express += tk
				tk = ''
			elif tk == '+' or tk == '-' or tk == '*' or tk == '/' or tk == '%':
				express += tk
				isexpress = 1
				tk = ''
			elif tk == '"' or tk == ' "':
				if bolge == False:
					bolge = True
				elif bolge == True:
					tks.append(string + '"')
					string = ''
					bolge = False
				tk = ''
			elif bolge == True:
				string += tk
				tk = ''
	return tks
