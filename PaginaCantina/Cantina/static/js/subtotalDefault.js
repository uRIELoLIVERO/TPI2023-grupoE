$(document).ready(function () {
    // Iterar sobre cada elemento con la clase 'fila-objeto'
    $('.fila-objeto').each(function () {
        // Obtener el precio unitario del elemento y validar que sea un número válido
        const precioUnitarioElement = $(this).find('.precio');
        const precioUnitarioText = precioUnitarioElement.text().replace('$', '').trim();
        const precioUnitario = parseFloat(precioUnitarioText);

        // Obtener el elemento de subtotal asociado
        const subtotalElement = $(this).find('.subtotal');

        // Establecer el valor predeterminado del subtotal como el precio unitario
        subtotalElement.text('$' + precioUnitario.toFixed(2));

         $.ajax({
             url: '/actualizar_subtotal/',
             type: 'POST',
             data: { productoId: $(this).data('product-id'), nuevoSubtotal: precioUnitario },
             success: function (response) {
                // Manejar la respuesta del servidor si es necesario
             },
             error: function (error) {
                 console.error('Error en la solicitud AJAX', error);
             }
         });
    });
});
