document.addEventListener("DOMContentLoaded", function() {
    // Obtener el elemento del botón
    var button = document.querySelector('.btn-cancelarPedido');

    // Obtener el estado del pedido
    var status = document.querySelector('.status-request .titulos-principal').textContent.trim();

    // Deshabilitar el botón si el estado del pedido es "Entregado"
    if (status === "Entregado") {
        button.disabled = true;
    }
});