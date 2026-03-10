class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.costo = 1.50
    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
        else:
            self.pasajeros = self.capacidad
    def cobrar_pasaje(self):
        return self.pasajeros * self.costo
    def asientos_disponibles(self):
        return self.capacidad - self.pasajeros
bus = Bus(40)               
bus.subir_pasajeros(25)      
print(bus.cobrar_pasaje())   
print(bus.asientos_disponibles())  