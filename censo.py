import numpy as np
Comunas = []
Poblacion2015 = []
Poblacion2016 = []
Nc=int(input("ingrese el n° de comunas:"))

for i in range(Nc):

    Comunas.append(input("Comuna: "))
    Poblacion2015.append(int(input("Población en 2015:")))
    Poblacion2016.append(int(input("Población en 2016:")))

print("Comunas: ", Comunas) #1)
print("--------------------------------------------------------")
print("Poblacion en 2015: ", Poblacion2015) #2)
print("--------------------------------------------------------")
print("Poblacion en 2016: ", Poblacion2016) #2)
print("--------------------------------------------------------")

lugar1 = Poblacion2016.index (max(Poblacion2016))
print("La comuna de mayor población para 2016 es", Comunas[lugar1], ",tenia", Poblacion2016[lugar1], "habitantes")# 4)
print("--------------------------------------------------------")

lugar2 = Poblacion2016.index (min(Poblacion2016))
print("La comuna de menor población para 2016 es", Comunas[lugar2], ",tenia", Poblacion2016[lugar2], "habitantes")#5)
print("--------------------------------------------------------")

rmaxmin = Poblacion2016[lugar1]/Poblacion2016[lugar2]
print("La relación de la comuna más habitada a la menos habitada en 2016 es:", round(rmaxmin,0))
print("--------------------------------------------------------")

promedio2015 = np.mean(Poblacion2015)
print("El promedio de habitantes en 2015 es: ", round(promedio2015,0))
print("--------------------------------------------------------")

promedio2016 = np.mean(Poblacion2016)
print("El promedio de habitantes en 2016 es: ", round(promedio2016,0))
pcrecimiento=(promedio2016-promedio2015)/promedio2015*100
print("--------------------------------------------------------")

print("El porcentaje de crecimiento en la región de Coquimboes:", round(pcrecimiento,1))# 7)
print("--------------------------------------------------------")

pcomuna=[]

for i in range(0,Nc):

    pcomuna.append(int(Poblacion2016[i]/sum(Poblacion2016)*100))
print("El porcentaje que corresponde a la comuna de", Comunas[i], "es:", round(pcomuna[i],0))

print("--------------------------------------------------------")
Comunam=Comunas[lugar1] #Comuna de mayor población
Comunas.remove(Comunas[lugar1])
Poblacion2016.remove(Poblacion2016[lugar1])

pcomuna1 = []
Nc1=Nc-1

for i in range(0,Nc1):
    pcomuna1.append(Poblacion2016[i]/sum(Poblacion2016)*100)
print("El porcentaje que corresponde a la comuna", Comunas[i], "sinconsiderar", Comunam, "es:", round(pcomuna1[i],0))
