import os
os.system("clear")
print("Estas usando un sistema: "+os.name)
file = open("examenes.txt","r")
cant = 0
suma = 0
nota_min = 9999
nota_max = 00
lista_max = []
lista_min = []
for line in file:
    
    if cant == 0:
        pass
        #Titulos
    else:
        x = line.split(",")
        nota = int(x[1])
        nombre = str(x[0])
        if nota > nota_max:
            lista_max.clear()
            lista_max.append([nombre,nota])
            nota_max = nota
            
        if nota == nota_max:
            lista_max.append([nombre,nota])
            nota_max = nota

        if nota < nota_min:
            lista_min.clear()
            lista_max.append([nombre,nota])
            nota_min = nota
            
        if nota == nota_min:
            lista_min.append([nombre,nota])
            nota_min = nota
        
        suma = suma + nota
    cant = cant + 1
print("Lista de Notas MAS ALTAS")
print("")
for l in lista_max:
    print(l)
print("")
print("============")
print("")
print("Lista de Notas MAS BAJAS")
for l in lista_min:
    print(l)
print("")
print("============")
print("")
print("primedio: "+str(round(suma/cant,2))) 