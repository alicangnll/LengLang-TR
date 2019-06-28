# -*- coding: utf-8 -*-
semboller = {}


def alDEGISKEN(varname, semboller):
    if varname in semboller:
        return semboller[varname]


def YERLESTIR(varname, varvalue):
    global semboller
    semboller[varname[4:]] = varvalue


def parser(tks,i):
    try:
        while i < len(tks):
            if tks[i] == 'EGER':
                if tks[i + 2] == 'ESIT':
                    if tks[i + 1][0:4] == "OPER":
                        tks[i + 1] = "SAYI:" + str(eval(tks[i + 1][5:]))
                    if tks[i + 3][0:4] == "OPER":
                        tks[i + 3] = "SAYI:" + str(eval(tks[i + 3][5:]))
                    if tks[i + 1][0:4] == "DEG:":
                        tks[i + 1] = alDEGISKEN(tks[i + 1][4:],semboller)
                    if tks[i + 3][0:4] == "DEG:":
                        tks[i + 3] = alDEGISKEN(tks[i + 3][4:],semboller)
                    if tks[i + 1] == tks[i + 3]:
                        i += 5
                        a = i
                        while tks[a] != 'YAP':
                            a += 1
                        while tks[i] != 'YAP' and i < len(tks):
                            parser(tks[0:a+i],i)
                            i += 1
                    else:
                        while tks[i] != 'YAP':
                            i += 1
            elif tks[i] == 'IKEN':
                _i = 0
                if tks[i - 2] == 'ESIT':
                    if tks[i - 1][0:4] == "OPER":
                        tks[i - 1] = "SAYI:" + str(eval(tks[i - 1][5:]))
                    if tks[i - 3][0:4] == "OPER":
                        tks[i - 3] = "SAYI:" + str(eval(tks[i - 3][5:]))
                    if tks[i - 1][0:4] == "DEG:":
                        pram_a_is_var = True
                        pram_a_name = tks[i - 1][4:]
                        tks[i - 1] = alDEGISKEN(tks[i - 1][4:],semboller)
                    if tks[i - 3][0:4] == "DEG:":
                        pram_b_is_var = True
                        pram_b_name = tks[i - 3][4:]
                        tks[i - 3] = alDEGISKEN(tks[i - 3][4:],semboller)
                    if tks[i - 1] == tks[i - 3]:
                        i += 1
                        a = i
                        while tks[a] != 'TEKRAR':
                            a += 1
                        while tks[i] != 'TEKRAR' and i < len(tks) and alDEGISKEN(pram_a_name,semboller) == alDEGISKEN(pram_b_name,semboller):
                            parser(tks[0:a+i],i)
                    else:
                        while tks[i] != 'TEKRAR':
                            i += 1
                
            elif tks[i] == 'YAZ':
                veri = tks[i + 1]
                if veri[0] == '"':
                    veri = veri.replace('"', '')
                elif veri[0:4] == 'SAYI':
                    veri = veri[5:]
                elif veri[0:4] == 'OPER':
                    veri = veri[5:]
                    veri = eval(veri)
                elif veri[0:3] == 'DEG':
                    veri = alDEGISKEN(veri[4:], semboller)
                print veri
                i += 2
            elif tks[i][0:4] == 'DEG:' and tks[i + 1] == 'ESITTIR':
                if tks[i + 2][0] == '"':
                    veri = tks[i + 2].replace('"', '')
                    YERLESTIR(tks[i], veri)
                elif tks[i + 2][0:4] == 'SAYI':
                    veri = tks[i + 2][5:]
                    YERLESTIR(tks[i], veri)
                elif tks[i + 2][0:4] == 'OPER':
                    veri = tks[i + 2][5:]
                    veri = eval(veri)
                    YERLESTIR(tks[i], veri)
                elif tks[i + 2][0:4] == 'DEG:':
                    YERLESTIR(tks[i], alDEGISKEN(tks[i + 2][4:], semboller))
                elif tks[i + 2] == 'GIRDI':
                    veri = raw_input(tks[i + 3].replace('"', ''))
                    YERLESTIR(tks[i], veri)
                i += 3
            elif tks[i] == "CIK":
                exit()
            elif tks[i] == 'EKLE':
                if tks[i + 2][0:4] == 'OPER':
                    veri = eval(tks[i + 2][5:])
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data + veri))

                    i += 3
                elif tks[i + 2][0:4] == 'SAYI':
                    veri = int(tks[i + 2][5:])
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data + veri))

                    i += 3
                elif  tks[i + 2][0:4] == 'DEG:':
                    veri =  int(alDEGISKEN(tks[i + 2][4:],semboller))
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data + veri))

                    i += 3
                else:
                    i += 3
            elif tks[i] == 'CARP':
                if tks[i + 2][0:4] == 'OPER':
                    veri = eval(tks[i + 2][5:])
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data * veri))

                    i += 3
                elif tks[i + 2][0:4] == 'SAYI':
                    veri = int(tks[i + 2][5:])
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data * veri))

                    i += 3
                elif  tks[i + 2][0:4] == 'DEG:':
                    veri =  int(alDEGISKEN(tks[i + 2][4:],semboller))
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data * veri))

                    i += 3
                else:
                    i += 3
            elif tks[i] == 'BOL':
                if tks[i + 2][0:4] == 'OPER':
                    veri = eval(tks[i + 2][5:])
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data / veri))

                    i += 3
                elif tks[i + 2][0:4] == 'SAYI':
                    veri = int(tks[i + 2][5:])
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data / veri))

                    i += 3
                elif  tks[i + 2][0:4] == 'DEG:':
                    veri =  int(alDEGISKEN(tks[i + 2][4:],semboller))
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data / veri))

                    i += 3
                else:
                    i += 3
            elif tks[i] == 'EKSI':
                if tks[i + 2][0:4] == 'OPER':
                    veri = eval(tks[i + 2][5:])
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data - veri))

                    i += 3
                elif tks[i + 2][0:4] == 'SAYI':
                    veri = int(tks[i + 2][5:])
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data - veri))

                    i += 3
                elif  tks[i + 2][0:4] == 'DEG:':
                    veri =  int(alDEGISKEN(tks[i + 2][4:],semboller))
                    var_data = int(alDEGISKEN(tks[i + 1][4:],semboller))
                    YERLESTIR(tks[i + 1],str(var_data - veri))

                    i += 3


            else:
                i += 1


    except Exception as e:
        if str(e) == "list index out of range":
            pass
        else:
            print(e)
