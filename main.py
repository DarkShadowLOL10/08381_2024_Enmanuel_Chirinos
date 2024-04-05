# sacar lineaS POR QUE ALGUNAS NO SERVIRAN SE EJECUTARAN VARIAS VECES #
def resistenciaMaterial(x, y):
    z = (x**2 + y**2)**2 + (x**2 - y**2)

x = 2
y = 20

if [x > y]:
    print("ojo")

else:

    print("cara")

for i in [x, y]:
    if(x < i):
        print("hola")
    else:
        print("chao")

        while(x < y):
            print(("Locura") + str(x))

x = x + 1

z = resistenciaMaterial(x, y)
print(z)
