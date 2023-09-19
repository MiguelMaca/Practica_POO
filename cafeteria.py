class Cafeteria:

    def __init__(self):
        self.capacidad_max = 1000
        self.capacidad_act = 0
        self.capacidad_act = self.capacidad_max

        if self.capacidad_act > self.capacidad_max:
            self.capacidad_act = self.capacidad_max


    def llenarCaf(self):
        self.capacidad_act = self.capacidad_max
        print("Se lleno la cafetera")


    def servirTaza(self):
        if self.capacidad_act < 100:
            print("No hay suficiente cafe en la cafetera")
            print("Favor de llenar la cafetera")
        else:
            self.capacidad_act = self.capacidad_act - 100
            print("Se sirvio una taza de cafe")
            print("Cantidad actual en la cafetera: ", self.capacidad_act)


    def vaciarCaf(self):
        self.capacidad_act = 0
        print("La cafetera esta vacia")


    def agregarCafe(self):
        agregar = int(input("Ingrese la cantidad de cafe que desea agregar"))
        self.capacidad_act = self.capacidad_act + agregar
        print(self.capacidad_act)


cafe = Cafeteria()
a = 0
while a == 0:
    print("-----MENU CAFETERIA-----")
    print("1. Llenar Cafetera")
    print("2. Servir Taza")
    print("3. Vaciar Cafetera")
    print("4. Agregar Cafe")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        cafe.llenarCaf()
    elif opcion == 2:
        cafe.servirTaza()
    elif opcion == 3:
        cafe.vaciarCaf()
    elif opcion == 4:
        cafe.agregarCafe()
    elif opcion == 5:
        a = 1
    else:
        print("Opcion no Encontrada")
