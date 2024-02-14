from Vehicle import Vehicle

class Register:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        tipos=["carro", "avión", "barco"]
        
        for i in range(len(tipos)):
            print(f"{i+1}. {tipos[i]}")

        type = input("Inserte el tipo de vehículo: ")
        while not type.isnumeric() or int(type)-1 not in range(len(tipos)):
            type = input("Ingreso inválido, inserte el tipo de vehículo: ")
        type = int(type)
        type = tipos[type-1]

        model = input("Ingrese el modelo del vehículo: ")
        year = input("Ingrese el año del modelo: ")
        while not year.isnumeric() or int(year)>2024:
            year = input("Ingreso inválido, ingrese el año del modelo: ")
        
        mileage = input("Ingrese el kilometraje del vehículo: ")
        while not mileage.isnumeric() or int(mileage)<0:
            mileage = input("Ingreso inválido, ingrese el kilometraje del vehículo: ")

        new_vehicle = Vehicle(type, model, year, mileage)
        self.vehicles.append(new_vehicle)

    def show_menu(self):
        while True:
            opciones = ["Ver por tipos", "Ver todos", "Salir"]
            for i in range(len(opciones)):
                print(f"{i+1}. {opciones[i]}")
            opcion = input("Ingrese su opcion: ")
            while not opcion.isnumeric() or int(opcion)-1 not in range(len(opciones)):
                opcion = input("Ingreso inválidos, ingrese su opcion: ")

            opcion=int(opcion)
            x=0

            if opcion == 1:
                tipos=["carro", "avión", "barco"]
                for i in range(len(tipos)):
                    print(f"{i+1}. {tipos[i]}")
                type = input("Inserte el tipo de vehículo: ")
                while not type.isnumeric() or int(type)-1 not in range(len(tipos)):
                    type = input("Ingreso inválido, inserte el tipo de vehículo: ")

                for i in range(len(self.vehicles)):
                    if self.vehicles[i].type == tipos[int(type)-1]:
                        print(f"---{x+1}---")
                        print(self.vehicles[i].show())
                        print("")
                        x+=1
                
            elif opcion == 2:
                for i in range(len(self.vehicles)):
                    print(f"---{i+1}---")
                    print(self.vehicles[i].show())
                    print("")

            else:
                break

    def menu(self):
        while True:
            opciones = ["Registrar Vehículo", "Mostrar Vehículos Registrados", "Salir"]
            for i in range(len(opciones)):
                print(f"{i+1}. {opciones[i]}")
            opcion = input("Ingrese su opcion: ")
            while not opcion.isnumeric() or int(opcion)-1 not in range(len(opciones)):
                opcion = input("Ingreso inválidos, ingrese su opcion: ")

            opcion=int(opcion)
            if opcion == 1:
                self.add_vehicle()
            elif opcion == 2:
                self.show_menu()
            else:
                break