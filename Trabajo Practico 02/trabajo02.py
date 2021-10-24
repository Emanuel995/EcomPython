import os
import datetime

from src.validar_linea import validar_cueanexo, validar_sector, validar_ambito, validar_codarea, validar_codpostal, validar_nrotel, validar_true_false
from src.gestion_archivos import abrir_archivo, escribir_archivo, limpiar_archivos
from src.parametros import ARCH_ENT, ARCH_FILTRO, ARCH_LOG, ARCH_ESTABLECIMIENTOS

#Limpiar pantalla
if os.name =='posix':
    os.system("clear")
else:
    os.system("cls")
print("Corriendo el programa desde un sistema: "+os.name+'\n')

#Configuracion de archivos de entrada
archivo_filtro = abrir_archivo(ARCH_FILTRO,'r')
archivo = abrir_archivo(ARCH_ENT,'r')

#Limpiar archivos de salida
ARCHIVOS = [ARCH_LOG, ARCH_ESTABLECIMIENTOS]
limpiar_archivos(ARCHIVOS)

#Variables para el Diccionario
establecimientos = {}
establecimiento = {}
cueanexos = []

#Recupero los cueanexo filtros VALIDOS
for line in archivo_filtro:
    try: 
        cueanexos.append(int(line.strip()))
    except:
        print("ERROR con el cueanexo de entrada. No es un numero "+line.strip())
print("CUEANEXOS FILTROS: "+str(cueanexos))

#Comienzo del tratamiento de archivos
cont_lineas = 0
cant_filtrados = 0
cant_validos = 0
cant_invalidos = 0
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
        is_valid = True
        for i in range(len(linea)):
            #0 Jurisdiccion
            if i == 0:
                establecimiento["Jurisdiccion"] = linea[i]
            #1 cueanexo
            if i == 1:
                if validar_cueanexo(linea[i]):
                    establecimiento["cueanexo"] = linea[i]                    
                else:
                    error = "ERROR TIPO DE DATO CUEANEXO"
                    is_valid = False
                    break  
            #2 Establecimiento
            if i == 2:
                establecimiento["Establecimiento"] = linea[i]
            #3 Sector
            if i == 3:
                if validar_sector(linea[i]):
                    establecimiento["Sector"] = linea[i]
                else:
                    error = "ERROR SECTOR INVALIDO"
                    is_valid = False
                    break
            #4 Ambito
            if i == 4:
                if validar_ambito(linea[i]):
                    establecimiento["Ambito"] = linea[i]
                else:
                    error = "ERROR AMBITO INVALIDO"
                    is_valid = False
                    break
            #5 Domicilio
            if i == 5:
                establecimiento["Domicilio"] = linea[i]
            #6 CP
            if i == 6:
                if validar_codpostal(linea[i]):
                    establecimiento["CP"] = linea[i]
                else:
                    error = "ERROR TIPO DE DATO COD POSTAL"
                    is_valid = False
                    break
            #7 Cod Area
            if i == 7:
                if validar_codarea(linea[i]):
                    establecimiento["CodArea"] = linea[i]
                else:
                    error = "ERROR TIPO DE DATO COD AREA"
                    is_valid = False
                    break
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
                    if validar_true_false(linea[i]):
                        establecimiento["Tipo"+str(i)] = linea[i].strip()         
                    else:
                        is_valid = False
                        error = "ERROR TIPO DE DATO (TRUE/FALSE)"
                        break
            #Armo el renglon para mostrar
            #renglon += linea[i]+'\t'

        #Grabo los cueanexos que coinciden con el filtro y no tiene errores
        if is_valid:
            if int(linea[1]) in cueanexos:
                escribir_archivo(ARCH_ESTABLECIMIENTOS,str(establecimiento))
                cant_filtrados +=1
            establecimientos.update({"Establecimiento_"+str(cont_lineas) : establecimiento})
            fecha = datetime.datetime.now()
            texto = fecha.strftime("%Y-%m-%d %H:%M ") + "CORRECTO Cueanexo = "+str(linea[1])
            escribir_archivo(ARCH_LOG,texto)
            cant_validos += 1
        else:
            fecha = datetime.datetime.now()
            texto = fecha.strftime("%Y-%m-%d %H:%M ") + error
            escribir_archivo(ARCH_LOG,texto)
            cant_invalidos += 1
    
    cont_lineas += 1
print("Se trataron un total de: "+str(cont_lineas-1)+" lineas.")
print("Se registraron "+str(cant_validos)+" Establecimientos VALIDOS.")
print("Se Registraron "+str(cant_filtrados)+" Establecimientos que coinciden con el archivo de FILTRO.")
print("Se Registraron "+str(cant_invalidos)+" Establecimientos INVALIDOS.")