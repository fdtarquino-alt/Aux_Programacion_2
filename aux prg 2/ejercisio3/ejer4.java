class Videojuego {
    String nombre;
    String plataforma;
    int jugadores;
    Videojuego() {
        this.nombre = "Desconocido";
        this.plataforma = "Genérica";
        this.jugadores = 1;
    }
    Videojuego(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.jugadores = 1;
    }
    Videojuego(String nombre, String plataforma, int jugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.jugadores = jugadores;
    }
    void agregarJugadores() {
        this.jugadores++;
    }
    void agregarJugadores(int cantidad) {
        this.jugadores += cantidad;
    }
}