def abrir_archivo(nombre,modo):
    return open(nombre,modo)

def escribir_archivo(nombre,texto):
    try:
        archivo = open(nombre,'x')
        #print("archivo creado")
    except:
        archivo = open(nombre,'a')
        #print("archivo ya existente abierto")
    archivo.write(texto)
    archivo.write('\n')
    archivo.close()

def limpiar_archivos(archivos):
    for archivo in archivos:
        f = open(archivo,'w')
        f.close()

    print("Archivos de salidas Inicializados...")

    

