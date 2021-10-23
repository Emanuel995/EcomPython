
#Validacion cueanexo   
def validar_cueanexo(cueanexo):
    if len(cueanexo) == 9:
        try:
            int(cueanexo)
            is_valid = True
        except:
            print("ERROR TIPO DE DATO CUEANEXO")
            is_valid = False
    else:
        print("ERROR LONGITUD DE CUEANEXO")
        is_valid = False
    
    return is_valid
         
#Validar sector
def validar_sector(sector):
    VALIDO = ("ESTATAL", "PRIVADO", "SOCIAL/COOPERATIVA")
    if sector.upper() in VALIDO:
        #print("SECTOR VALIDO")
        is_valid = True
    else:
        #print("SECTOR INVALIDO")
        is_valid = False
    
    return is_valid

#Validar ambito
def validar_ambito(ambito):
    VALIDO = ("RURAL", "URBANO")
    if ambito.upper() in VALIDO:
        #print("AMBITO VALIDO")
        is_valid = True
    else:
        #print("AMBITO INVALIDO")
        is_valid = False

    return is_valid

#Validar codpostal
def validar_codpostal(codpostal):
    try:
        int(codpostal)
        is_valid = True
        #print("TIPO DE DATO CORRECTO COD POSTAL")
    except:
        #print("ERROR TIPO DE DATO COD POSTAL")
        is_valid = False 
    
    return is_valid

#Validar codarea
def validar_codarea(codarea):
    try:
        int(codarea)
        is_valid = True
        #print("TIPO DE DATO CORRECTO COD AREA")
    except:
        #print("ERROR TIPO DE DATO COD AREA")
        is_valid = False 
    return is_valid

#Validar nrotel
def validar_nrotel(nrotel):
    nrotel_valido = ''
    nrotel_valido = filter(lambda x: x in [1,2,3,4,5,6,7,8,9,0], nrotel)
    #for nro in nrotel:
    #    if nro in [1,2,3,4,5,6,7,8,9,0]:
    #        nrotel_valido+= nro
    return nrotel_valido

#Validar verdadero falso
def validar_true_false(booleano):
    if booleano.upper().strip() == 'VERDADERO' or booleano.upper().strip() == 'FALSO':
        is_valid = True
        #print("TIPO DE DATO CORRECTO (TRUE/FALSE)")
    else:
        is_valid = False
        #print("ERROR TIPO DE DATO (TRUE/FALSE) ")
    return is_valid
