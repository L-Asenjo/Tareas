class Vehicle:
    def __init__(self, type, model, year, mileage):
        self.type = type
        self.model = model
        self.year = year
        self.mileage = mileage

    def show(self):
        return f"""
        Tipo de Vehículo: {self.type}
        Modelo de Vehículo: {self.model}
        Año del Modelo: {self.year}
        Kilometraje: {self.mileage}        
        """
    
