document.addEventListener('DOMContentLoaded', function() {
    // Obtener todos los elementos con la clase 'accion-cantidad'
    var botonesCantidad = document.querySelectorAll('.accion-cantidad');

    // Iterar sobre cada botón y agregar un evento de clic
    botonesCantidad.forEach(function(boton) {
        boton.addEventListener('click', function() {
            // Obtener el producto ID desde el atributo data-product-id
            var productId = boton.dataset.productId;

            // Obtener el elemento de cantidad asociado
            var cantidadElement = document.getElementById('cantidad-' + productId);

            // Obtener el valor actual de la cantidad y convertirlo a un número
            var cantidad = parseInt(cantidadElement.innerText);

            // Obtener la acción a realizar (restar o sumar) desde el atributo data-action
            var accion = boton.dataset.action;

            // Actualizar la cantidad en función de la acción
            if (accion === 'restar') {
                cantidad = Math.max(1, cantidad - 1);
            } else if (accion === 'sumar') {
                cantidad += 1;
            }

            // Actualizar el valor de la cantidad en el elemento HTML
            cantidadElement.innerText = cantidad;
        });
    });
});