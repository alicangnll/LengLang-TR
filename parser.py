# -*- coding: utf-8 -*-
symbols = {}


def alDEGISKEN(varname, symbols):
    if varname in symbols:
        return symbols[varname]


def YERLESTIR(varname, varvalue):
    global symbols
    symbols[varname[4:]] = varvalue


def parser(tokenler,i):
    try:
        while i < len(tokenler):
            if tokenler[i] == 'EGER':
                if tokenler[i + 2] == 'ESES':
                    if tokenler[i + 1][0:4] == "OPER":
                        tokenler[i + 1] = "SAYI:" + str(eval(tokenler[i + 1][5:]))
                    if tokenler[i + 3][0:4] == "OPER":
                        tokenler[i + 3] = "SAYI:" + str(eval(tokenler[i + 3][5:]))
                    if tokenler[i + 1][0:4] == "DEG:":
                        tokenler[i + 1] = alDEGISKEN(tokenler[i + 1][4:],symbols)
                    if tokenler[i + 3][0:4] == "DEG:":
                        tokenler[i + 3] = alDEGISKEN(tokenler[i + 3][4:],symbols)
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
                    if tokenler[i - 1][0:4] == "OPER":
                        tokenler[i - 1] = "SAYI:" + str(eval(tokenler[i - 1][5:]))
                    if tokenler[i - 3][0:4] == "OPER":
                        tokenler[i - 3] = "SAYI:" + str(eval(tokenler[i - 3][5:]))
                    if tokenler[i - 1][0:4] == "DEG:":
                        pram_a_is_var = True
                        pram_a_name = tokenler[i - 1][4:]
                        tokenler[i - 1] = alDEGISKEN(tokenler[i - 1][4:],symbols)
                    if tokenler[i - 3][0:4] == "DEG:":
                        pram_b_is_var = True
                        pram_b_name = tokenler[i - 3][4:]
                        tokenler[i - 3] = alDEGISKEN(tokenler[i - 3][4:],symbols)
                    if tokenler[i - 1] == tokenler[i - 3]:
                        i += 1
                        a = i
                        while tokenler[a] != 'TEKRAR':
                            a += 1
                        while tokenler[i] != 'TEKRAR' and i < len(tokenler) and alDEGISKEN(pram_a_name,symbols) == alDEGISKEN(pram_b_name,symbols):
                            parser(tokenler[0:a+i],i)
                    else:
                        while tokenler[i] != 'TEKRAR':
                            i += 1
                
            elif tokenler[i] == 'YAZ':
                data = tokenler[i + 1]
                if data[0] == '"':
                    data = data.replace('"', '')
                elif data[0:4] == 'SAYI':
                    data = data[5:]
                elif data[0:4] == 'OPER':
                    data = data[5:]
                    data = eval(data)
                elif data[0:3] == 'DEG':
                    data = alDEGISKEN(data[4:], symbols)
                print data
                i += 2
            elif tokenler[i][0:4] == 'DEG:' and tokenler[i + 1] == 'ESITTIR':
                if tokenler[i + 2][0] == '"':
                    data = tokenler[i + 2].replace('"', '')
                    YERLESTIR(tokenler[i], data)
                elif tokenler[i + 2][0:4] == 'SAYI':
                    data = tokenler[i + 2][5:]
                    YERLESTIR(tokenler[i], data)
                elif tokenler[i + 2][0:4] == 'OPER':
                    data = tokenler[i + 2][5:]
                    data = eval(data)
                    YERLESTIR(tokenler[i], data)
                elif tokenler[i + 2][0:4] == 'DEG:':
                    YERLESTIR(tokenler[i], alDEGISKEN(tokenler[i + 2][4:], symbols))
                elif tokenler[i + 2] == 'GIRDI':
                    data = raw_input(tokenler[i + 3].replace('"', ''))
                    YERLESTIR(tokenler[i], data)
                i += 3
            elif tokenler[i] == "CIK":
                exit()
            elif tokenler[i] == 'EKLE':
                if tokenler[i + 2][0:4] == 'OPER':
                    data = eval(tokenler[i + 2][5:])
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data + data))

                    i += 3
                elif tokenler[i + 2][0:4] == 'SAYI':
                    data = int(tokenler[i + 2][5:])
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data + data))

                    i += 3
                elif  tokenler[i + 2][0:4] == 'DEG:':
                    data =  int(alDEGISKEN(tokenler[i + 2][4:],symbols))
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data + data))

                    i += 3
                else:
                    i += 3
            elif tokenler[i] == 'CARP':
                if tokenler[i + 2][0:4] == 'OPER':
                    data = eval(tokenler[i + 2][5:])
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data * data))

                    i += 3
                elif tokenler[i + 2][0:4] == 'SAYI':
                    data = int(tokenler[i + 2][5:])
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data * data))

                    i += 3
                elif  tokenler[i + 2][0:4] == 'DEG:':
                    data =  int(alDEGISKEN(tokenler[i + 2][4:],symbols))
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data * data))

                    i += 3
                else:
                    i += 3
            elif tokenler[i] == 'BOL':
                if tokenler[i + 2][0:4] == 'OPER':
                    data = eval(tokenler[i + 2][5:])
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data / data))

                    i += 3
                elif tokenler[i + 2][0:4] == 'SAYI':
                    data = int(tokenler[i + 2][5:])
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data / data))

                    i += 3
                elif  tokenler[i + 2][0:4] == 'DEG:':
                    data =  int(alDEGISKEN(tokenler[i + 2][4:],symbols))
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data / data))

                    i += 3
                else:
                    i += 3
            elif tokenler[i] == 'EKSI':
                if tokenler[i + 2][0:4] == 'OPER':
                    data = eval(tokenler[i + 2][5:])
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data - data))

                    i += 3
                elif tokenler[i + 2][0:4] == 'SAYI':
                    data = int(tokenler[i + 2][5:])
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data - data))

                    i += 3
                elif  tokenler[i + 2][0:4] == 'DEG:':
                    data =  int(alDEGISKEN(tokenler[i + 2][4:],symbols))
                    var_data = int(alDEGISKEN(tokenler[i + 1][4:],symbols))
                    YERLESTIR(tokenler[i + 1],str(var_data - data))

                    i += 3


            else:
                i += 1


    except Exception as e:
        if str(e) == "list index out of range":
            pass
        else:
            print(e)