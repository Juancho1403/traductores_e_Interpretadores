public class PruebaPatterns {
    public static void main(String[] args) {
        // Declaración de variables
        String ciudad = "Caracas";
        int temperatura = 28;
        boolean esLluvioso = false;

        // Imprimir mensaje
        System.out.printf("Ciudad: %s | Temperatura: %d°C | Lluvia: %b%n", ciudad, temperatura, esLluvioso);

        // Condicional
        if (temperatura > 30) {
            System.out.println("Hace mucho calor");
        } else if (temperatura >= 20) {
            System.out.println("El clima está agradable");
        } else {
            System.out.println("Hace frío");
        }

        // Bucle while
        int contador = 5;
        while (contador > 0) {
            System.out.println("Cuenta regresiva: " + contador);
            contador--;
        }

        // Comentarios
        // Este es otro comentario de una línea
        /* Bloque de comentario
           para múltiples líneas */
    }
}
