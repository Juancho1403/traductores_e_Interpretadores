public class Prueba1Patterns {
    public static void main(String[] args) {
        // Declaración de variables
        String producto = "Laptop";
        double precio = 799.99;
        int stock = 5;

        // Mostrar información del producto
        System.out.printf("Producto: %s | Precio: $%.2f | Stock: %d unidades%n", producto, precio, stock);

        // Verificar disponibilidad
        if (stock > 0) {
            System.out.println("El producto está disponible para la venta.");
        } else {
            System.out.println("Producto agotado.");
        }

        // Bucle do-while
        int unidadesVendidas = 0;
        do {
            System.out.println("Vendiendo una unidad... Stock restante: " + (stock - unidadesVendidas));
            unidadesVendidas++;
        } while (unidadesVendidas < stock);

        System.out.println("Se han vendido todas las unidades.");
    }
}
