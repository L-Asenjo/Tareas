from Vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, type, model, year, color, shell, propulsion):
        super().__init__(type, model, year, color)
        self.shell = shell
        self.propulsion = propulsion
        
    def show(self):
        msj = super().show()
        msj += f"""Material del casco: {self.shell}
        Tipo de Propulsion: {self.propulsion}
                """
        return msj