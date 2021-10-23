import os

from src.validar_linea import validar_cueanexo, validar_sector, validar_ambito, validar_codarea, validar_codpostal, validar_nrotel, validar_true_false
from src.gestion_archivos import abrir_archivo, escribir_archivo

#Limpiar pantalla

if os.name =='posix':
    os.system("clear")
else:
    os.system("cls")
print(os.name)

#Configuracion de archivos
ARCH_ENT = 'prueba.txt'
archivo = abrir_archivo(ARCH_ENT,'r')

ARCH_FILTRO = 'establecimientos_filtros.txt'
archivo_filtro = abrir_archivo(ARCH_FILTRO,'r')

ARCH_SALIDA = 'errores.txt'

establecimientos = {}
establecimiento = {}

#Comienzo del tratamiento de archivos
cont_lineas = 0
for line in archivo:
    linea = line.split(';')
    if cont_lineas == 0:
        #Titulos
        renglon = ""
        for l in linea:
            renglon += l+'\t'
        print(renglon)
    else:
        #Información
        renglon = ""
        establecimiento = {}
        for i in range(len(linea)):
            #0 Jurisdiccion
            if i == 0:
                establecimiento["Jurisdiccion"] = linea[i]
            #1 cueanexo
            if i == 1:
                if validar_cueanexo(linea[i]):
                    pass
                else:
                    pass
                establecimiento["cueanexo"] = str(linea[i])
            #2 Establecimiento
            if i == 2:
                establecimiento["Establecimiento"] = linea[i]
            #3 Sector
            if i == 3:
                validar_sector(linea[i])
                establecimiento["Sector"] = linea[i]
            #4 Ambito
            if i == 4:
                validar_ambito(linea[i])
                establecimiento["Ambito"] = linea[i]
            #5 Domicilio
            if i == 5:
                establecimiento["Domicilio"] = linea[i]
            #6 CP
            if i == 6:
                validar_codpostal(linea[i])
                establecimiento["CP"] = linea[i]
            #7 Cod Area
            if i == 7:
                validar_codarea(linea[i])
                establecimiento["CodArea"] = linea[i]
            #8 Telefono
            if i == 8:
                establecimiento["Telefono"] = validar_nrotel(linea[i])
            #9 Cod Loc
            if i == 9:
                establecimiento["CodLoc"] = linea[i]
            #10 Localidad
            if i == 10:
                establecimiento["Localidad"] = linea[i]
            #11 Departamento
            if i == 11:
                establecimiento["Departamento"] = linea[i]
            #12 Mail 
            if i > 11:
                if "@" in str(linea[i]):
                    establecimiento["Mail"] = linea[i]
                else:
                    #Validar True/False
                    validar_true_false(linea[i])
                    establecimiento["Tipo"+str(i)] = linea[i]

            #Armo el renglon para mostrar
            renglon += linea[i]+'\t'
        escribir_archivo(ARCH_SALIDA,str(establecimiento))
        #print(renglon)
        #print(establecimiento)

    cont_lineas += 1