from Vehicle import Vehicle 

class Car(Vehicle):
    def __init__(self, type, model, year, color, mileage):
        super().__init__(type, model, year, color)
        self.mileage = mileage
    
    def show(self):
        msj = super().show()
        msj += f"Kilometraje: {self.mileage}"
        return msj
