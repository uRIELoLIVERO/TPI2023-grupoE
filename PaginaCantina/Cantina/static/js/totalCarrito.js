$(document).ready(function () {
    // Función para calcular el total y actualizar en la página
    function calcularTotal() {
        let total = 0;

        // Iterar sobre cada elemento con la clase 'fila-objeto'
        $('.fila-objeto').each(function () {
            // Obtener el elemento de cantidad asociado
            const cantidadElement = $(this).find('.cantidad');

            // Obtener el valor actual de la cantidad y convertirlo a un número
            const cantidad = parseInt(cantidadElement.text());

            // Obtener el precio unitario del elemento y validar que sea un número válido
            const precioUnitarioElement = $(this).find('.precio');
            const precioUnitarioText = precioUnitarioElement.text().replace('$', '').trim();
            const precioUnitario = parseFloat(precioUnitarioText);

            // Calcular el subtotal en base a la cantidad y el precio unitario
            const subtotal = isNaN(cantidad) || isNaN(precioUnitario) ? 0 : cantidad * precioUnitario;

            // Sumar al total
            total += subtotal;
        });

        // Actualizar el valor del total en el elemento HTML
        $('#total-carrito').text(total.toFixed(2));
    }

    // Llamar a la función para calcular el total al cargar la página
    calcularTotal();

    // Llamar a la función para calcular el total cada vez que cambie la cantidad
    $('.accion-cantidad').click(function () {
        // Realizar cualquier acción adicional que actualice los subtotales aquí si es necesario

        // Calcular el total después de que cambie la cantidad
        calcularTotal();
    });

    // También puedes llamar a la función calcularTotal en otros eventos que puedan cambiar los subtotales dinámicamente
    // Por ejemplo, después de actualizar otros elementos que afectan a los subtotales.
});
