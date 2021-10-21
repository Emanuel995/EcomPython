import os

from src.validar_linea import validar_cueanexo, validar_sector, validar_ambito, validar_codarea, validar_codpostal, validar_nrotel, validar_true_false

#Limpiar pantalla
#if os.name =='nt':
#    os.system("cls")
#else:
#    os.system("clear")

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
            #5 Domicilio
            #6 CP
            if i == 6:
                validar_codpostal(linea[i])
            #7 Cod Area
            if i == 7:
                validar_codarea(linea[i])
            #8 Telefono
            if i == 8:
                validar_nrotel(linea[i])
            #9 Cod Loc
            #10 Localidad
            #11 Departamento
            #12 Mail 
            if i > 11:
                if "@" in str(linea[i]):
                    mail = str(linea[i])
                else:
                    #Validar True/False
                    validar_true_false(linea[i])

            #Armo el renglon para mostrar
            renglon += linea[i]+'\t'
            
        print(renglon)

    cont_lineas += 1