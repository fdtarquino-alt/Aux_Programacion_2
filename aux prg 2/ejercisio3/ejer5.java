class Aula {
    String nombre;
    int piso;
    String[] estudiantes;
    int[] notas;

    Aula(String nombre, int piso, String[] estudiantes, int[] notas) {
        this.nombre = nombre;
        this.piso = piso;
        this.estudiantes = estudiantes;
        this.notas = notas;
    }
    void mostrarDatos() {
        System.out.println("Aula: " + nombre + " Piso: " + piso);
        for (int i = 0; i < estudiantes.length; i++) {
            System.out.println(estudiantes[i] + " - Nota: " + notas[i]);
        }
    }
    void mostrarDatos(boolean conEstado) {
        System.out.println("Aula: " + nombre + " Piso: " + piso);
        for (int i = 0; i < estudiantes.length; i++) {
            String estado = (notas[i] >= 70) ? "APROBADO" : "REPROBADO";
            System.out.println(estudiantes[i] + " - Nota: " + notas[i] + " → " + estado);
        }
    }
}