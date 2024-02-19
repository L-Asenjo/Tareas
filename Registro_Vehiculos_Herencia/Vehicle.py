class Vehicle:
    def __init__(self, type, model, year, color):
        self.type = type
        self.model = model
        self.year = year
        self.color = color

    def show(self):
        return f"""
        Tipo de Vehículo: {self.type}
        Modelo de Vehículo: {self.model}
        Año del Modelo: {self.year}
        Color: {self.color}        
        """
    
