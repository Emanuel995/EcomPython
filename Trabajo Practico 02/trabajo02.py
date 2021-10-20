import os

from src.validar_linea import validar_cueanexo, validar_sector, validar_ambito

#Limpiar pantalla
os.system("clear")

#Abrir Archivo de entrada
archivo = open('prueba.txt','r')
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
        for i in range(len(linea)):
            if i == 1:
                #cueanexo
                validar_cueanexo(linea[i])
            if i == 3:
                validar_sector(linea[i])
            if i == 4:
                validar_ambito(linea[i])
            #Armo el renglon para mostrar
            renglon += linea[i]+'\t'
            
        print(renglon)

    cont_lineas += 1