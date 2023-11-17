

  $(document).ready(function () {
    $('.accion-cantidad').click(function () {
      const accion = $(this).data('action');
      const productoId = $(this).data('product-id');
      const cantidadElement = $('#cantidad-' + productoId);
      const cantidad = parseInt(cantidadElement.text());
      const precioUnitarioElement = $(this).closest('.fila-objeto').find('.precio');
      const subtotalElement = $(this).closest('.fila-objeto').find('.subtotal');

      // Obtener el precio unitario del elemento y validar que sea un número válido
      const precioUnitarioText = precioUnitarioElement.text().replace('$', '').trim();
      const precioUnitario = parseFloat(precioUnitarioText);

      if (!isNaN(cantidad) && cantidad >= 1 && !isNaN(precioUnitario)) {
        if (accion === 'sumar') {
          cantidadElement.text(cantidad + 1);
        } else if (accion === 'restar' && cantidad > 1) {
          cantidadElement.text(cantidad - 1);
        }

        const nuevoSubtotal = parseInt(cantidadElement.text()) * precioUnitario;
        subtotalElement.text('$' + nuevoSubtotal.toFixed(2));

         $.ajax({
           url: '/actualizar_subtotal/',
           type: 'POST',
           data: { productoId: productoId, nuevoSubtotal: nuevoSubtotal },
           success: function (response) {
             // Manejar la respuesta del servidor si es necesario
           },
           error: function (error) {
             console.error('Error en la solicitud AJAX', error);
           }
         });
      } else {
        // Manejar el caso en que la cantidad o el precio no sean válidos
        alert('La cantidad ingresada o el precio no son válidos.');
        // Puedes ajustar este manejo de error según tus necesidades
      }
    });
  });

