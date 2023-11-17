$(document).ready(function () {
    $('.boton-eliminar').click(function () {
        const productId = $(this).data('product-id');
        
        // Realizar una solicitud AJAX para actualizar el valor 'carrito' en la base de datos
        $.ajax({
            type: 'GET',
            url: `/quitarProducto/${productId}/`,
            success: function (response) {
                if (response.success) {
                    // Éxito: Puedes agregar lógica adicional aquí si es necesario
                    window.location.href = '/productosCarrito';
                    console.log('Carrito actualizado correctamente.');
                } else {
                    // Manejar el error, por ejemplo, mostrar un mensaje al usuario
                    console.error('Error al actualizar el carrito:', response.error);
                }
            },
            error: function (error) {
                // Manejar errores de AJAX
                console.error('Error en la solicitud AJAX:', error);
            }
        });
    });
});
