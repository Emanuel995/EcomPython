
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
         
def validar_sector(sector):
    VALIDO = ("ESTATAL", "PRIVADO", "SOCIAL/COOPERATIVA")
    if sector.upper() in VALIDO:
        print("SECTOR VALIDO")
        is_error = False
    else:
        print("SECTOR INVALIDO")
        is_error = True
    
    return is_error

def validar_ambito(ambito):
    VALIDO = ("RURAL", "URBANO")
    if ambito.upper() in VALIDO:
        print("AMBITO VALIDO")
        is_error = False
    else:
        print("AMBITO INVALIDO")
        is_error = True

    return is_error

def validar_codpostal(codpostal):
    try:
        int(codpostal)
        is_error = False
    except:
        print("ERROR TIPO DE DATO COD POSTAL")
        is_error = True 
    
    return is_error

def validar_codarea(codarea):
    pass

def validar_nrotel(nrotel):
    pass