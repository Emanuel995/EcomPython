
#Validacion cueanexo   
def validar_cueanexo(cueanexo):
    if len(cueanexo) == 9:
        try:
            int(cueanexo)
            is_error = False
        except:
            print("ERROR TIPO DE DATO CUEANEXO")
            is_error = True
    else:
        print("ERROR LONGITUD DE CUEANEXO")
        is_error = True
    
    return is_error
         
#Validar sector
def validar_sector(sector):
    VALIDO = ("ESTATAL", "PRIVADO", "SOCIAL/COOPERATIVA")
    if sector.upper() in VALIDO:
        print("SECTOR VALIDO")
        is_error = False
    else:
        print("SECTOR INVALIDO")
        is_error = True
    
    return is_error

#Validar ambito
def validar_ambito(ambito):
    VALIDO = ("RURAL", "URBANO")
    if ambito.upper() in VALIDO:
        print("AMBITO VALIDO")
        is_error = False
    else:
        print("AMBITO INVALIDO")
        is_error = True

    return is_error

#Validar codpostal
def validar_codpostal(codpostal):
    try:
        int(codpostal)
        is_error = False
        print("TIPO DE DATO CORRECTO COD POSTAL")
    except:
        print("ERROR TIPO DE DATO COD POSTAL")
        is_error = True 
    
    return is_error

#Validar codarea
def validar_codarea(codarea):
    try:
        int(codarea)
        is_error = False
        print("TIPO DE DATO CORRECTO COD AREA")
    except:
        print("ERROR TIPO DE DATO COD AREA")
        is_error = True 
    return is_error

#Validar nrotel
def validar_nrotel(nrotel):
    nrotel_valido = ''
    for nro in nrotel:
        if nro in [1,2,3,4,5,6,7,8,9,0]:
            nrotel_valido+= nro
    return nrotel_valido

#Validar verdadero falso
def validar_true_false(booleano):
    if booleano.upper().strip() == 'VERDADERO' or booleano.upper().strip() == 'FALSO':
        is_error = False
        print("TIPO DE DATO CORRECTO (TRUE/FALSE)")
    else:
        is_error = True
        print("ERROR TIPO DE DATO (TRUE/FALSE) ")
    return is_error
