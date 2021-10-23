def abrir_archivo(nombre,modo):
    return open(nombre,modo)

def escribir_archivo(nombre,texto):
    try:
        archivo = open(nombre,'x')
        print("archivo creado")
    except:
        archivo = open(nombre,'a')
        print("archivo ya existente abierto")
    archivo.write(texto)
    archivo.write('\n')
    archivo.close()
    

