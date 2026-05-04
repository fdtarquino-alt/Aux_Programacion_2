class Celular:
    def __init__(self, nroTel, dueno, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueno = dueno
        self.espacio = espacio
        self.ram = ram
        self.nroApp = nroApp
    def __pos__(self):
        self.nroApp += 10
        return self
    def __neg__(self):
        self.espacio -= 5
        if self.espacio < 0: self.espacio = 0
        return self
    def mostrar_datos(self, estado):
        print(f"--- DATOS {estado} ---")
        print(f"Dueño: {self.dueno} | Tel: {self.nroTel}")
        print(f"Espacio: {self.espacio}GB | RAM: {self.ram}GB | Apps: {self.nroApp}")
        print("-" * 45)
mi_cel = Celular("76543210", "Carlos Gomez", 128, 8, 25)
mi_cel.mostrar_datos("ANTES DE LOS OPERADORES")
+mi_cel  
-mi_cel  
mi_cel.mostrar_datos("Despues de operadores(+10 apps, -5GB)")