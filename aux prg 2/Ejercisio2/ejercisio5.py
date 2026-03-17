class Servidor:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, nombre, diamantes):
        if len(self.jugadores) < 10:
            self.jugadores.append((nombre, diamantes))
        else:
            print("El servidor ya tiene 10 jugadores.")

    def stacks_por_jugador(self):
        for nombre, diamantes in self.jugadores:
            print(f"{nombre} tiene {diamantes // 64} stacks de diamantes")

    def jugador_con_mas_diamantes(self):
        if not self.jugadores:
            print("No hay jugadores en el servidor.")
            return
        nombre, diamantes = max(self.jugadores, key=lambda j: j[1])
        print(f"El jugador con más diamantes es {nombre} con {diamantes} diamantes")

    def total_diamantes(self):
        total = sum(d for _, d in self.jugadores)
        print(f"Total de diamantes en el servidor: {total}")
class Main():
    def __init__(self):
        servidor = Servidor()
        servidor.agregar_jugador("Steve", 120)
        servidor.agregar_jugador("Alex", 65)
        servidor.agregar_jugador("Herobrine", 200)
        servidor.stacks_por_jugador()
        servidor.jugador_con_mas_diamantes()
        servidor.total_diamantes()
Main()
