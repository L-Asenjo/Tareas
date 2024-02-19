from Vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, type, model, year, color, advertiser, airway):
        super().__init__(type, model, year, color)
        self.advertiser = advertiser
        self.airway = airway
    
    def show(self):
        msj = super().show()
        msj += f"""Patrocinador: {self.advertiser}
        Aerolínea: {self.airway}
                """
        return msj